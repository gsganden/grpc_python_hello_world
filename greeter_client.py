from textwrap import dedent

import grpc

from constants import PORT
from generated_grpc import helloworld_pb2
from generated_grpc import helloworld_pb2_grpc


def run_client():
    print(f"Attempting to connect to server at localhost:{PORT}")
    with grpc.insecure_channel(f"localhost:{PORT}") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        name_to_greet = "gRPC Python User"
        request = helloworld_pb2.HelloRequest(name=name_to_greet)
        print(f"Sending request to SayHello with name: {name_to_greet}")

        try:
            response = stub.SayHello(request)
            print(f"Greeter client received: {response.message}")
        except grpc.RpcError as e:
            print(f"RPC failed: {e.code()} - {e.details()}")
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                print(
                    dedent(
                        """\
                            The server is likely unavailable. Ensure `greeter_server.py`
                            is running.
                        """
                    )
                )


if __name__ == "__main__":
    run_client()
