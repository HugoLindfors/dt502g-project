from modules.entities.player import player
from modules.menu import Menu
import pygame
from pygame import display, event, key
from pygame.time import Clock

pygame.init()

# SCREEN SETUP
info = display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("DT502G Project - The Game")

# CREATE PLAYER INSTANCE
player = player.Player(200, SCREEN_HEIGHT - 80 - 20, "images/player.png")  # x, y, image_path

# CREATE MENU INSTANCE
menu = Menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT, "images/game_logo.png", "images/star.png", num_stars=50)

# GAME STATE
loop_should_break = False
game_started = False
clock = Clock()

# MAIN LOOP
while not loop_should_break:

    # --- Event handling ---
    for evt in event.get():
        if evt.type == pygame.QUIT:
            loop_should_break = True
        elif evt.type == pygame.KEYDOWN:
            if not game_started:
                if evt.key == pygame.K_RETURN:
                    game_started = True
                elif evt.key == pygame.K_ESCAPE:
                    loop_should_break = True
            else:
                if evt.key == pygame.K_ESCAPE:
                    loop_should_break = True

    # --- Start menu ---
    if not game_started:
        menu.draw()
        clock.tick(60)
        continue

    # --- Player movement ---
    keys_pressed = key.get_pressed()
    player.handle_movement(keys_pressed, SCREEN_WIDTH)

    # --- Drawing code ---
    screen.fill((0, 255, 0))
    player.draw(screen)

    # drawing code should go here

    display.flip()

    # --- Limit to 60 frames per second ---
    clock.tick(60)

# Close the window and quit.
pygame.quit()