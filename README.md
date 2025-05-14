# gRPC Hello World

"Hello, world" example with gRPC to remind myself how to use it.

## Commands

Generate Python gRPC code:

```bash
uv run \
    python -m \
    grpc_tools.protoc \
    -I. \
    --python_out=. \
    --pyi_out=. \
    --grpc_python_out=. \
    helloworld.proto
```
