"""
Module: 'requests' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def request(*args, **kwargs) -> Incomplete:
    ...


def head(*args, **kwargs) -> Incomplete:
    ...


def post(*args, **kwargs) -> Incomplete:
    ...


def patch(*args, **kwargs) -> Incomplete:
    ...


def delete(*args, **kwargs) -> Incomplete:
    ...


def put(*args, **kwargs) -> Incomplete:
    ...


def get(*args, **kwargs) -> Incomplete:
    ...


class Response:
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete  ## <class 'property'> = <property>
    text: Incomplete  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None:
        ...
