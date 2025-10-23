# Imports
from pygame import init, quit, QUIT
from pygame.display import set_caption, set_mode
from pygame.event import get


def main():
    # Init
    init()

    # Screen settings
    HEIGHT = 300
    WIDTH = 400
    CAPTION = "DT502G Project - The Game"

    screen = set_mode((WIDTH, HEIGHT))
    set_caption(CAPTION)

    # Game loop
    loop_should_break = False
    while not loop_should_break:
        for event in get():
            if event.type == QUIT:
                loop_should_break = True

    # Quit
    quit()


if __name__ == "__main__":
    main()
