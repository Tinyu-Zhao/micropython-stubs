"""
Module: 'datetime' on micropython-v1.24.1-webassembly
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

_DBM: tuple = ()
_TIME_SPEC: tuple = ()
_DIM: tuple = ()
MINYEAR: Final[int] = 1
MAXYEAR: Final[int] = 9999

def _iso2t(*args, **kwargs) -> Incomplete: ...
def _time(*args, **kwargs) -> Incomplete: ...
def _iso2d(*args, **kwargs) -> Incomplete: ...
def _t2iso(*args, **kwargs) -> Incomplete: ...
def _leap(*args, **kwargs) -> Incomplete: ...
def _o2ymd(*args, **kwargs) -> Incomplete: ...
def _d2iso(*args, **kwargs) -> Incomplete: ...
def _dim(*args, **kwargs) -> Incomplete: ...
def _ymd2o(*args, **kwargs) -> Incomplete: ...
def _dby(*args, **kwargs) -> Incomplete: ...
def _date(*args, **kwargs) -> Incomplete: ...
def _dbm(*args, **kwargs) -> Incomplete: ...

class datetime:
    def date(self, *args, **kwargs) -> Incomplete: ...
    def isoweekday(self, *args, **kwargs) -> Incomplete: ...
    def dst(self, *args, **kwargs) -> Incomplete: ...
    def tzname(self, *args, **kwargs) -> Incomplete: ...
    def toordinal(self, *args, **kwargs) -> Incomplete: ...
    def timestamp(self, *args, **kwargs) -> Incomplete: ...
    def timetuple(self, *args, **kwargs) -> Incomplete: ...
    def timetz(self, *args, **kwargs) -> Incomplete: ...
    def isoformat(self, *args, **kwargs) -> Incomplete: ...
    def utcoffset(self, *args, **kwargs) -> Incomplete: ...
    def time(self, *args, **kwargs) -> Incomplete: ...
    def tuple(self, *args, **kwargs) -> Incomplete: ...
    def replace(self, *args, **kwargs) -> Incomplete: ...
    def weekday(self, *args, **kwargs) -> Incomplete: ...
    def astimezone(self, *args, **kwargs) -> Incomplete: ...
    def _sub(self, *args, **kwargs) -> Incomplete: ...
    def _cmp(self, *args, **kwargs) -> Incomplete: ...

    year: Incomplete  ## <class 'property'> = <property>
    @classmethod
    def now(cls, *args, **kwargs) -> Incomplete: ...

    second: Incomplete  ## <class 'property'> = <property>
    tzinfo: Incomplete  ## <class 'property'> = <property>
    day: Incomplete  ## <class 'property'> = <property>
    fold: Incomplete  ## <class 'property'> = <property>
    @classmethod
    def fromisoformat(cls, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def combine(cls, *args, **kwargs) -> Incomplete: ...

    EPOCH: Incomplete  ## <class 'datetime'> = datetime.datetime(1970, 1, 1, 0, 0, 0, 0, datetime.timezone(datetime.timedelta(microseconds=0), None), fold=0)
    month: Incomplete  ## <class 'property'> = <property>
    microsecond: Incomplete  ## <class 'property'> = <property>
    minute: Incomplete  ## <class 'property'> = <property>
    @classmethod
    def fromordinal(cls, *args, **kwargs) -> Incomplete: ...

    hour: Incomplete  ## <class 'property'> = <property>
    @classmethod
    def fromtimestamp(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class timedelta:
    def _tuple(self, *args, **kwargs) -> Incomplete: ...
    def _format(self, *args, **kwargs) -> Incomplete: ...
    def isoformat(self, *args, **kwargs) -> Incomplete: ...
    def total_seconds(self, *args, **kwargs) -> Incomplete: ...
    def tuple(self, *args, **kwargs) -> Incomplete: ...

    min: Incomplete  ## <class 'timedelta'> = datetime.timedelta(microseconds=-86399999913600000000)
    resolution: Incomplete  ## <class 'timedelta'> = datetime.timedelta(microseconds=1)
    seconds: Incomplete  ## <class 'property'> = <property>
    max: Incomplete  ## <class 'timedelta'> = datetime.timedelta(microseconds=86399999999999999999)
    microseconds: Incomplete  ## <class 'property'> = <property>
    days: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...

class timezone:
    def isoformat(self, *args, **kwargs) -> Incomplete: ...
    def tzname(self, *args, **kwargs) -> Incomplete: ...
    def utcoffset(self, *args, **kwargs) -> Incomplete: ...
    def fromutc(self, *args, **kwargs) -> Incomplete: ...
    def dst(self, *args, **kwargs) -> Incomplete: ...

    utc: Incomplete  ## <class 'timezone'> = datetime.timezone(datetime.timedelta(microseconds=0), None)
    def __init__(self, *argv, **kwargs) -> None: ...

class tzinfo:
    def isoformat(self, *args, **kwargs) -> Incomplete: ...
    def tzname(self, *args, **kwargs) -> Incomplete: ...
    def utcoffset(self, *args, **kwargs) -> Incomplete: ...
    def fromutc(self, *args, **kwargs) -> Incomplete: ...
    def dst(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class time:
    def _sub(self, *args, **kwargs) -> Incomplete: ...
    def dst(self, *args, **kwargs) -> Incomplete: ...
    def isoformat(self, *args, **kwargs) -> Incomplete: ...
    def tzname(self, *args, **kwargs) -> Incomplete: ...
    def utcoffset(self, *args, **kwargs) -> Incomplete: ...
    def tuple(self, *args, **kwargs) -> Incomplete: ...
    def replace(self, *args, **kwargs) -> Incomplete: ...

    resolution: Incomplete  ## <class 'timedelta'> = datetime.timedelta(microseconds=1)
    minute: Incomplete  ## <class 'property'> = <property>
    second: Incomplete  ## <class 'property'> = <property>
    tzinfo: Incomplete  ## <class 'property'> = <property>
    min: Incomplete  ## <class 'time'> = datetime.time(microsecond=0, tzinfo=None, fold=0)
    fold: Incomplete  ## <class 'property'> = <property>
    max: Incomplete  ## <class 'time'> = datetime.time(microsecond=86399999999, tzinfo=None, fold=0)
    microsecond: Incomplete  ## <class 'property'> = <property>
    @classmethod
    def fromisoformat(cls, *args, **kwargs) -> Incomplete: ...

    hour: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...

class date:
    def timetuple(self, *args, **kwargs) -> Incomplete: ...
    def toordinal(self, *args, **kwargs) -> Incomplete: ...
    def isoformat(self, *args, **kwargs) -> Incomplete: ...
    def isoweekday(self, *args, **kwargs) -> Incomplete: ...
    def weekday(self, *args, **kwargs) -> Incomplete: ...
    def replace(self, *args, **kwargs) -> Incomplete: ...
    def tuple(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def today(cls, *args, **kwargs) -> Incomplete: ...

    resolution: Incomplete  ## <class 'timedelta'> = datetime.timedelta(microseconds=86400000000)
    month: Incomplete  ## <class 'property'> = <property>
    year: Incomplete  ## <class 'property'> = <property>
    min: Incomplete  ## <class 'date'> = datetime.date(0, 0, 1)
    @classmethod
    def fromtimestamp(cls, *args, **kwargs) -> Incomplete: ...

    max: Incomplete  ## <class 'date'> = datetime.date(0, 0, 3652059)
    @classmethod
    def fromordinal(cls, *args, **kwargs) -> Incomplete: ...

    day: Incomplete  ## <class 'property'> = <property>
    @classmethod
    def fromisoformat(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
