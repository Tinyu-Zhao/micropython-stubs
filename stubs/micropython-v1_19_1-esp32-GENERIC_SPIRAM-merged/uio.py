"""
Module: 'uio' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import IO, Optional, Any
import abc
from _typeshed import Incomplete as Incomplete
from stdlib.io import *


def open(name, mode: str = ..., **kwargs) -> Incomplete:
    """
    Open a file. Builtin ``open()`` function is aliased to this function.
    All ports (which provide access to file system) are required to support
    *mode* parameter, but support for other arguments vary by port.
    """
    ...


class IOBase:
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TextIOWrapper(
    IO,
):
    """
    This is type of a file open in text mode, e.g. using ``open(name, "rt")``.
    You should not instantiate this class directly.
    """

    def write(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def readlines(self, *args, **kwargs) -> Any:
        ...

    def seek(self, *args, **kwargs) -> Any:
        ...

    def tell(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *args, **kwargs) -> None:
        ...


class StringIO(
    IO,
):
    def write(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def getvalue(self, *args, **kwargs) -> Any:
        ...

    def seek(self, *args, **kwargs) -> Any:
        ...

    def tell(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, string: Optional[Any] = ...) -> None:
        ...


class BufferedWriter:
    def flush(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class FileIO(
    IO,
):
    """
    This is type of a file open in binary mode, e.g. using ``open(name, "rb")``.
    You should not instantiate this class directly.
    """

    def write(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def readlines(self, *args, **kwargs) -> Any:
        ...

    def seek(self, *args, **kwargs) -> Any:
        ...

    def tell(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *args, **kwargs) -> None:
        ...


class BytesIO(
    IO,
):
    """
    In-memory file-like objects for input/output. `StringIO` is used for
    text-mode I/O (similar to a normal file opened with "t" modifier).
    `BytesIO` is used for binary-mode I/O (similar to a normal file
    opened with "b" modifier). Initial contents of file-like objects
    can be specified with *string* parameter (should be normal string
    for `StringIO` or bytes object for `BytesIO`). All the usual file
    methods like ``read()``, ``write()``, ``seek()``, ``flush()``,
    ``close()`` are available on these objects, and additionally, a
    following method:
    """

    def write(self, *args, **kwargs) -> Any:
        ...

    def flush(self, *args, **kwargs) -> Any:
        ...

    def getvalue(self) -> Incomplete:
        """
        Get the current contents of the underlying buffer which holds data.
        """
        ...

    def seek(self, *args, **kwargs) -> Any:
        ...

    def tell(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, string: Optional[Any] = ...) -> None:
        ...
