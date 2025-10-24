# imports
from pygame import FULLSCREEN
from pygame import init as init_game, quit as quit_game, QUIT as QUIT_GAME
from pygame.display import (
    set_caption as set_display_caption,
    set_mode as set_display_mode,
)
from pygame.event import get as get_event

# screen settings
CAPTION = "DT502G Project - The Game"


def init():
    "init runs once"

    # init game
    init_game()

    set_display_mode((0,0),FULLSCREEN)
    set_display_caption(CAPTION)


def loop():
    "loop runs continuously"

    # game main loop
    loop_should_break = False
    while not loop_should_break:
        for event in get_event():
            if event.type == QUIT_GAME:
                loop_should_break = True

    # quit game
    quit_game()


def main():
    "Program main entry point."
    init()
    loop()


if __name__ == "__main__":
    main()
