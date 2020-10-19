
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class ADC:
    def read_u16() -> None: ...
class I2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...
class Pin:
    def af() -> None: ...
    def af_list() -> None: ...
    def debug() -> None: ...
    def dict() -> None: ...
    def gpio() -> None: ...
    def high() -> None: ...
    def init() -> None: ...
    def irq() -> None: ...
    def low() -> None: ...
    def mapper() -> None: ...
    def mode() -> None: ...
    def name() -> None: ...
    def names() -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def pin() -> None: ...
    def port() -> None: ...
    def pull() -> None: ...
    def value() -> None: ...
class RTC:
    def calibration() -> None: ...
    def datetime() -> None: ...
    def info() -> None: ...
    def init() -> None: ...
    def wakeup() -> None: ...
class SPI:
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...
class Signal:
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...
class SoftI2C:
    def init() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def readinto() -> None: ...
    def scan() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
    def writevto() -> None: ...
class SoftSPI:
    def deinit() -> None: ...
    def init() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def write() -> None: ...
    def write_readinto() -> None: ...
class Timer:
    def deinit() -> None: ...
    def init() -> None: ...
class UART:
    def any() -> None: ...
    def deinit() -> None: ...
    def init() -> None: ...
    def irq() -> None: ...
    def read() -> None: ...
    def readchar() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def sendbreak() -> None: ...
    def write() -> None: ...
    def writechar() -> None: ...
class WDT:
    def feed() -> None: ...
def bootloader() -> None: ...
def deepsleep() -> None: ...
def disable_irq() -> None: ...
def enable_irq() -> None: ...
def freq() -> None: ...
def idle() -> None: ...
def info() -> None: ...
def lightsleep() -> None: ...
def reset() -> None: ...
def reset_cause() -> None: ...
def rng() -> None: ...
def sleep() -> None: ...
def soft_reset() -> None: ...
def time_pulse_us() -> None: ...
def unique_id() -> None: ...
