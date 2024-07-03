"""
Module: 'uasyncio.stream' on micropython-v1.21.0-stm32-PYBV11
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

stream_awrite: Generator  ## = <generator>

class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    awritestr: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Stream:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    awritestr: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...

    _serve: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    awritestr: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

open_connection: Generator  ## = <generator>
start_server: Generator  ## = <generator>
