import grpc
from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import JSONResponse
from google.protobuf import json_format
import logging
from typing import Dict, Any, List, Tuple
from fastapi.middleware.cors import CORSMiddleware

# Import your generated proto modules
import greeter_pb2
import greeter_pb2_grpc
import user_pb2, user_pb2_grpc

# FastAPI app instance
app = FastAPI()
# Add CORS middleware to allow any and every request
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Simple service configuration
# This is where you'll add new RPC methods as you define them in your proto file
GRPC_SERVICES = {
    "Greeter": {
        "endpoint_prefix": "/greeter",
        "methods": {
            "SayHelloMethod": {
                "path": "/say-hello",
                "request_class": greeter_pb2.SayHelloMethodRequest,
                "response_class": greeter_pb2.SayHelloMethodResponse,
            },
            "SayHelloAgainMethod": {
                "path": "/say-hello-again",
                "request_class": greeter_pb2.SayHelloAgainMethodRequest,
                "response_class": greeter_pb2.SayHelloAgainMethodResponse,
            },
        },
    },
    "UserService": {
        "endpoint_prefix": "/userservice",
        "methods": {
            "SignUp": {
                "path": "/sign-up",
                "request_class": user_pb2.SignupUser,
                "response_class": user_pb2.UsersResponse,
            },
            "SignIn": {
                "path": "/sign-in",
                "request_class": user_pb2.SignInReq,
                "response_class": user_pb2.ActionResponse,
            },
            "ForgotPassword": {
                "path": "/forgot-password",
                "request_class": user_pb2.ForgotPasswordReq,
                "response_class": user_pb2.ActionResponse,
            }
        },
    },
}

# gRPC client stub cache
client_stubs = {}


def get_grpc_client(service_name: str):
    """
    Get or create a gRPC client stub for the specified service.

    Args:
        service_name (str): The name of the gRPC service.

    Returns:
        The gRPC client stub for the specified service.

    Raises:
        KeyError: If the service name is not found in the client stubs.
    """
    if service_name not in client_stubs:
        # Create the channel and stub
        channel = grpc.insecure_channel("localhost:50052")

        # if service_name == "Greeter":
        #     client_stubs[service_name] = greeter_pb2_grpc.GreeterStub(channel)
        # Add more services as needed
        if service_name == "UserService":
            client_stubs[service_name] = user_pb2_grpc.UserServiceStub(channel)

    return client_stubs[service_name]


def extract_headers_for_metadata(request: Request) -> List[Tuple[str, str]]:
    """
    Extract gRPC metadata from HTTP headers.

    Args:
        request (Request): The FastAPI request object.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing the header name and value.

    Note:
        Excludes certain headers such as 'host', 'content-length', and 'content-type'.
    """
    metadata = []
    excluded_headers = {"host", "content-length", "content-type"}

    for header_name, header_value in request.headers.items():
        if header_name.lower() not in excluded_headers:
            metadata.append((header_name.lower(), header_value))

    return metadata


# Register all endpoints from the configuration
for service_name, service_config in GRPC_SERVICES.items():
    for method_name, method_config in service_config["methods"].items():
        endpoint_path = method_config["path"]

        # Define the endpoint handler
        @app.post(endpoint_path)
        async def handle_grpc_request(
            request: Request,
            request_data: Dict[str, Any] = Body(...),
            svc_name: str = service_name,
            mth_name: str = method_name,
        ):
            # Get method config to use in the handler
            method_cfg = GRPC_SERVICES[svc_name]["methods"][mth_name]

            try:
                # Get the gRPC client
                stub = get_grpc_client(svc_name)

                # Create the request object
                grpc_request = method_cfg["request_class"](**request_data)

                # Extract metadata from headers
                metadata = extract_headers_for_metadata(request)

                # Get the gRPC method
                grpc_method = getattr(stub, mth_name)

                # Make the gRPC call with metadata
                grpc_response, call_details = grpc_method.with_call(
                    grpc_request, metadata=metadata
                )

                # Convert response to dict
                response_dict = json_format.MessageToDict(
                    grpc_response, preserving_proto_field_name=True
                )

                # Get trailing metadata for headers
                response_headers = {}
                for key, value in call_details.trailing_metadata():
                    if key.lower() == "set-cookie":
                        response_headers["Set-Cookie"] = value
                    else:
                        response_headers[f"X-Grpc-{key}"] = value

                # Create the response with headers
                response = JSONResponse(content=response_dict)
                for k, v in response_headers.items():
                    response.headers[k] = v

                return response

            except grpc.RpcError as e:
                status_code = e.code().value[0] if hasattr(e, "code") else 500
                detail = e.details() if hasattr(e, "details") else str(e)
                logging.error(f"gRPC call failed: {detail}")
                raise HTTPException(status_code=status_code, detail=detail)
            except Exception as e:
                logging.exception(f"Error handling request: {str(e)}")
                raise HTTPException(
                    status_code=500, detail=f"Internal server error: {str(e)}"
                )


# Simple function to add a new gRPC method to the configuration
def register_grpc_method(
    service_name: str,
    method_name: str,
    endpoint_path: str,
    request_class,
    response_class,
):
    """
    Utility function to register a new gRPC method at runtime.

    Args:
        service_name (str): The name of the gRPC service.
        method_name (str): The name of the gRPC method.
        endpoint_path (str): The endpoint path for the method.
        request_class: The request class for the gRPC method.
        response_class: The response class for the gRPC method.

    Note:
        FastAPI routes cannot be added dynamically after startup. For true dynamic addition,
        you would need to restart the server or use a different approach like a middleware.
    """
    if service_name not in GRPC_SERVICES:
        GRPC_SERVICES[service_name] = {
            "endpoint_prefix": f"/{service_name.lower()}",
            "methods": {},
        }

    GRPC_SERVICES[service_name]["methods"][method_name] = {
        "path": endpoint_path,
        "request_class": request_class,
        "response_class": response_class,
    }

    logging.info(
        f"Registered new gRPC method: {service_name}.{method_name} at {endpoint_path}"
    )


if __name__ == "__main__":
    import uvicorn

    logging.basicConfig(level=logging.INFO)

    # Example of adding a method if you add it to your proto file
    # register_grpc_method(
    #     "Greeter",
    #     "SayHelloAgain",
    #     "/say-hello-again",
    #     greeter_pb2.SayHelloAgainRequest,
    #     greeter_pb2.SayHelloAgainResponse
    # )

    uvicorn.run(app, host="0.0.0.0", port=8000)
