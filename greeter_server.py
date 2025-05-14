from concurrent import futures

import grpc

from constants import PORT
from generated_grpc import helloworld_pb2
from generated_grpc import helloworld_pb2_grpc


class GreeterServicer(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(
        self,
        request: helloworld_pb2.HelloRequest,
        context: grpc.ServicerContext,
    ) -> helloworld_pb2.HelloReply:
        print(f"Received SayHello request from: {request.name}")
        return helloworld_pb2.HelloReply(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    helloworld_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    server.add_insecure_port(f"[::]:{PORT}")
    print(f"Starting server. Listening on port {PORT}")
    server.start()
    print("Server started. Waiting for termination signal...")
    server.wait_for_termination()
    print("Server shutting down...")


if __name__ == "__main__":
    serve()
