from typing import Any, List, Optional, Tuple

HEAP_DATA: Any
HEAP_EXEC: Any
WAKEUP_ALL_LOW: Any
WAKEUP_ANY_HIGH: Any

class Partition:
    BOOT: Any
    RUNNING: Any
    TYPE_APP: Any
    TYPE_DATA: Any
    def __init__(self, id) -> None: ...
    @classmethod
    def find(cls, type=..., subtype: int = ..., label: Any | None = ...) -> List: ...
    def info(self) -> Tuple: ...
    def readblocks(self, block_num, buf, offset: Optional[int]) -> Any: ...
    def writeblocks(self, block_num, buf, offset: Optional[int]) -> Any: ...
    def ioctl(self, cmd, arg) -> Any: ...
    def set_boot(self) -> None: ...
    def get_next_update(self) -> Partition: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls) -> Any: ...

class RMT:
    def __init__(self, channel, *, pin: Any | None = ..., clock_div: int = ..., idle_level: bool = ..., tx_carrier: Any | None = ...) -> None: ...
    def source_freq(self) -> Any: ...
    def clock_div(self) -> Any: ...
    def wait_done(self, *, timeout: int = ...) -> bool: ...
    def loop(self, enable_loop) -> None: ...
    def write_pulses(self, duration, data: bool = ...) -> Any: ...
    @staticmethod
    def bitstream_channel(value: Optional[Any]) -> int: ...

class ULP:
    def __init__(self) -> None: ...
    def set_wakeup_period(self, period_index, period_us) -> None: ...
    def load_binary(self, load_addr, program_binary) -> None: ...
    def run(self, entry_point) -> Any: ...

class NVS:
    def __init__(self, namespace) -> None: ...
    def set_i32(self, key, value) -> None: ...
    def get_i32(self, key) -> int: ...
    def set_blob(self, key, value) -> None: ...
    def get_blob(self, key, buffer) -> int: ...
    def erase_key(self, key) -> Any: ...
    def commit(self) -> Any: ...

def wake_on_touch(wake) -> None: ...
def wake_on_ext0(pin, level) -> None: ...
def wake_on_ext1(pins, level) -> None: ...
def raw_temperature() -> int: ...
def hall_sensor() -> int: ...
def idf_heap_info(capabilities) -> List[Tuple]: ...
