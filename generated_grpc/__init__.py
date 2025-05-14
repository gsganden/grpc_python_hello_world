# Create an alias to compensate for grpcio's inability to get python imports right with
# a sensible directory structure:
#
# - https://github.com/protocolbuffers/protobuf/issues/1491
# - https://github.com/protocolbuffers/protobuf/issues/7061
from importlib import import_module
import sys

module = import_module(".helloworld_pb2", package=__name__)
sys.modules.setdefault("helloworld_pb2", module)
