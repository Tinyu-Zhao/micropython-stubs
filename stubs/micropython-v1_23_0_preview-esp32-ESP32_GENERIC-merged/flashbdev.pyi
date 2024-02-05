"""
Module: 'flashbdev' on micropython-v1.23.0-preview-esp32-ESP32_GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.23.0-preview', 'build': 'preview.6.g3d0b6276f', 'ver': '1.23.0-preview-preview.6.g3d0b6276f', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.3
from __future__ import annotations
from _typeshed import Incomplete

bdev: Incomplete  ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>

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
