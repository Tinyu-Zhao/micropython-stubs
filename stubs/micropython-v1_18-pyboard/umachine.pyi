from typing import Any

class RTC:
    def __init__(self, *argv) -> None: ...
    def calibration(self, *args) -> Any: ...
    def datetime(self, *args) -> Any: ...
    def info(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def wakeup(self, *args) -> Any: ...

class ADC:
    def __init__(self, *argv) -> None: ...
    CORE_TEMP: int
    CORE_VBAT: int
    CORE_VREF: int
    VREF: int
    def read_u16(self, *args) -> Any: ...

DEEPSLEEP_RESET: int
HARD_RESET: int

class I2C:
    def __init__(self, *argv) -> None: ...
    def readinto(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def readfrom(self, *args) -> Any: ...
    def readfrom_into(self, *args) -> Any: ...
    def readfrom_mem(self, *args) -> Any: ...
    def readfrom_mem_into(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def writeto(self, *args) -> Any: ...
    def writeto_mem(self, *args) -> Any: ...
    def writevto(self, *args) -> Any: ...

class I2S:
    def __init__(self, *argv) -> None: ...
    def readinto(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    MONO: int
    RX: int
    STEREO: int
    TX: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def shift(self, *args) -> Any: ...

PWRON_RESET: int

class Pin:
    def __init__(self, *argv) -> None: ...
    @classmethod
    def dict(cls, *args) -> Any: ...
    def value(self, *args) -> Any: ...
    AF1_TIM1: int
    AF1_TIM2: int
    AF2_TIM3: int
    AF2_TIM4: int
    AF2_TIM5: int
    AF3_TIM10: int
    AF3_TIM11: int
    AF3_TIM8: int
    AF3_TIM9: int
    AF4_I2C1: int
    AF4_I2C2: int
    AF5_I2S2: int
    AF5_SPI1: int
    AF5_SPI2: int
    AF6_I2S2: int
    AF7_USART1: int
    AF7_USART2: int
    AF7_USART3: int
    AF8_UART4: int
    AF8_USART6: int
    AF9_CAN1: int
    AF9_CAN2: int
    AF9_TIM12: int
    AF9_TIM13: int
    AF9_TIM14: int
    AF_OD: int
    AF_PP: int
    ALT: int
    ALT_OPEN_DRAIN: int
    ANALOG: int
    IN: int
    IRQ_FALLING: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    OUT: int
    OUT_OD: int
    OUT_PP: int
    PULL_DOWN: int
    PULL_NONE: int
    PULL_UP: int
    def af(self, *args) -> Any: ...
    def af_list(self, *args) -> Any: ...
    class board:
        def __init__(self, *argv) -> None: ...
        LED_BLUE: Any
        LED_GREEN: Any
        LED_RED: Any
        LED_YELLOW: Any
        MMA_AVDD: Any
        MMA_INT: Any
        SD: Any
        SD_CK: Any
        SD_CMD: Any
        SD_D0: Any
        SD_D1: Any
        SD_D2: Any
        SD_D3: Any
        SD_SW: Any
        SW: Any
        USB_DM: Any
        USB_DP: Any
        USB_ID: Any
        USB_VBUS: Any
        X1: Any
        X10: Any
        X11: Any
        X12: Any
        X17: Any
        X18: Any
        X19: Any
        X2: Any
        X20: Any
        X21: Any
        X22: Any
        X3: Any
        X4: Any
        X5: Any
        X6: Any
        X7: Any
        X8: Any
        X9: Any
        Y1: Any
        Y10: Any
        Y11: Any
        Y12: Any
        Y2: Any
        Y3: Any
        Y4: Any
        Y5: Any
        Y6: Any
        Y7: Any
        Y8: Any
        Y9: Any
    class cpu:
        def __init__(self, *argv) -> None: ...
        A0: Any
        A1: Any
        A10: Any
        A11: Any
        A12: Any
        A13: Any
        A14: Any
        A15: Any
        A2: Any
        A3: Any
        A4: Any
        A5: Any
        A6: Any
        A7: Any
        A8: Any
        A9: Any
        B0: Any
        B1: Any
        B10: Any
        B11: Any
        B12: Any
        B13: Any
        B14: Any
        B15: Any
        B2: Any
        B3: Any
        B4: Any
        B5: Any
        B6: Any
        B7: Any
        B8: Any
        B9: Any
        C0: Any
        C1: Any
        C10: Any
        C11: Any
        C12: Any
        C13: Any
        C2: Any
        C3: Any
        C4: Any
        C5: Any
        C6: Any
        C7: Any
        C8: Any
        C9: Any
        D2: Any
    @classmethod
    def debug(cls, *args) -> Any: ...
    def gpio(self, *args) -> Any: ...
    def high(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def low(self, *args) -> Any: ...
    @classmethod
    def mapper(cls, *args) -> Any: ...
    def mode(self, *args) -> Any: ...
    def name(self, *args) -> Any: ...
    def names(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...
    def pin(self, *args) -> Any: ...
    def port(self, *args) -> Any: ...
    def pull(self, *args) -> Any: ...

SOFT_RESET: int

class SPI:
    def __init__(self, *argv) -> None: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    LSB: int
    MSB: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def write_readinto(self, *args) -> Any: ...

class Signal:
    def __init__(self, *argv) -> None: ...
    def value(self, *args) -> Any: ...
    def off(self, *args) -> Any: ...
    def on(self, *args) -> Any: ...

class SoftI2C:
    def __init__(self, *argv) -> None: ...
    def readinto(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def readfrom(self, *args) -> Any: ...
    def readfrom_into(self, *args) -> Any: ...
    def readfrom_mem(self, *args) -> Any: ...
    def readfrom_mem_into(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def writeto(self, *args) -> Any: ...
    def writeto_mem(self, *args) -> Any: ...
    def writevto(self, *args) -> Any: ...

class SoftSPI:
    def __init__(self, *argv) -> None: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    LSB: int
    MSB: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def write_readinto(self, *args) -> Any: ...

class Timer:
    def __init__(self, *argv) -> None: ...
    ONE_SHOT: int
    PERIODIC: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...

class UART:
    def __init__(self, *argv) -> None: ...
    def any(self, *args) -> Any: ...
    def read(self, *args) -> Any: ...
    def readinto(self, *args) -> Any: ...
    def readline(self, *args) -> Any: ...
    def write(self, *args) -> Any: ...
    CTS: int
    IRQ_RXIDLE: int
    RTS: int
    def deinit(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def readchar(self, *args) -> Any: ...
    def sendbreak(self, *args) -> Any: ...
    def writechar(self, *args) -> Any: ...

class WDT:
    def __init__(self, *argv) -> None: ...
    def feed(self, *args) -> Any: ...

WDT_RESET: int

def bitstream(*args) -> Any: ...
def bootloader(*args) -> Any: ...
def deepsleep(*args) -> Any: ...
def disable_irq(*args) -> Any: ...
def enable_irq(*args) -> Any: ...
def freq(*args) -> Any: ...
def idle(*args) -> Any: ...
def info(*args) -> Any: ...
def lightsleep(*args) -> Any: ...

mem16: Any
mem32: Any
mem8: Any

def reset(*args) -> Any: ...
def reset_cause(*args) -> Any: ...
def rng(*args) -> Any: ...
def sleep(*args) -> Any: ...
def soft_reset(*args) -> Any: ...
def time_pulse_us(*args) -> Any: ...
def unique_id(*args) -> Any: ...
