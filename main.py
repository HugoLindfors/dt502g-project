from pygame import init, quit, QUIT
from pygame.display import set_caption, set_mode
from pygame.event import get

init()

screen = set_mode((400, 300))
set_caption("Hello Pygame")

loop_should_break = False
while not loop_should_break:
    for event in get():
        if event.type == QUIT:
            loop_should_break = True

quit()
