"""
Module: 'uzlib' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any
from _typeshed import Incomplete as Incomplete


def decompress(data, wbits: int = ..., bufsize: int = ...) -> bytes:
    """
    Return decompressed *data* as bytes. *wbits* is DEFLATE dictionary window
    size used during compression (8-15, the dictionary size is power of 2 of
    that value). Additionally, if value is positive, *data* is assumed to be
    zlib stream (with zlib header). Otherwise, if it's negative, it's assumed
    to be raw DEFLATE stream. *bufsize* parameter is for compatibility with
    CPython and is ignored.
    """
    ...


class DecompIO:
    """
    Create a `stream` wrapper which allows transparent decompression of
    compressed data in another *stream*. This allows to process compressed
    streams with data larger than available heap size. In addition to
    values described in :func:`decompress`, *wbits* may take values
    24..31 (16 + 8..15), meaning that input stream has gzip header.

    Difference to CPython

       This class is MicroPython extension. It's included on provisional
       basis and may be changed considerably or removed in later versions.
    """

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def readline(self, *args, **kwargs) -> Any:
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, stream, wbits: int = ...) -> None:
        ...
