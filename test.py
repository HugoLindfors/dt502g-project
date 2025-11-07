from modules.entities.player import player
from modules.menu import Menu
from modules.ui.health_bar import health_bar
from modules.ui.score import score
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

# CREATE HEALTHBAR INSTANCE
health_bar = health_bar(screen, max_health=3, heart_image_path="images/heart.png",
                       gray_heart_image_path="images/gray_heart.png")
# CREATE SCORE INSTANCE
player_score = score(20, 20)

# GAME STATE
loop_should_break = False
game_started = False
game_over = False
clock = Clock()


# health_bar.lose_health(2) # losing heart test

# MAIN LOOP
while not loop_should_break:
    for evt in event.get():
        if evt.type == pygame.QUIT:
            loop_should_break = True
        elif evt.type == pygame.KEYDOWN:
            # START MENU
            if not game_started:
                if evt.key == pygame.K_RETURN:
                    game_started = True
                elif evt.key == pygame.K_ESCAPE:
                    loop_should_break = True
            # GAMEPLAY
            elif not game_over:
                if evt.key == pygame.K_ESCAPE:
                    loop_should_break = True
                # TEST: lose health
                elif evt.key == pygame.K_h:
                    health_bar.lose_health(1)
                    if health_bar.current_health <= 0:
                        game_over = True
                # TEST: add points
                elif evt.key == pygame.K_5:
                    player_score.add_points(50)
                elif evt.key == pygame.K_0:
                    player_score.reset_score()
            # GAME OVER
            elif game_over:
                if evt.key == pygame.K_ESCAPE:
                    loop_should_break = True
                elif evt.key == pygame.K_RETURN:
                    # RESET EVERYTHING
                    player_score.reset_score()
                    health_bar.set_health(3)
                    player.x = 200
                    player.y = SCREEN_HEIGHT - 80 - 20
                    game_over = False

    # START MENU
    if not game_started:
        menu.draw()
        clock.tick(60)
        continue
    
    # GAME OVER SCREEN
    if game_over:
        menu.draw_game_over()
        clock.tick(60)
        continue

    # PLAYER MOVEMENT
    keys_pressed = key.get_pressed()
    player.handle_movement(keys_pressed, SCREEN_WIDTH)

    # DRAWING CODE
    screen.fill((55, 66, 91)) # TEMP BACKGROUND
    health_bar.draw()
    player_score.draw(screen)
    player.draw(screen)

    display.flip()
    clock.tick(60)

pygame.quit()