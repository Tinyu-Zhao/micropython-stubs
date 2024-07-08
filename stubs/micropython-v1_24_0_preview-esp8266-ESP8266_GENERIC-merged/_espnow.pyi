"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/v1.24.0-preview/library/aioespnow.html

---
Module: '_espnow' on micropython-v1.24.0-preview-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': 'preview.98.g4d16a9cce', 'arch': 'xtensa', 'ver': '1.24.0-preview-preview.98.g4d16a9cce', 'cpu': 'ESP8266'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete
from _espnow import ESPNowBase
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

MAX_DATA_LEN: int = 250
MAX_TOTAL_PEER_NUM: int = 20
MAX_ENCRYPT_PEER_NUM: int = 6
ADDR_LEN: int = 6
KEY_LEN: int = 16

class ESPNowBase:
    def del_peer(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def recvinto(self, *args, **kwargs) -> Incomplete: ...
    def set_pmk(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def add_peer(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
