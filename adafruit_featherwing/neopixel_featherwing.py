# The MIT License (MIT)
#
# Copyright (c) 2019 Melissa LeBlanc-Williams for Adafruit Industries LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_featherwing.neopixel_featherwing`
====================================================

Helper for using the `NeoPixel FeatherWing <https://www.adafruit.com/product/2945>`_.

* Author(s): Melissa LeBlanc-Williams
"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_FeatherWing.git"

import board
import neopixel
from adafruit_featherwing.dotstar_featherwing import DotStarFeatherWing

class NeoPixelFeatherWing(DotStarFeatherWing):
    """Class representing a `NeoPixel FeatherWing
       <https://www.adafruit.com/product/2945>`_.

       The feather uses pins D6 by default"""
    #pylint: disable-msg=super-init-not-called
    def __init__(self, pixel_pin=board.D6, brightness=0.1):
        """
            :param pin pixel_pin: The pin for the featherwing
            :param float brightness: Optional brightness (0.0-1.0) that defaults to 1.0
        """
        self.rows = 4
        self.columns = 8
        self._auto_write = True
        self._display = neopixel.NeoPixel(pixel_pin, self.rows * self.columns,
                                          brightness=brightness, auto_write=False,
                                          pixel_order=neopixel.GRB)
    #pylint: enable-msg=super-init-not-called

    #pylint: disable-msg=useless-super-delegation
    def fill(self, color=0):
        """
        Fills all of the NeoPixels with a color or unlit if empty.

        :param color: (Optional) The text or number to display (default=0)
        :type color: list/tuple or int

        This example shows various ways of using the fill() function

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()
            neopixel.fill((255, 255, 255)) # Fill White
            time.sleep(1)
            neopixel.fill(0xFF0000) # Fill Red
            time.sleep(1)
            neopixel.fill() # Clear all lit NeoPixels

        """
        super().fill(color)

    def show(self):
        """
        Update the NeoPixels. This is only needed if auto_write is set to False
        This can be very useful for more advanced graphics effects.

        This example changes the blink rate and prints out the current setting

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()
            neopixel.fill() # Clear any lit NeoPixels
            neopixel.auto_write = False
            neopixel[0, 0] = (255, 255, 255) # Set White
            time.sleep(1)
            neopixel.show() # Update the NeoPixels

        """
        super().show()

    def shift_right(self, rotate=False):
        """
        Shift all pixels left

        :param rotate: (Optional) Rotate the shifted pixels to the left side (default=False)

        This example shifts 2 pixels to the right

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()

            # Draw Red and Green Pixels
            neopixel[4, 1] = (255, 0, 0)
            neopixel[5, 1] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, neopixel.columns - 1):
                neopixel.shift_right(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, neopixel.columns - 1):
                neopixel.shift_right()
                time.sleep(.1)

        """
        super().shift_right(rotate)

    def shift_left(self, rotate=False):
        """
        Shift all pixels left

        :param rotate: (Optional) Rotate the shifted pixels to the right side (default=False)

        This example shifts 2 pixels to the left

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()

            # Draw Red and Green Pixels
            neopixel[4, 1] = (255, 0, 0)
            neopixel[5, 1] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, neopixel.columns - 1):
                neopixel.shift_left(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, neopixel.columns - 1):
                neopixel.shift_left()
                time.sleep(.1)

        """
        super().shift_left(rotate)
    #pylint: enable-msg=useless-super-delegation

    def shift_up(self, rotate=False):
        """
        Shift all pixels up

        :param rotate: (Optional) Rotate the shifted pixels to bottom (default=False)

        This example shifts 2 pixels up

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()

            # Draw Red and Green Pixels
            neopixel[4, 1] = (255, 0, 0)
            neopixel[5, 1] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_up(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_up()
                time.sleep(.1)

        """
        super().shift_down(rotate) # Up and down are reversed

    def shift_down(self, rotate=False):
        """
        Shift all pixels down.

        :param rotate: (Optional) Rotate the shifted pixels to top (default=False)

        This example shifts 2 pixels down

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()

            # Draw Red and Green Pixels
            neopixel[4, 1] = (255, 0, 0)
            neopixel[5, 1] = (0, 255, 0)

            # Rotate it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_down(True)
                time.sleep(.1)

            time.sleep(1)
            # Shift it off the screen
            for i in range(0, neopixel.rows - 1):
                neopixel.shift_down()
                time.sleep(.1)

        """
        super().shift_up(rotate) # Up and down are reversed

    @property
    def auto_write(self):
        """
        Whether or not we are automatically updating
        If set to false, be sure to call show() to update

        This lights NeoPixels with and without auto_write

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()
            neopixel.fill() # Clear any lit NeoPixels
            neopixel[0, 0] = (255, 255, 255) # Set White
            time.sleep(1)

            neopixel.auto_write = False
            neopixel[1, 0] = (255, 255, 255) # Set White
            time.sleep(1)
            neopixel.show() # Update the NeoPixels

        """
        return super().auto_write

    @property
    def brightness(self):
        """
        Overall brightness of the display

        This example changes the brightness

        .. code-block:: python

            import time
            from adafruit_featherwing import neopixel_featherwing

            neopixel = neopixel_featherwing.NeoPixelFeatherWing()
            neopixel.brightness = 0
            neopixel.fill(0xFFFFFF)
            for i in range(0, 6):
                neopixel.brightness = (i / 10)
                time.sleep(.2)

            neopixel.brightness = 0.3

        """
        return super().brightness