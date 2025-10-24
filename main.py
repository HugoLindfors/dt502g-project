import pygame
from pygame import display, event, image, key, transform
from pygame.time import Clock


# STATIC VARIABLES
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 127, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)


pygame.init()

# SCREEN SETUP
info = display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
display.set_caption("DT502G Project - The Game")

# LOAD AND SCALE PLAYER IMAGE
player_image = image.load("images/player.png").convert_alpha()

# RESIZE IMAGE
player_image = transform.scale(player_image, (80, 80))
player_width, player_height = player_image.get_size()


x, y = 200, 200
v = 10

loop_should_break = False
clock = Clock()

while not loop_should_break:

    for evt in event.get():
        if evt.type == pygame.QUIT:
            loop_should_break = True

    keys = key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True

    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_d]:
        dx = 1
    if keys[pygame.K_w]:
        dy = -1
    if keys[pygame.K_s]:
        dy = 1
    if keys[pygame.K_LSHIFT]:
        if v == 10:
            v = 20
        else:
            v = 10
    if keys[pygame.K_LCTRL]:
        if v == 10:
            v = 5
        else:
            v = 10

    if dx and dy:
        dx *= 0.7071
        dy *= 0.7071

    x += dx * v
    y += dy * v
    x = max(0, min(SCREEN_WIDTH - player_width, x))
    y = max(0, min(SCREEN_HEIGHT - player_height, y))

    screen.fill(GREEN)
    screen.blit(player_image, (x, y))

    # drawing code should go here

    display.flip()

    clock.tick(60)

pygame.quit()
