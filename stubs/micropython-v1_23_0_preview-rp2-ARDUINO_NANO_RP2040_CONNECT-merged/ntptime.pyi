"""
Module: 'ntptime' on micropython-v1.22.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'build': '', 'ver': '1.22.1', 'version': '1.22.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.16.3
from __future__ import annotations
from _typeshed import Incomplete

host: str = "pool.ntp.org"
timeout: int = 1

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
