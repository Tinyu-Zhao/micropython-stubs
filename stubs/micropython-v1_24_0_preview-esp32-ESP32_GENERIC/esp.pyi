"""
Module: 'esp' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': 'preview.98.g4d16a9cce', 'arch': 'xtensawin', 'ver': '1.24.0-preview-preview.98.g4d16a9cce', 'cpu': 'ESP32'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

LOG_NONE: int = 0
LOG_WARNING: int = 2
LOG_VERBOSE: int = 5
LOG_DEBUG: int = 4
LOG_INFO: int = 3
LOG_ERROR: int = 1

def osdebug(*args, **kwargs) -> Incomplete: ...
def flash_write(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_in(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_out(*args, **kwargs) -> Incomplete: ...
def flash_user_start(*args, **kwargs) -> Incomplete: ...
def flash_erase(*args, **kwargs) -> Incomplete: ...
def flash_read(*args, **kwargs) -> Incomplete: ...
def flash_size(*args, **kwargs) -> Incomplete: ...
