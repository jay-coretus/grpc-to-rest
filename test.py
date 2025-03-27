from leobrain_protos_new.user_service import user_pb2_grpc, user_pb2
from leobrain_protos_new.auth_service import auth_pb2_grpc, auth_pb2
from icecream import ic


GRPC_SERVICES = {
    "UserService": {
        "endpoint_prefix": "/api/userservice",
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
            },
            "CreateOrganization": {
                "path": "/create-org",
                "request_class": user_pb2.CreateOrganizationRequest,
                "response_class": user_pb2.CreateOrganizationResponse,
            }
        },
    },
    "AuthService": {
        "endpoint_prefix": "/api/authservice",
        "methods": {
            "RefreshToken": {
                "path": "/refresh-token",
                "request_class": auth_pb2.User,
                "response_class": auth_pb2.RefreshTokenResponse
            },
            "GenerateToken": {
                "path": "/generate-token",
                "request_class": auth_pb2.User,
                "response_class": auth_pb2.TokenResponse
            }
        }
    }
}

client_stubs = {}
services = []
for service, data in GRPC_SERVICES.items():
    services.append(service)
    ic(service, data)

# ic(services)
# ic(hasattr(GRPC_SERVICES, "UserService"))