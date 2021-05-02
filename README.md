gc9a01py.py
===========

This is a fork of devbis' st7789py_mpy module from
https://github.com/devbis/st7789py_mpy modified to drive 240x240 pixel GC9A01
displays.

The driver supports display rotation, mirroring, scrolling drawing text using 8
and 16 bit wide bitmap fonts with heights that are multiples of 8. Included are
12 bitmap fonts derived from classic pc text mode fonts and several example
programs.

Utilities to convert bitmaps fonts and images to bitmap modules are included in
the utils directory. Documentation can be found in the docs directory.

If you are looking for a faster driver with additional features, check out the
C version of the driver at https://github.com/russhughes/gc9a01_mpy

This is a work in progress.
