"""
Module: 'flashbdev' on micropython-v1.24.1-esp32-ESP32_GENERIC_S3
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.3', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

bdev: Incomplete  ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=6291456, label=vfs, encrypted=0>

class Partition:
    RUNNING: int = 1
    TYPE_APP: int = 0
    TYPE_DATA: int = 1
    BOOT: int = 0
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def set_boot(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def find(self, *args, **kwargs) -> Incomplete: ...
    def get_next_update(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
