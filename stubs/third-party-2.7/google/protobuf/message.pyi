# Stubs for google.protobuf.message (Python 2.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Sequence, Optional, Tuple

from .descriptor import FieldDescriptor

class Error(Exception): ...
class DecodeError(Error): ...
class EncodeError(Error): ...

class Message:
    DESCRIPTOR = ... # type: Any
    def __deepcopy__(self, memo=None): ...
    def __eq__(self, other_msg): ...
    def __ne__(self, other_msg): ...
    def MergeFrom(self, other_msg: Message) -> None: ...
    def CopyFrom(self, other_msg: Message) -> None: ...
    def Clear(self) -> None: ...
    def SetInParent(self) -> None: ...
    def IsInitialized(self) -> bool: ...
    def MergeFromString(self, serialized: Any) -> int: ... # TODO: we need to be able to call buffer() on serialized
    def ParseFromString(self, serialized: Any) -> None: ...
    def SerializeToString(self) -> str: ...
    def SerializePartialToString(self) -> str: ...
    def ListFields(self) -> Sequence[Tuple[FieldDescriptor, Any]]: ...
    def HasField(self, field_name: str) -> bool: ...
    def ClearField(self, field_name: str) -> None: ...
    def WhichOneof(self, oneof_group) -> Optional[str]: ...
    def HasExtension(self, extension_handle): ...
    def ClearExtension(self, extension_handle): ...
    def ByteSize(self) -> int: ...