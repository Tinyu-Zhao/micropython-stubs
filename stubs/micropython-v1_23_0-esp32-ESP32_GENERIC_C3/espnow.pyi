"""
Module: 'espnow' on micropython-v1.23.0-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': '', 'arch': '', 'ver': '1.23.0', 'cpu': 'ESP32C3'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

KEY_LEN: int = 16
MAX_DATA_LEN: int = 250
MAX_ENCRYPT_PEER_NUM: int = 6
MAX_TOTAL_PEER_NUM: int = 20
ADDR_LEN: int = 6

class ESPNow:
    _data: list = []
    _none_tuple: tuple = ()
    def peer_count(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def mod_peer(self, *args, **kwargs) -> Incomplete: ...
    def irecv(self, *args, **kwargs) -> Incomplete: ...
    def stats(self, *args, **kwargs) -> Incomplete: ...
    def recvinto(self, *args, **kwargs) -> Incomplete: ...
    def set_pmk(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def add_peer(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def get_peers(self, *args, **kwargs) -> Incomplete: ...
    def get_peer(self, *args, **kwargs) -> Incomplete: ...
    def del_peer(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ESPNowBase:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def mod_peer(self, *args, **kwargs) -> Incomplete: ...
    def get_peers(self, *args, **kwargs) -> Incomplete: ...
    def stats(self, *args, **kwargs) -> Incomplete: ...
    def set_pmk(self, *args, **kwargs) -> Incomplete: ...
    def peer_count(self, *args, **kwargs) -> Incomplete: ...
    def recvinto(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def get_peer(self, *args, **kwargs) -> Incomplete: ...
    def del_peer(self, *args, **kwargs) -> Incomplete: ...
    def add_peer(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
