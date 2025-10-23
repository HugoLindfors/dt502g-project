# Imports
from pygame import init as init_game, quit as quit_game, QUIT as QUIT_GAME
from pygame.display import (
    set_caption as set_display_caption,
    set_mode as set_display_mode,
)
from pygame.event import get as get_event

# Screen settings
HEIGHT = 300
WIDTH = 400
CAPTION = "DT502G Project - The Game"


# Init runs once
def init():
    # Init
    init_game()

    screen = set_display_mode((WIDTH, HEIGHT))
    set_display_caption(CAPTION)


# Loop runs continuously
def loop():
    # Game loop
    loop_should_break = False
    while not loop_should_break:
        for event in get_event():
            if event.type == QUIT_GAME:
                loop_should_break = True

    # Quit
    quit_game()


# Program main entry point
def main():
    init()
    loop()


if __name__ == "__main__":
    main()
