"""
Module: 'os' on micropython-v1.21.0-webassembly-GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'webassembly', 'board': 'GENERIC', 'cpu': 'Emscripten', 'mpy': '', 'arch': ''}
# Stubber: v1.15.0
from typing import Any
from _typeshed import Incomplete


def rename(*args, **kwargs) -> Incomplete:
    ...


def rmdir(*args, **kwargs) -> Incomplete:
    ...


def mount(*args, **kwargs) -> Incomplete:
    ...


def unlink(*args, **kwargs) -> Incomplete:
    ...


def umount(*args, **kwargs) -> Incomplete:
    ...


def stat(*args, **kwargs) -> Incomplete:
    ...


def statvfs(*args, **kwargs) -> Incomplete:
    ...


def chdir(*args, **kwargs) -> Incomplete:
    ...


def mkdir(*args, **kwargs) -> Incomplete:
    ...


def remove(*args, **kwargs) -> Incomplete:
    ...


def getcwd(*args, **kwargs) -> Incomplete:
    ...


def listdir(*args, **kwargs) -> Incomplete:
    ...


def ilistdir(*args, **kwargs) -> Incomplete:
    ...


class VfsPosix:
    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    def umount(self, *args, **kwargs) -> Incomplete:
        ...

    def mount(self, *args, **kwargs) -> Incomplete:
        ...

    def statvfs(self, *args, **kwargs) -> Incomplete:
        ...

    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def mkdir(self, *args, **kwargs) -> Incomplete:
        ...

    def open(self, *args, **kwargs) -> Incomplete:
        ...

    def ilistdir(self, *args, **kwargs) -> Incomplete:
        ...

    def chdir(self, *args, **kwargs) -> Incomplete:
        ...

    def getcwd(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
