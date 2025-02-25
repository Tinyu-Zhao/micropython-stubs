"""
Module: 'logging' on micropython-v1.24.1-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

_loggers: dict = {}
NOTSET: Final[int] = 0
INFO: Final[int] = 20
ERROR: Final[int] = 40
_default_datefmt: str = '%Y-%m-%d %H:%M:%S'
_level_dict: dict = {}
WARNING: Final[int] = 30
_default_fmt: str = '%(levelname)s:%(name)s:%(message)s'
DEBUG: Final[int] = 10
CRITICAL: Final[int] = 50
def exception(*args, **kwargs) -> Incomplete:
    ...

def getLogger(*args, **kwargs) -> Incomplete:
    ...

def info(*args, **kwargs) -> Incomplete:
    ...

def shutdown(*args, **kwargs) -> Incomplete:
    ...

def critical(*args, **kwargs) -> Incomplete:
    ...

def error(*args, **kwargs) -> Incomplete:
    ...

def basicConfig(*args, **kwargs) -> Incomplete:
    ...

def debug(*args, **kwargs) -> Incomplete:
    ...

def addLevelName(*args, **kwargs) -> Incomplete:
    ...

def warning(*args, **kwargs) -> Incomplete:
    ...

def log(*args, **kwargs) -> Incomplete:
    ...

def const(*args, **kwargs) -> Incomplete:
    ...


class StreamHandler():
    def emit(self, *args, **kwargs) -> Incomplete:
        ...

    def setFormatter(self, *args, **kwargs) -> Incomplete:
        ...

    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

_stream: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>

class FileHandler():
    def emit(self, *args, **kwargs) -> Incomplete:
        ...

    def setFormatter(self, *args, **kwargs) -> Incomplete:
        ...

    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Logger():
    def hasHandlers(self, *args, **kwargs) -> Incomplete:
        ...

    def warning(self, *args, **kwargs) -> Incomplete:
        ...

    def getEffectiveLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Incomplete:
        ...

    def addHandler(self, *args, **kwargs) -> Incomplete:
        ...

    def exception(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def error(self, *args, **kwargs) -> Incomplete:
        ...

    def critical(self, *args, **kwargs) -> Incomplete:
        ...

    def debug(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Formatter():
    def formatTime(self, *args, **kwargs) -> Incomplete:
        ...

    def usesTime(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class LogRecord():
    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Handler():
    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def setFormatter(self, *args, **kwargs) -> Incomplete:
        ...

    def format(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

