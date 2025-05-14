# gRPC Hello World

"Hello, world" example with gRPC in Python to remind myself how to use it.

## Commands

Generate Python gRPC code:

```bash
uv run python -m grpc_tools.protoc \
    -Iproto_definitions \
    --python_out=. \
    --pyi_out=. \
    --grpc_python_out=. \
    generated_grpc/helloworld.proto
```

Start server:

```bash
uv run greeter_server.py
```

Run client script:

```bash
uv run greeter_client.py
```
