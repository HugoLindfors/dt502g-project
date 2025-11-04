import sys
import os

"""
This allows the code to omit the first modules folder from the imports, i.e. import entities instead of import modules.entities.
"""
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "modules"))
sys.path.insert(0, module_path)

import pygame
from pygame.display import Info as GetVidInfo
from pygame import display, event, NOFRAME
from pygame.time import Clock
from colors import *
from keybindings import *


def main():
    pygame.init()

    # SCREEN SETUP
    _vidinfo = GetVidInfo()
    SCREEN_WIDTH, SCREEN_HEIGHT = _vidinfo.current_w, _vidinfo.current_h
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)
    display.set_caption("DT502G Project - The Game")

    loop_should_break = bool(False)
    clock = Clock()

    while not loop_should_break:
        for evt in event.get():
            if evt.type == pygame.QUIT:
                loop_should_break = True
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
