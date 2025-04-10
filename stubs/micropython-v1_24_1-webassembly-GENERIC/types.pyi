"""
Module: 'types' on micropython-v1.24.1-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def _calculate_meta(*args, **kwargs) -> Incomplete:
    ...

def prepare_class(*args, **kwargs) -> Incomplete:
    ...

def new_class(*args, **kwargs) -> Incomplete:
    ...


class ModuleType():
    def __init__(self, *argv, **kwargs) -> None:
        ...

SimpleNamespace: Incomplete ## <class 'NoneType'> = None

class MethodType():
    def __init__(self, *argv, **kwargs) -> None:
        ...

CodeType: Incomplete ## <class 'NoneType'> = None

class BuiltinFunctionType():
    def __init__(self, *argv, **kwargs) -> None:
        ...

TracebackType: Incomplete ## <class 'NoneType'> = None

class BuiltinMethodType():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class FunctionType():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class GeneratorType():
    def pend_throw(self, *args, **kwargs) -> Incomplete:
        ...

    def throw(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

FrameType: Incomplete ## <class 'NoneType'> = None
MemberDescriptorType: Incomplete ## <class 'NoneType'> = None
MappingProxyType: Incomplete ## <class 'NoneType'> = None
GetSetDescriptorType: Incomplete ## <class 'NoneType'> = None

class LambdaType():
    def __init__(self, *argv, **kwargs) -> None:
        ...

