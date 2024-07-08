"""
Module: 'lwip' on micropython-v1.23.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.23.0', 'cpu': 'ESP8266'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

SOCK_STREAM: int = 1
SOCK_DGRAM: int = 2
SOCK_RAW: int = 3
SO_REUSEADDR: int = 4
SOL_SOCKET: int = 1
SO_BROADCAST: int = 32
TCP_NODELAY: int = 64
AF_INET6: int = 10
IP_DROP_MEMBERSHIP: int = 1025
AF_INET: int = 2
IP_ADD_MEMBERSHIP: int = 1024
IPPROTO_IP: int = 0
IPPROTO_TCP: int = 6

def reset(*args, **kwargs) -> Incomplete: ...
def print_pcbs(*args, **kwargs) -> Incomplete: ...
def getaddrinfo(*args, **kwargs) -> Incomplete: ...
def callback(*args, **kwargs) -> Incomplete: ...

class socket:
    def recvfrom(self, *args, **kwargs) -> Incomplete: ...
    def recv(self, *args, **kwargs) -> Incomplete: ...
    def makefile(self, *args, **kwargs) -> Incomplete: ...
    def listen(self, *args, **kwargs) -> Incomplete: ...
    def settimeout(self, *args, **kwargs) -> Incomplete: ...
    def sendall(self, *args, **kwargs) -> Incomplete: ...
    def setsockopt(self, *args, **kwargs) -> Incomplete: ...
    def setblocking(self, *args, **kwargs) -> Incomplete: ...
    def sendto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def send(self, *args, **kwargs) -> Incomplete: ...
    def bind(self, *args, **kwargs) -> Incomplete: ...
    def accept(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
