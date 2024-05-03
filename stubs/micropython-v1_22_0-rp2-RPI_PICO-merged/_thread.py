"""
Multithreading support.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/_thread.html

CPython module: :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.

---
Module: '_thread' on micropython-v1.22.0-rp2-RPI_PICO
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'RPI_PICO', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def get_ident(*args, **kwargs) -> Incomplete: ...


def start_new_thread(*args, **kwargs) -> Incomplete: ...


def stack_size(*args, **kwargs) -> Incomplete: ...


def exit(*args, **kwargs) -> Incomplete: ...


def allocate_lock(*args, **kwargs) -> Incomplete: ...


class LockType:
    def locked(self, *args, **kwargs) -> Incomplete: ...

    def release(self, *args, **kwargs) -> Incomplete: ...

    def acquire(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...
