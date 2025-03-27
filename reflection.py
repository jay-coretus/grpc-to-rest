from leobrain_protos_new.user_service import user_pb2_grpc, user_pb2
from leobrain_protos_new.auth_service import auth_pb2_grpc, auth_pb2
import grpc
from grpc_reflection.v1alpha.proto_reflection_descriptor_database import (
    ProtoReflectionDescriptorDatabase,
    FileDescriptorProto,
    FileDescriptorResponse,
    ServerReflectionRequest,
    ServerReflectionResponse,
    ServerReflectionStub,
)
from icecream import ic
from google.protobuf.descriptor_pool import DescriptorPool

channel = grpc.insecure_channel("localhost:50052")
reflection_db = ProtoReflectionDescriptorDatabase(channel)
desc_pool = DescriptorPool(reflection_db)
services = reflection_db.get_services()
ic(services)

service_desc = desc_pool.FindServiceByName(services[1])
ic(service_desc)

methods = service_desc.methods

signup_method = methods[0]
ic(signup_method.name, signup_method.input_type.name, signup_method.output_type.name)
ic(signup_method.CopyToProto())




# for method in methods:
#     # ic(method.name, method.output_type.name, method.input_type.name)
#     ic(method.output_type)