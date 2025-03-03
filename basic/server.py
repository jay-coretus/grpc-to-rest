import asyncio
import greeter_pb2
import greeter_pb2_grpc
import logging
import grpc
from icecream import ic
from grpc_reflection.v1alpha import reflection

accessToken = "00000000000"

# Update the Greeter service class to use asynchronous methods
class Greeter(greeter_pb2_grpc.GreeterServicer):

    async def SayHelloMethod(self, request, context):
        # Get the incoming metadata
        incoming_metadata = context.invocation_metadata()
        ic(incoming_metadata)

        # Set trailing metadata
        context.set_trailing_metadata(
            (
                ("set-cookie", f"Cookie:{accessToken}"),
                ("key2", "value2")
            )
        )

        # If the name is '0', abort the request with an error
        if request.name == '0':
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, 'Please enter a different name')

        # Return the response
        return greeter_pb2.SayHelloMethodResponse(message=f"Hello, {request.name}")
    
    async def SayHelloAgainMethod(self, request, context):
        return greeter_pb2.SayHelloAgainMethodResponse(
            message=f"Hello, {request.detail.first_name} {request.detail.last_name}"
        )

# Async function to start the gRPC server
async def serve():
    port = "50051"
    server = grpc.aio.server()  # Use grpc.aio.server() for async server
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    # Enable gRPC reflection
    SERVICE_NAMES = (
        greeter_pb2.DESCRIPTOR.services_by_name["Greeter"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    # Add server port
    server.add_insecure_port(f"[::]:{port}")
    
    # Start the server
    await server.start()
    ic(f"Server started on port {port}")
    
    # Wait for termination
    await server.wait_for_termination()

# Main entry point for the asyncio event loop
if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(serve())
