"""
Module: 'asyncio.stream' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete

stream_awrite: Incomplete  ## <class 'generator'> = <generator>


class StreamWriter:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Stream:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Server:
    def close(self, *args, **kwargs) -> Incomplete: ...

    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class StreamReader:
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awrite: Incomplete  ## <class 'generator'> = <generator>
    readexactly: Incomplete  ## <class 'generator'> = <generator>
    awritestr: Incomplete  ## <class 'generator'> = <generator>
    drain: Incomplete  ## <class 'generator'> = <generator>
    readinto: Incomplete  ## <class 'generator'> = <generator>
    read: Incomplete  ## <class 'generator'> = <generator>
    aclose: Incomplete  ## <class 'generator'> = <generator>
    readline: Incomplete  ## <class 'generator'> = <generator>
    wait_closed: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


open_connection: Incomplete  ## <class 'generator'> = <generator>
start_server: Incomplete  ## <class 'generator'> = <generator>
