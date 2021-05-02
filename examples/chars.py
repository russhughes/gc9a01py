"""
chars.py

    Pages through all characters of four fonts on the display.

"""
import utime
from machine import Pin, SPI
import gc9a01py as gc9a01

# Choose a few fonts

# from fonts import vga1_8x8 as font
from fonts import vga2_8x8 as font1
# from fonts import vga1_8x16 as font
from fonts import vga2_8x16 as font2
# from fonts import vga1_16x16 as font
# from fonts import vga1_bold_16x16 as font
# from fonts import vga2_16x16 as font
from fonts import vga2_bold_16x16 as font3
# from fonts import vga1_16x32 as font
# from fonts import vga1_bold_16x32 as font
# from fonts import vga2_16x32 as font
from fonts import vga2_bold_16x32 as font4


def main():
    spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(21, Pin.OUT),
        cs=Pin(13, Pin.OUT),
        reset=Pin(26, Pin.OUT),
        backlight=Pin(14, Pin.OUT),
        rotation=0)

    while True:
        for font in (font1, font2, font3, font4):
            tft.fill(gc9a01.BLUE)
            line = 0
            col = 0

            for char in range(font.FIRST, font.LAST):
                tft.text(font, chr(char), col, line, gc9a01.WHITE, gc9a01.BLUE)
                col += font.WIDTH
                if col > tft.width - font.WIDTH:
                    col = 0
                    line += font.HEIGHT

                    if line > tft.height-font.HEIGHT:
                        utime.sleep(3)
                        tft.fill(gc9a01.BLUE)
                        line = 0
                        col = 0

            utime.sleep(3)


main()
