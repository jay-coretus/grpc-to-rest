from http.cookies import SimpleCookie
import grpc
from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.responses import JSONResponse
from google.protobuf import json_format
import logging
from typing import Dict, Any, List, Tuple
from fastapi.middleware.cors import CORSMiddleware
from icecream import ic
# Import your generated proto modules
from leobrain_protos_new.auth_service import auth_pb2, auth_pb2_grpc
from protos import user_pb2_grpc, user_pb2
from custom_methods.my_method import my_method, set_cookies

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
GRPC_SERVICES = {
    "UserService": {
        "endpoint_prefix": "/api/userservice",
        "methods": {
            "SignUp": {
                "path": "/sign-up",
                "method": "POST",
                "request_class": user_pb2.SignupUser,
                "response_class": user_pb2.UsersResponse,
            },
            "SignIn": {
                "path": "/sign-in",
                "method": "POST",
                "request_class": user_pb2.SignInReq,
                "response_class": user_pb2.ActionResponse,
                "pre_method_injection": my_method,
                "post_method_injection": set_cookies,
            },
            "ForgotPassword": {
                "path": "/forgot-password",
                "method": "POST",
                "request_class": user_pb2.ForgotPasswordReq,
                "response_class": user_pb2.ActionResponse,
            },
            "CreateOrganization": {
                "path": "/create-org",
                "method": "POST",
                "request_class": user_pb2.CreateOrganizationRequest,
                "response_class": user_pb2.CreateOrganizationResponse,
            },
            "UpdateOrganization": {
                "path": "/update-org",
                "method": "POST",
                "request_class": user_pb2.UpdateOrganizationRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "ViewOrganization": {
                "path": "/view-org",
                "method": "GET",
                "request_class": user_pb2.ViewOrganizationRequest,
                "response_class": user_pb2.ViewOrganizationResponse,
            },
            "DeleteOrganization": {
                "path": "/delete-org",
                "method": "DELETE",
                "request_class": user_pb2.DeleteOrganizationRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "UpdateProfile": {
                "path": "/update-profile",
                "method": "POST",
                "request_class": user_pb2.UpdateProfileRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "UpdateEmail": {
                "path": "/update-email",
                "method": "POST",
                "request_class": user_pb2.UpdateEmailRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "UpdatePassword": {
                "path": "/update-password",
                "method": "POST",
                "request_class": user_pb2.UpdatePasswordRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "ChangeOrgProfilePicture": {
                "path": "/change-org-profile-pic",
                "method": "POST",
                "request_class": user_pb2.ChangeProfilePictureRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "DeleteUser": {
                "path": "/delete-user",
                "method": "DELETE",
                "request_class": user_pb2.DeleteUserRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "ChangeProfilePicture": {
                "path": "/change-profile-pic",
                "method": "POST",
                "request_class": user_pb2.ChangeProfilePictureRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "SocialSignUp": {
                "path": "/social-sign-up",
                "method": "POST",
                "request_class": user_pb2.SocialUser,
                "response_class": user_pb2.UsersResponse,
            },
            "VerifyInvitation": {
                "path": "/verify-invitation",
                "method": "POST",
                "request_class": user_pb2.VerifyInvitationReq,
                "response_class": user_pb2.VerifyInvitationRes,
            },
            "DisplayUser": {
                "path": "/display-user",
                "method": "GET",
                "request_class": user_pb2.DisplayUserRequest,
                "response_class": user_pb2.DisplayUserResponse,
            },
            # "SingleUserInfo": {
            #     "path": "/single-user-info",
            #     "method": "GET",
            #     "request_class": user_pb2.SingleUserInfoRequest,
            #     "response_class": user_pb2.SingleUserInfoResponse,
            # },
            "RemoveUser": {
                "path": "/remove-user",
                "method": "DELETE",
                "request_class": user_pb2.RemoveUserRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "RemoveService": {
                "path": "/remove-service",
                "method": "DELETE",
                "request_class": user_pb2.RemoveServiceRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "AssignService": {
                "path": "/assign-service",
                "method": "POST",
                "request_class": user_pb2.AssignServiceRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "UpdateOrganizationRole": {
                "path": "/update-org-role",
                "method": "POST",
                "request_class": user_pb2.UpdateOrganizationRoleRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "UpdateServiceRole": {
                "path": "/update-service-role",
                "method": "POST",
                "request_class": user_pb2.UpdateServiceRoleRequest,
                "response_class": user_pb2.MessageResponse,
            },
            "ViewProfile": {
                "path": "/view-profile",
                "method": "GET",
                "request_class": user_pb2.Empty,
                "response_class": user_pb2.ViewProfileResponse,
            },
            "CreateInvitation": {
                "path": "/create-invitation",
                "method": "POST",
                "request_class": user_pb2.CreateInvitationRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "DisplayInvitation": {
                "path": "/display-invitation",
                "method": "GET",
                "request_class": user_pb2.Empty,
                "response_class": user_pb2.DisplayInvitationResponse,
            },
            "DeleteInvitation": {
                "path": "/delete-invitation",
                "method": "DELETE",
                "request_class": user_pb2.DeleteInvitationRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "ResetPassword": {
                "path": "/reset-password",
                "method": "POST",
                "request_class": user_pb2.ResetPasswordReq,
                "response_class": user_pb2.ActionResponse,
            },
            "ChangePassword": {
                "path": "/change-password",
                "method": "POST",
                "request_class": user_pb2.ChangePasswordReq,
                "response_class": user_pb2.ActionResponse,
            },
            "VerifyUser": {
                "path": "/verify-user",
                "method": "POST",
                "request_class": user_pb2.VerifyUserRequest,
                "response_class": user_pb2.ActionResponse,
            },
            "Services": {
                "path": "/services",
                "method": "GET",
                "request_class": user_pb2.EmptyRequest,
                "response_class": user_pb2.ServicesResponse,
            },
            # "ChangeDomain": {
            #     "path": "/change-domain",
            #     "method": "POST",
            #     "request_class": user_pb2.ChangeDomainRequest,
            #     "response_class": user_pb2.MessageResponse,
            # }
        },
    },
    "AuthService": {
        "endpoint_prefix": "/api/authservice",
        "methods": {
            "RefreshToken": {
                "path": "/refresh-token",
                "method": "GET",
                "request_class": auth_pb2.User,
                "response_class": auth_pb2.RefreshTokenResponse
            },
            "GenerateToken": {
                "path": "/generate-token",
                "method": "POST",
                "request_class": auth_pb2.User,
                "response_class": auth_pb2.TokenResponse
            }
        }
    }
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
        if service_name == "UserService":
            channel = grpc.insecure_channel("localhost:50052")
            client_stubs[service_name] = user_pb2_grpc.UserServiceStub(channel)
        elif service_name == "AuthService":
            channel = grpc.insecure_channel("localhost:50051")
            client_stubs[service_name] = auth_pb2_grpc.AuthServiceStub(channel)
        else:
            raise KeyError(f"Unknown service: {service_name}")

    return client_stubs[service_name]


def extract_headers_for_metadata(request: Request) -> List[Tuple[str, str]]:
    """
    Extract gRPC metadata from HTTP headers.
    Also parses the 'cookie' header and adds specific cookie values
    as metadata keys ("accessToken", "refreshToken", "sessionId").
    """
    metadata = []
    # Exclude these headers if needed
    excluded_headers = {"host", "content-length", "content-type"}
    
    for header_name, header_value in request.headers.items():
        lower_name = header_name.lower()
        if lower_name in excluded_headers:
            continue

        if lower_name == "cookie":
            # Parse the cookie header
            cookie = SimpleCookie()
            cookie.load(header_value)
            # Extract specific cookie values if they exist and add to metadata.
            if "access_token" in cookie:
                metadata.append(("access_token", cookie["access_token"].value))
            if "refresh_token" in cookie:
                metadata.append(("refresh_token", cookie["refresh_token"].value))
            if "session_id" in cookie:
                metadata.append(("session_id", cookie["session_id"].value))
        else:
            metadata.append((lower_name, header_value))
    ic(metadata)
    return metadata

def map_grpc_error_to_http_code(code: grpc.StatusCode) -> int:
    """
    Map a gRPC status code to an appropriate HTTP status code.
    """
    mapping = {
         grpc.StatusCode.OK: 200,
         grpc.StatusCode.CANCELLED: 499,
         grpc.StatusCode.UNKNOWN: 500,
         grpc.StatusCode.INVALID_ARGUMENT: 400,
         grpc.StatusCode.DEADLINE_EXCEEDED: 504,
         grpc.StatusCode.NOT_FOUND: 404,
         grpc.StatusCode.ALREADY_EXISTS: 409,
         grpc.StatusCode.PERMISSION_DENIED: 403,
         grpc.StatusCode.RESOURCE_EXHAUSTED: 429,
         grpc.StatusCode.FAILED_PRECONDITION: 400,
         grpc.StatusCode.ABORTED: 409,
         grpc.StatusCode.OUT_OF_RANGE: 400,
         grpc.StatusCode.UNIMPLEMENTED: 501,
         grpc.StatusCode.INTERNAL: 500,
         grpc.StatusCode.UNAVAILABLE: 503,
         grpc.StatusCode.DATA_LOSS: 500,
         grpc.StatusCode.UNAUTHENTICATED: 401,
    }
    return mapping.get(code, 500)

def create_endpoint_handler(service_name: str, method_name: str):
    """
    Create a handler function for a specific gRPC method endpoint.
    
    Args:
        service_name (str): The name of the gRPC service.
        method_name (str): The name of the gRPC method.
        
    Returns:
        function: The handler function for the endpoint.
    """
    async def handler(request: Request, request_data: Dict[str, Any] = Body(...)):
        method_cfg = GRPC_SERVICES[service_name]["methods"][method_name]
        
        # Run custom logic before the gRPC call if provided
        pre_logic = method_cfg.get("pre_method_injection")
        if callable(pre_logic):
            pre_logic(request, request_data)
        
        try:
            # Get the gRPC client
            stub = get_grpc_client(service_name)

            # Create the gRPC request object from the request data
            grpc_request = method_cfg["request_class"](**request_data)

            # Extract metadata from headers
            metadata = extract_headers_for_metadata(request)
            # Get the gRPC method from the stub
            grpc_method = getattr(stub, method_name)

            # Make the gRPC call with metadata
            grpc_response, call_details = grpc_method.with_call(
                grpc_request, metadata=metadata
            )
            # Convert the gRPC response to a dict
            response_dict = json_format.MessageToDict(
                grpc_response, preserving_proto_field_name=True
            )

            # Process trailing metadata for headers
            response_headers = {}
            for key, value in call_details.trailing_metadata():
                if key.lower() == "set-cookie":
                    response_headers["Set-Cookie"] = value
                else:
                    response_headers[f"X-Grpc-{key}"] = value
            
            # Check if a post-method injection is provided (for example, to set cookies)
            post_logic = method_cfg.get("post_method_injection")
            if callable(post_logic):
                # The post_logic function is expected to return a FastAPI Response with cookies set.
                response = post_logic(grpc_response, call_details)
                # Merge any additional headers if needed
                for k, v in response_headers.items():
                    response.headers[k] = v
                return response
            else:
                # Otherwise, return a standard JSONResponse with headers
                response = JSONResponse(content=response_dict)
                for k, v in response_headers.items():
                    response.headers[k] = v
                return response

        except grpc.RpcError as e:
            grpc_code = e.code()
            http_status_code = map_grpc_error_to_http_code(grpc_code)
            detail = e.details() if hasattr(e, "details") else str(e)
            logging.error(f"gRPC call failed: {detail}")
            raise HTTPException(status_code=http_status_code, detail=detail)
        except Exception as e:
            logging.exception(f"Error handling request: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
    return handler


# Composite Endpoint: SignUp + SignIn
@app.post("/api/userservice/sign-up-and-sign-in")
async def sign_up_and_sign_in(request: Request, request_data: Dict[str, Any] = Body(...)):
    try:
        stub = get_grpc_client("UserService")
        metadata = extract_headers_for_metadata(request)

        # 1. Call SignUp
        sign_up_config = GRPC_SERVICES["UserService"]["methods"]["SignUp"]
        sign_up_request = sign_up_config["request_class"](**request_data)
        sign_up_response, sign_up_call_details = stub.SignUp.with_call(
            sign_up_request, metadata=metadata
        )
        ic("SignUp completed", sign_up_response)

        # 2. Call SignIn with the same data
        sign_in_config = GRPC_SERVICES["UserService"]["methods"]["SignIn"]
        sign_in_request = sign_in_config["request_class"](**request_data)
        sign_in_response, sign_in_call_details = stub.SignIn.with_call(
            sign_in_request, metadata=metadata
        )
        ic("SignIn completed", sign_in_response)

        # Combine both responses
        response_content = {
            "sign_up": json_format.MessageToDict(
                sign_up_response, preserving_proto_field_name=True
            ),
            "sign_in": json_format.MessageToDict(
                sign_in_response, preserving_proto_field_name=True
            )
        }

        # Return the combined response
        return JSONResponse(content=response_content)

    except grpc.RpcError as e:
        grpc_code = e.code()
        http_status_code = map_grpc_error_to_http_code(grpc_code)
        detail = e.details() if hasattr(e, "details") else str(e)
        logging.error(f"Composite gRPC call failed: {detail}")
        raise HTTPException(status_code=http_status_code, detail=detail)
    except Exception as e:
        logging.exception(f"Error handling composite request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/api/composite/signin-and-generate-token")
async def composite_signin_and_generate_token(request: Request, request_data: Dict[str, Any] = Body(...)):
    try:
        # Extract metadata (includes parsed cookies etc.)
        metadata = extract_headers_for_metadata(request)
        
        # --- Call SignIn from UserService ---
        user_stub = get_grpc_client("UserService")
        sign_in_cfg = GRPC_SERVICES["UserService"]["methods"]["SignIn"]
        # Create the SignIn request object (pre-method injection will run if defined)
        sign_in_request = sign_in_cfg["request_class"](**request_data)
        # Call SignIn with metadata
        sign_in_response, sign_in_details = user_stub.SignIn.with_call(
            sign_in_request, metadata=metadata
        )
        ic("SignIn completed", sign_in_response)
        
        # --- Call GenerateToken from AuthService ---
        # Prepare request data for GenerateToken by removing unwanted fields.
        generate_token_data = request_data.copy()
        # Remove fields that are not part of the AuthService.User proto (e.g., "password")
        generate_token_data.pop("password", None)
        
        auth_stub = get_grpc_client("AuthService")
        generate_token_cfg = GRPC_SERVICES["AuthService"]["methods"]["GenerateToken"]
        generate_token_request = generate_token_cfg["request_class"](**generate_token_data)
        generate_token_response, generate_token_details = auth_stub.GenerateToken.with_call(
            generate_token_request, metadata=metadata
        )
        ic("GenerateToken completed", generate_token_response)
        
        # Combine both responses into one JSON payload
        response_content = {
            "sign_in": json_format.MessageToDict(
                sign_in_response, preserving_proto_field_name=True
            ),
            "generate_token": json_format.MessageToDict(
                generate_token_response, preserving_proto_field_name=True
            )
        }
        return JSONResponse(content=response_content)

    except grpc.RpcError as e:
        grpc_code = e.code()
        http_status_code = map_grpc_error_to_http_code(grpc_code)
        detail = e.details() if hasattr(e, "details") else str(e)
        logging.error(f"Composite call failed: {detail}")
        raise HTTPException(status_code=http_status_code, detail=detail)
    except Exception as e:
        logging.exception(f"Error handling composite request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")




# Register all individual gRPC routes
for service_name, service_config in GRPC_SERVICES.items():
    for method_name, method_config in service_config["methods"].items():
        full_path = f"{service_config['endpoint_prefix']}{method_config['path']}"
        handler = create_endpoint_handler(service_name, method_name)
 
        app.add_api_route(full_path, handler, methods=[method_config["method"]])
        
        logging.info(f"Registered static route for {service_name}.{method_name} at {full_path}")


if __name__ == "__main__":
    import uvicorn

    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8000)
