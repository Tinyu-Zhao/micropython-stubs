"""
Zlib decompression.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/zlib.html

CPython module: :mod:`python:zlib` https://docs.python.org/3/library/zlib.html .

This module allows to decompress binary data compressed with
`DEFLATE algorithm <https://en.wikipedia.org/wiki/DEFLATE>`_
(commonly used in zlib library and gzip archiver). Compression
is not yet implemented.

---
Module: 'zlib' on micropython-v1.20.0-samd-ADAFRUIT_ITSYBITSY_M4_EXPRESS
"""

# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_ITSYBITSY_M4_EXPRESS', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any
from _typeshed import Incomplete


def decompress(data, wbits=0, bufsize=0, /) -> bytes:
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

    def readinto(self, *args, **kwargs) -> Any: ...

    def readline(self, *args, **kwargs) -> Any: ...

    def read(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
