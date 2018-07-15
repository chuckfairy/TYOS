import os
import pygame
import time
import random

DEBUG = True
class pyscope :
    screen = None;

    def __init__(self):
        os.environ["SDL_FBDEV"] = "/dev/fb1"
        os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen" #Use touchscreen instead of event0
        os.environ["SDL_MOUSEDRV"] = "TSLIB"

        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            if DEBUG:
                print "I'm running under X display = {0}".format(disp_no)

        # size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        size = (450, 450)
        if DEBUG:
            print "Framebuffer size: %d x %d" % (size[0], size[1])

        self.screen = pygame.display.set_mode(size, 0, 32)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()
