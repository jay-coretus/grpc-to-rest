from fastapi import Request
from leobrain_protos_new.user_service import user_pb2_grpc, user_pb2
from leobrain_protos_new.auth_service import auth_pb2_grpc, auth_pb2
from icecream import ic
import grpc
from google.protobuf import json_format

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
        },
    },
    "AuthService": {
        "endpoint_prefix": "/api/authservice",
        "methods": {
            "RefreshToken": {
                "path": "/refresh-token",
                "method": "GET",
                "request_class": auth_pb2.User,
                "response_class": auth_pb2.RefreshTokenResponse,
            },
            "GenerateToken": {
                "path": "/generate-token",
                "method": "GET",
                "request_class": auth_pb2.User,
                "response_class": auth_pb2.TokenResponse,
            },
        },
    },
}

# client_stubs = {}
# services = []

# channel = grpc.insecure_channel("localhost:50052")
# client_stubs["UserService"] = user_pb2_grpc.UserServiceStub(channel)
# stub = client_stubs.get("UserService")
# ic(stub)

# service_name = "UserService"
# method_name = "SignIn"
# method_cfg = GRPC_SERVICES[service_name]["methods"][method_name]
# ic(method_cfg)

# request: Request = {"email": "jay.gokani@coretus.com", "password": "Password@123"}
# metadata = []
# grpc_method = getattr(stub, method_name)
# ic(grpc_method)

# grpc_request = method_cfg["request_class"](**request)
# ic(grpc_request)

# grpc_response, call_details = grpc_method.with_call(grpc_request, metadata=metadata)
# ic(grpc_response, call_details)

# response_dict = json_format.MessageToDict(
#     grpc_response, preserving_proto_field_name=True
# )
# ic(response_dict)

for service_name, service_config in GRPC_SERVICES.items():
    ic(service_name)
    for method_name, method_config in service_config["methods"].items():
        ic(method_name, method_config)
        ic(method_config["method"])
        ic('-----------------------------------------------')

    ic('-----------------------------------------------')