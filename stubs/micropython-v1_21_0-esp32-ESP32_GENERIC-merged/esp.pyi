from _typeshed import Incomplete as Incomplete
from typing import Any, Optional

LOG_NONE: int
LOG_WARNING: int
LOG_VERBOSE: int
LOG_DEBUG: int
LOG_INFO: int
LOG_ERROR: int

def osdebug(level) -> None:
    """
    Turn esp os debugging messages on or off.

    The *level* parameter sets the threshold for the log messages for all esp components.
    The log levels are defined as constants:

        * ``LOG_NONE`` -- No log output
        * ``LOG_ERROR`` -- Critical errors, software module can not recover on its own
        * ``LOG_WARN`` -- Error conditions from which recovery measures have been taken
        * ``LOG_INFO`` -- Information messages which describe normal flow of events
        * ``LOG_DEBUG`` -- Extra information which is not necessary for normal use (values, pointers, sizes, etc)
        * ``LOG_VERBOSE`` -- Bigger chunks of debugging information, or frequent messages
          which can potentially flood the output
    """

def flash_write(byte_offset, bytes) -> Incomplete: ...
def gpio_matrix_in(*args, **kwargs) -> Incomplete: ...
def gpio_matrix_out(*args, **kwargs) -> Incomplete: ...
def flash_user_start() -> Incomplete:
    """
    Read the memory offset at which the user flash space begins.
    """

def flash_erase(sector_no) -> Incomplete: ...
def flash_read(byte_offset, length_or_buffer) -> Incomplete: ...
def flash_size() -> Incomplete:
    """
    Read the total size of the flash memory.
    """
