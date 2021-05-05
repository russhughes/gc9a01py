"""
chango.py

    Test for font2bitmap converter for the GC9A01 display.
    See the font2bitmap program in the utils directory.
"""

from machine import Pin, SPI
import gc9a01py

from truetype import chango_16 as font_16
from truetype import chango_32 as font_32
from truetype import chango_64 as font_64


def main():
    # enable display and clear screen
    spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
    tft = gc9a01py.GC9A01(
        spi,
        dc=Pin(21, Pin.OUT),
        cs=Pin(13, Pin.OUT),
        reset=Pin(26, Pin.OUT),
        backlight=Pin(14, Pin.OUT),
        rotation=0)

    tft.fill(gc9a01py.BLACK)

    row = 0
    tft.write(font_16, "abcdefghijklmnopqrstuvwxyz", 0, row)
    row += font_16.HEIGHT

    tft.write(font_32, "abcdefghijklm", 0, row)
    row += font_32.HEIGHT

    tft.write(font_32, "nopqrstuvwxy", 0, row)
    row += font_32.HEIGHT

    tft.write(font_64, "abcdef", 0, row)
    row += font_64.HEIGHT

    tft.write(font_64, "ghijkl", 0, row)
    row += font_64.HEIGHT


main()
