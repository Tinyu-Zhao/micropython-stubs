
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Btn:
    def attach() -> None: ...
    def deinit() -> None: ...
    def detach() -> None: ...
    def multiBtnCb() -> None: ...
    def restart() -> None: ...
    def timerCb() -> None: ...
class BtnChild:
    def deinit() -> None: ...
    def isPressed() -> None: ...
    def isReleased() -> None: ...
    def pressFor() -> None: ...
    def restart() -> None: ...
    def upDate() -> None: ...
    def wasDoublePress() -> None: ...
    def wasPressed() -> None: ...
    def wasReleased() -> None: ...
class I2S:
    def adc_enable() -> None: ...
    def bits() -> None: ...
    def deinit() -> None: ...
    def init() -> None: ...
    def nchannels() -> None: ...
    def read() -> None: ...
    def sample_rate() -> None: ...
    def set_adc_pin() -> None: ...
    def set_dac_mode() -> None: ...
    def set_pin() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def volume() -> None: ...
    def write() -> None: ...
class IP5306:
    def getBatteryLevel() -> None: ...
    def init() -> None: ...
    def isChargeFull() -> None: ...
    def isCharging() -> None: ...
    def setCharge() -> None: ...
    def setChargeVolt() -> None: ...
    def setVinMaxCurrent() -> None: ...
class Rgb_multi:
    def deinit() -> None: ...
    def setBrightness() -> None: ...
    def setColor() -> None: ...
    def setColorAll() -> None: ...
    def setColorFrom() -> None: ...
    def setShowLock() -> None: ...
    def show() -> None: ...
class Speaker:
    def _timeout_cb() -> None: ...
    def checkInit() -> None: ...
    def setBeat() -> None: ...
    def setVolume() -> None: ...
    def sing() -> None: ...
    def tone() -> None: ...
def btnText() -> None: ...
def const() -> None: ...
def get_sd_state() -> None: ...
def hwDeinit() -> None: ...
def sd_mount() -> None: ...
def sd_umount() -> None: ...
