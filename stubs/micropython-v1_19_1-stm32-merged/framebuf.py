"""
Module: 'framebuf' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Optional, Any
from _typeshed import Incomplete as Incomplete

MONO_HMSB = 4  # type: int
MONO_HLSB = 3  # type: int
RGB565 = 1  # type: int
MONO_VLSB = 0  # type: int
MVLSB = 0  # type: int
GS2_HMSB = 5  # type: int
GS8 = 6  # type: int
GS4_HMSB = 2  # type: int


def FrameBuffer1(*args, **kwargs) -> Any:
    ...


class FrameBuffer:
    """
    Construct a FrameBuffer object.  The parameters are:

        - *buffer* is an object with a buffer protocol which must be large
          enough to contain every pixel defined by the width, height and
          format of the FrameBuffer.
        - *width* is the width of the FrameBuffer in pixels
        - *height* is the height of the FrameBuffer in pixels
        - *format* specifies the type of pixel used in the FrameBuffer;
          permissible values are listed under Constants below. These set the
          number of bits used to encode a color value and the layout of these
          bits in *buffer*.
          Where a color value c is passed to a method, c is a small integer
          with an encoding that is dependent on the format of the FrameBuffer.
        - *stride* is the number of pixels between each horizontal line
          of pixels in the FrameBuffer. This defaults to *width* but may
          need adjustments when implementing a FrameBuffer within another
          larger FrameBuffer or screen. The *buffer* size must accommodate
          an increased step size.

    One must specify valid *buffer*, *width*, *height*, *format* and
    optionally *stride*.  Invalid *buffer* size or dimensions may lead to
    unexpected errors.
    """

    def rect(self, x, y, w, h, c) -> Incomplete:
        ...

    def pixel(self, x, y, c: Optional[Any] = ...) -> Incomplete:
        """
        If *c* is not given, get the color value of the specified pixel.
        If *c* is given, set the specified pixel to the given color.
        """
        ...

    def vline(self, x, y, h, c) -> Incomplete:
        ...

    def scroll(self, xstep, ystep) -> Incomplete:
        """
        Shift the contents of the FrameBuffer by the given vector. This may
        leave a footprint of the previous colors in the FrameBuffer.
        """
        ...

    def text(self, s, x, y, c: Optional[Any] = ...) -> None:
        """
        Write text to the FrameBuffer using the the coordinates as the upper-left
        corner of the text. The color of the text can be defined by the optional
        argument but is otherwise a default value of 1. All characters have
        dimensions of 8x8 pixels and there is currently no way to change the font.
        """
        ...

    def fill(self, c) -> None:
        """
        Fill the entire FrameBuffer with the specified color.
        """
        ...

    def blit(self, fbuf, x, y, key: int = ..., palette: Incomplete | None = ...) -> None:
        """
        Draw another FrameBuffer on top of the current one at the given coordinates.
        If *key* is specified then it should be a color integer and the
        corresponding color will be considered transparent: all pixels with that
        color value will not be drawn.

        The *palette* argument enables blitting between FrameBuffers with differing
        formats. Typical usage is to render a monochrome or grayscale glyph/icon to
        a color display. The *palette* is a FrameBuffer instance whose format is
        that of the current FrameBuffer. The *palette* height is one pixel and its
        pixel width is the number of colors in the source FrameBuffer. The *palette*
        for an N-bit source needs 2**N pixels; the *palette* for a monochrome source
        would have 2 pixels representing background and foreground colors. The
        application assigns a color to each pixel in the *palette*. The color of the
        current pixel will be that of that *palette* pixel whose x position is the
        color of the corresponding source pixel.
        """
        ...

    def line(self, x1, y1, x2, y2, c) -> None:
        """
        Draw a line from a set of coordinates using the given color and
        a thickness of 1 pixel. The `line` method draws the line up to
        a second set of coordinates whereas the `hline` and `vline`
        methods draw horizontal and vertical lines respectively up to
        a given length.
        """
        ...

    def fill_rect(self, x, y, w, h, c) -> None:
        """
        Draw a rectangle at the given location, size and color. The `rect`
        method draws only a 1 pixel outline whereas the `fill_rect` method
        draws both the outline and interior.
        """
        ...

    def hline(self, x, y, w, c) -> Incomplete:
        ...

    def __init__(self, buffer, width, height, format, stride: int = ...) -> None:
        ...
