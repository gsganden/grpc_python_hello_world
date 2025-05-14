# gRPC Hello World

"Hello, world" example with gRPC in Python to remind myself how to use it.

## Commands

Generate Python gRPC code:

```bash
uv run python -m grpc_tools.protoc \
    -Iprotos \
    --python_out=generated_grpc \
    --pyi_out=generated_grpc \
    --grpc_python_out=generated_grpc \
    helloworld.proto
```

Start server:

```bash
uv run greeter_server.py
```

Run client script:

```bash
uv run greeter_client.py
```
