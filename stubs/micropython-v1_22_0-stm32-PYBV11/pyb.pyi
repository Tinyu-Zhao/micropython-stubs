from _typeshed import Incomplete as Incomplete

hid_mouse: tuple
hid_keyboard: tuple

def hard_reset(*args, **kwargs) -> Incomplete: ...
def have_cdc(*args, **kwargs) -> Incomplete: ...
def hid(*args, **kwargs) -> Incomplete: ...
def info(*args, **kwargs) -> Incomplete: ...
def wfi(*args, **kwargs) -> Incomplete: ...
def elapsed_micros(*args, **kwargs) -> Incomplete: ...
def freq(*args, **kwargs) -> Incomplete: ...
def disable_irq(*args, **kwargs) -> Incomplete: ...
def fault_debug(*args, **kwargs) -> Incomplete: ...
def elapsed_millis(*args, **kwargs) -> Incomplete: ...
def enable_irq(*args, **kwargs) -> Incomplete: ...
def sync(*args, **kwargs) -> Incomplete: ...
def servo(*args, **kwargs) -> Incomplete: ...
def standby(*args, **kwargs) -> Incomplete: ...
def usb_mode(*args, **kwargs) -> Incomplete: ...
def udelay(*args, **kwargs) -> Incomplete: ...
def unique_id(*args, **kwargs) -> Incomplete: ...
def micros(*args, **kwargs) -> Incomplete: ...
def mount(*args, **kwargs) -> Incomplete: ...
def rng(*args, **kwargs) -> Incomplete: ...
def millis(*args, **kwargs) -> Incomplete: ...
def repl_uart(*args, **kwargs) -> Incomplete: ...
def pwm(*args, **kwargs) -> Incomplete: ...
def repl_info(*args, **kwargs) -> Incomplete: ...
def stop(*args, **kwargs) -> Incomplete: ...
def delay(*args, **kwargs) -> Incomplete: ...
def main(*args, **kwargs) -> Incomplete: ...
def bootloader(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class DAC:
    CIRCULAR: int
    NORMAL: int
    def noise(self, *args, **kwargs) -> Incomplete: ...
    def write_timed(self, *args, **kwargs) -> Incomplete: ...
    def triangle(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ExtInt:
    IRQ_FALLING: int
    IRQ_RISING_FALLING: int
    IRQ_RISING: int
    EVT_FALLING: int
    EVT_RISING_FALLING: int
    EVT_RISING: int
    def line(self, *args, **kwargs) -> Incomplete: ...
    def regs(self, *args, **kwargs) -> Incomplete: ...
    def swint(self, *args, **kwargs) -> Incomplete: ...
    def enable(self, *args, **kwargs) -> Incomplete: ...
    def disable(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Flash:
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class I2C:
    PERIPHERAL: int
    MASTER: int
    CONTROLLER: int
    SLAVE: int
    def scan(self, *args, **kwargs) -> Incomplete: ...
    def mem_read(self, *args, **kwargs) -> Incomplete: ...
    def mem_write(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def is_ready(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class LCD:
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def light(self, *args, **kwargs) -> Incomplete: ...
    def pixel(self, *args, **kwargs) -> Incomplete: ...
    def show(self, *args, **kwargs) -> Incomplete: ...
    def text(self, *args, **kwargs) -> Incomplete: ...
    def contrast(self, *args, **kwargs) -> Incomplete: ...
    def get(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def command(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class CAN:
    MASK16: int
    MASK32: int
    LOOPBACK: int
    LIST32: int
    SILENT_LOOPBACK: int
    NORMAL: int
    SILENT: int
    STOPPED: int
    ERROR_ACTIVE: int
    BUS_OFF: int
    LIST16: int
    ERROR_PASSIVE: int
    ERROR_WARNING: int
    def restart(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def rxcallback(self, *args, **kwargs) -> Incomplete: ...
    def setfilter(self, *args, **kwargs) -> Incomplete: ...
    def state(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def clearfilter(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADC:
    def read_timed(self, *args, **kwargs) -> Incomplete: ...
    def read_timed_multi(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ADCAll:
    def read_core_vbat(self, *args, **kwargs) -> Incomplete: ...
    def read_core_vref(self, *args, **kwargs) -> Incomplete: ...
    def read_vref(self, *args, **kwargs) -> Incomplete: ...
    def read_core_temp(self, *args, **kwargs) -> Incomplete: ...
    def read_channel(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Accel:
    def x(self, *args, **kwargs) -> Incomplete: ...
    def tilt(self, *args, **kwargs) -> Incomplete: ...
    def y(self, *args, **kwargs) -> Incomplete: ...
    def z(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def filtered_xyz(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class USB_VCP:
    RTS: int
    CTS: int
    IRQ_RX: int
    def readlines(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def setinterrupt(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Timer:
    OC_FORCED_ACTIVE: int
    OC_FORCED_INACTIVE: int
    OC_INACTIVE: int
    OC_ACTIVE: int
    LOW: int
    IC: int
    PWM_INVERTED: int
    RISING: int
    OC_TIMING: int
    PWM: int
    OC_TOGGLE: int
    UP: int
    BRK_LOW: int
    BRK_OFF: int
    CENTER: int
    BRK_HIGH: int
    BOTH: int
    HIGH: int
    ENC_B: int
    FALLING: int
    DOWN: int
    ENC_AB: int
    ENC_A: int
    def freq(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def period(self, *args, **kwargs) -> Incomplete: ...
    def prescaler(self, *args, **kwargs) -> Incomplete: ...
    def source_freq(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def callback(self, *args, **kwargs) -> Incomplete: ...
    def channel(self, *args, **kwargs) -> Incomplete: ...
    def counter(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Switch:
    def callback(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Servo:
    def speed(self, *args, **kwargs) -> Incomplete: ...
    def pulse_width(self, *args, **kwargs) -> Incomplete: ...
    def calibration(self, *args, **kwargs) -> Incomplete: ...
    def angle(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class UART:
    IRQ_RXIDLE: int
    CTS: int
    RTS: int
    def init(self, *args, **kwargs) -> Incomplete: ...
    def flush(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def txdone(self, *args, **kwargs) -> Incomplete: ...
    def sendbreak(self, *args, **kwargs) -> Incomplete: ...
    def readchar(self, *args, **kwargs) -> Incomplete: ...
    def writechar(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class USB_HID:
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class LED:
    def toggle(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def intensity(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RTC:
    def info(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def wakeup(self, *args, **kwargs) -> Incomplete: ...
    def datetime(self, *args, **kwargs) -> Incomplete: ...
    def calibration(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Pin:
    AF_OD: int
    AF9_TIM14: int
    ALT_OPEN_DRAIN: int
    AF_PP: int
    ALT: int
    AF9_CAN1: int
    AF8_USART6: int
    AF9_TIM13: int
    AF9_CAN2: int
    AF9_TIM12: int
    PULL_UP: int
    OUT_PP: int
    OUT_OD: int
    ANALOG: int
    PULL_DOWN: int
    PULL_NONE: int
    IRQ_FALLING: int
    IN: int
    OUT: int
    IRQ_RISING: int
    OPEN_DRAIN: int
    AF2_TIM5: int
    AF3_TIM10: int
    AF3_TIM11: int
    AF3_TIM8: int
    AF3_TIM9: int
    AF2_TIM4: int
    AF1_TIM1: int
    AF1_TIM2: int
    AF2_TIM3: int
    AF8_UART4: int
    AF6_I2S2: int
    AF7_USART1: int
    AF7_USART2: int
    AF7_USART3: int
    AF4_I2C1: int
    AF5_SPI2: int
    AF4_I2C2: int
    AF5_I2S2: int
    AF5_SPI1: int
    def mode(self, *args, **kwargs) -> Incomplete: ...
    def name(self, *args, **kwargs) -> Incomplete: ...
    def pull(self, *args, **kwargs) -> Incomplete: ...
    def low(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def pin(self, *args, **kwargs) -> Incomplete: ...
    def port(self, *args, **kwargs) -> Incomplete: ...
    def names(self, *args, **kwargs) -> Incomplete: ...
    def on(self, *args, **kwargs) -> Incomplete: ...
    def off(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def af_list(self, *args, **kwargs) -> Incomplete: ...
    def af(self, *args, **kwargs) -> Incomplete: ...
    def value(self, *args, **kwargs) -> Incomplete: ...
    def high(self, *args, **kwargs) -> Incomplete: ...
    def gpio(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def dict(cls, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def debug(cls, *args, **kwargs) -> Incomplete: ...

    class cpu:
        B9: Incomplete
        B8: Incomplete
        B7: Incomplete
        C0: Incomplete
        C1: Incomplete
        C10: Incomplete
        B3: Incomplete
        B2: Incomplete
        B6: Incomplete
        B4: Incomplete
        B5: Incomplete
        B15: Incomplete
        C7: Incomplete
        C6: Incomplete
        C5: Incomplete
        C8: Incomplete
        C9: Incomplete
        C11: Incomplete
        C13: Incomplete
        C12: Incomplete
        C4: Incomplete
        C2: Incomplete
        C3: Incomplete
        D2: Incomplete
        A15: Incomplete
        A14: Incomplete
        A13: Incomplete
        A2: Incomplete
        A3: Incomplete
        A4: Incomplete
        A1: Incomplete
        A0: Incomplete
        A12: Incomplete
        A10: Incomplete
        A11: Incomplete
        B14: Incomplete
        B11: Incomplete
        B10: Incomplete
        B1: Incomplete
        B12: Incomplete
        B13: Incomplete
        A5: Incomplete
        A7: Incomplete
        A6: Incomplete
        B0: Incomplete
        A8: Incomplete
        A9: Incomplete
        def __init__(self, *argv, **kwargs) -> None: ...

    @classmethod
    def mapper(cls, *args, **kwargs) -> Incomplete: ...

    class board:
        X5: Incomplete
        X18: Incomplete
        X4: Incomplete
        X8: Incomplete
        X6: Incomplete
        X7: Incomplete
        X2: Incomplete
        X3: Incomplete
        X19: Incomplete
        X22: Incomplete
        X20: Incomplete
        X21: Incomplete
        Y5: Incomplete
        X9: Incomplete
        Y4: Incomplete
        Y8: Incomplete
        Y6: Incomplete
        Y7: Incomplete
        Y10: Incomplete
        Y3: Incomplete
        Y1: Incomplete
        Y2: Incomplete
        Y11: Incomplete
        Y12: Incomplete
        Y9: Incomplete
        SD_CK: Incomplete
        X17: Incomplete
        SD: Incomplete
        SD_D1: Incomplete
        SD_CMD: Incomplete
        SD_D0: Incomplete
        LED_GREEN: Incomplete
        MMA_INT: Incomplete
        LED_BLUE: Incomplete
        MMA_AVDD: Incomplete
        LED_RED: Incomplete
        LED_YELLOW: Incomplete
        X1: Incomplete
        SD_D2: Incomplete
        USB_VBUS: Incomplete
        X12: Incomplete
        X10: Incomplete
        X11: Incomplete
        SD_SW: Incomplete
        USB_ID: Incomplete
        SD_D3: Incomplete
        USB_DP: Incomplete
        SW: Incomplete
        USB_DM: Incomplete
        def __init__(self, *argv, **kwargs) -> None: ...

    def __init__(self, *argv, **kwargs) -> None: ...

class SPI:
    MASTER: int
    LSB: int
    SLAVE: int
    MSB: int
    PERIPHERAL: int
    CONTROLLER: int
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def send_recv(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def init(self, *args, **kwargs) -> Incomplete: ...
    def write_readinto(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

SD: Incomplete

class SDCard:
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def power(self, *args, **kwargs) -> Incomplete: ...
    def present(self, *args, **kwargs) -> Incomplete: ...
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
