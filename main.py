
import pygame
from pygame import display, event, image, key, transform
from pygame.time import Clock
#from entities.items.items import Item
#from entities.items.scrap import Scrap
from entities.entity import Entity
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
player_img = image.load("img/player.png").convert_alpha()

# RESIZE IMAGE
player_img = transform.scale(player_img, (80, 80))
player_width, player_height = player_img.get_size()


x, y = 200, 200
vel = 10

loop_should_break = False
clock = Clock()
ent = Entity("test","img/player.png",200,200,500,500)
ent2 = Entity("test2","img/player.png",100,100,300,300)
ent3 = Entity("test3","img/player.png",200,200,900,300)

while not loop_should_break:


    for evt in event.get():
        if evt.type == pygame.QUIT:
            done = True

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

    if (
        dx != 0 and dy != 0
    ):  # diagonal movement correction (would be too fast otherwise)
        dx *= 0.7071  # 1/sqrt(2)
        dy *= 0.7071

    x += dx * vel
    y += dy * vel
    x = max(0, min(SCREEN_WIDTH - player_width, x))
    y = max(0, min(SCREEN_HEIGHT - player_height, y))

    #player_rect = player_img.get_rect(topleft=(x, y))
    screen.fill(GREEN)
    #screen.blit(player_img, (x, y))

    ent2.draw_item(screen)  
    ent2.set_position(x,y)

    ent.draw_item(screen)
    ent3.draw_item(screen)
    
    
    

    print(ent2.check_collision())    
       
    
    display.flip()

    clock.tick(60)

pygame.quit()

