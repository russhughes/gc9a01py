"""
scroll.py

    Smoothly(ish) scrolls all font characters up the screen on the display.
    Only works with fonts with heights that are even multiples of the screen
    height, (i.e. 8 or 16 pixels high)

"""
import utime
from machine import Pin, SPI
import gc9a01py as gc9a01

# choose a font

# import vga1_8x8 as font
# import vga2_8x8 as font
# import vga1_8x16 as font
# import vga2_8x16 as font
# import vga1_16x16 as font
# import vga1_bold_16x16 as font
# import vga2_16x16 as font
from fonts import vga2_bold_16x16 as font


def main():
    spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(21, Pin.OUT),
        cs=Pin(13, Pin.OUT),
        reset=Pin(26, Pin.OUT),
        backlight=Pin(14, Pin.OUT),
        rotation=0)

    last_line = tft.height - font.HEIGHT
    tfa = 0
    tfb = 0
    tft.vscrdef(tfa, 240, tfb)

    tft.fill(gc9a01.BLUE)
    scroll = 0
    character = 0
    while True:
        tft.fill_rect(0, scroll, tft.width, 1, gc9a01.BLUE)

        if scroll % font.HEIGHT == 0:
            tft.text(
                font,
                'x{:02x} = {:s}'.format(character, chr(character)),
                64,
                (scroll + last_line) % tft.height,
                gc9a01.WHITE,
                gc9a01.BLUE)

            character = character + 1 if character < 256 else 0

        tft.vscsad(scroll+tfa)
        scroll += 1

        if scroll == tft.height:
            scroll = 0

        utime.sleep(0.01)


main()
