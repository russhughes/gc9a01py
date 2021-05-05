"""
noto_fonts Writes the names of three Noto fonts centered on the display
    using the font. The fonts were converted from True Type fonts using
    the font2bitmap utility.
"""

from machine import SPI, Pin
import gc9a01py as gc9a01

from truetype import NotoSans_32 as noto_sans
from truetype import NotoSerif_32 as noto_serif
from truetype import NotoSansMono_32 as noto_mono


def main():

    def center(font, string, row, color=gc9a01.WHITE):
        screen = tft.width                        # get screen width
        width = tft.write_width(font, string)     # get the width of the string
        if width and width < screen:              # if the string < display
            col = tft.width // 2 - width // 2     # find the column to center
        else:                                     # otherwise
            col = 0                               # left justify

        tft.write(font, string, col, row, color)  # and write the string

    try:
        spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
        tft = gc9a01.GC9A01(
            spi,
            dc=Pin(21, Pin.OUT),
            cs=Pin(13, Pin.OUT),
            reset=Pin(26, Pin.OUT),
            backlight=Pin(14, Pin.OUT),
            rotation=0)

        # enable display and clear screen
        tft.fill(gc9a01.BLACK)

        # center the name of the first font, using the font
        row = 64
        center(noto_sans, "NotoSans", row, gc9a01.RED)
        row += noto_sans.HEIGHT

        # center the name of the second font, using the font
        center(noto_serif, "NotoSerif", row, gc9a01.GREEN)
        row += noto_serif.HEIGHT

        # center the name of the third font, using the font
        center(noto_mono, "NotoSansMono", row, gc9a01.BLUE)
        row += noto_mono.HEIGHT

    finally:
        # shutdown spi
        if 'spi' in locals():
            spi.deinit()


main()
