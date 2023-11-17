"""
Module: 'ssl' on micropython-v1.20.0-esp32-GENERIC_S3
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import IO, Any
from _typeshed import Incomplete as Incomplete
from stdlib.ssl import *

CERT_OPTIONAL = 1  # type: int
CERT_REQUIRED = 2  # type: int
CERT_NONE = 0  # type: int


def wrap_socket(
    sock,
    server_side: bool = ...,
    keyfile: Incomplete | None = ...,
    certfile: Incomplete | None = ...,
    cert_reqs: Incomplete | None = ...,
    cadata: Incomplete | None = ...,
    server_hostname: Incomplete | None = ...,
    do_handshake: bool = ...,
) -> IO:
    """
    Takes a `stream` *sock* (usually socket.socket instance of ``SOCK_STREAM`` type),
    and returns an instance of ssl.SSLSocket, which wraps the underlying stream in
    an SSL context. Returned object has the usual `stream` interface methods like
    ``read()``, ``write()``, etc.
    A server-side SSL socket should be created from a normal socket returned from
    :meth:`~socket.socket.accept()` on a non-SSL listening server socket.

    - *do_handshake* determines whether the handshake is done as part of the ``wrap_socket``
      or whether it is deferred to be done as part of the initial reads or writes
      (there is no ``do_handshake`` method as in CPython).
      For blocking sockets doing the handshake immediately is standard. For non-blocking
      sockets (i.e. when the *sock* passed into ``wrap_socket`` is in non-blocking mode)
      the handshake should generally be deferred because otherwise ``wrap_socket`` blocks
      until it completes. Note that in AXTLS the handshake can be deferred until the first
      read or write but it then blocks until completion.

    - *cert_reqs* determines whether the peer (server or client) must present a valid certificate.
      Note that for mbedtls based ports, ``ssl.CERT_NONE`` and ``ssl.CERT_OPTIONAL`` will not
      validate any certificate, only ``ssl.CERT_REQUIRED`` will.

    - *cadata* is a bytes object containing the CA certificate chain (in DER format) that will
      validate the peer's certificate.  Currently only a single DER-encoded certificate is supported.

    - *server_hostname* is for use as a client, and sets the hostname to check against the received
      server certificate.  It also sets the name for Server Name Indication (SNI), allowing the server
      to present the proper certificate.

    Depending on the underlying module implementation in a particular
    :term:`MicroPython port`, some or all keyword arguments above may be not supported.
    """
    ...
