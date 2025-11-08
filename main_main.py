import pygame
from pygame import display, event, key
from pygame.time import Clock
import random
import time

# ENTITIES
from modules.entities.player.player import Player
from modules.entities.enemies.slime import Slime
from modules.entities.enemies.boss import Boss
from modules.entities.enemies.enemy import Enemy
from modules.entities.projectiles.projectile import Laser
from modules.entities.entity import Entity

# UI
from modules.ui.health_bar import HealthBar
from modules.ui.score import Score
from modules.ui.menu import Menu

pygame.init()

# --- SCREEN SETUP ---
info = display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("DT502G Project - The Game")

# --- GAME OBJECTS ---
player = Player(200, SCREEN_HEIGHT - 100)
health_bar = HealthBar(screen, max_health=3)
player_score = Score(20, 20)
menu = Menu(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
            title_image_path="images/game_logo.png",
            star_image_path="images/star.png",
            game_over_image_path="images/game_over.png",
            num_stars=50)

# --- GAME STATE ---
loop_should_break = False
game_started = False
game_over = False
level = 1

clock = Clock()

# Player collision cooldown
player_last_hit_time = 0
hit_cooldown = 0.5  # seconds

# --- LEVEL SPAWN FUNCTIONS ---
def spawn_level_1():
    slime = Slime(
        x=random.randint(50, SCREEN_WIDTH - 100),
        y=random.randint(20, 100)
    )
    return slime

def spawn_level_2():
    enemy = Enemy(
        "Enemy",
        "images/enemy.png",
        100,
        100,
        random.randint(50, SCREEN_WIDTH - 150),
        50,
        health=5,
        fires_projectiles=True
    )
    return enemy

def spawn_boss():
    return Boss()

# --- MAIN LOOP ---
while not loop_should_break:
    dt = clock.tick(60) / 1000
    Entity.pass_dt(dt)
    current_time = time.time()

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
                # PLAYER SHOOT
                player.fire(evt)

            # GAME OVER
            elif game_over:
                if evt.key == pygame.K_ESCAPE:
                    loop_should_break = True
                elif evt.key == pygame.K_RETURN:
                    # RESET GAME
                    player_score.reset_score()
                    health_bar.set_health(3)
                    player.set_position(200, SCREEN_HEIGHT - 100)
                    Entity.entity_dic.clear()
                    player = Player(200, SCREEN_HEIGHT - 100)
                    level = 1
                    game_over = False

    # START MENU
    if not game_started:
        menu.draw()
        continue

    # GAME OVER SCREEN
    if game_over:
        menu.draw_game_over()
        continue

    # PLAYER MOVEMEN
    keys_pressed = key.get_pressed()
    player.handle_movement(keys_pressed, SCREEN_WIDTH)

    # LEVEL SPAWNING
    if level == 1:
        if len([e for e in Entity.entity_dic.values() if "Slime" in e.name]) < 5:
            slime = spawn_level_1()
            Entity.entity_dic[slime.name] = slime
    elif level == 2:
        if len([e for e in Entity.entity_dic.values() if "Enemy" in e.name]) < 1:
            enemy = spawn_level_2()
            Entity.entity_dic[enemy.name] = enemy
    elif level == 3:
        if not any("Boss" in e.name for e in Entity.entity_dic.values()):
            boss = spawn_boss()
            Entity.entity_dic[boss.name] = boss

    # UPDATE ENTITIES
    for ent in list(Entity.entity_dic.values()):
        ent.update(screen)

    # LASER COLLISION DETECTION & SCORING
    for ent in list(Entity.entity_dic.values()):
        if isinstance(ent, Laser):
            collided_entity, collided = ent.check_collision()
            if collided and collided_entity.name not in ["player", ent.name]:
                if "Slime" in collided_entity.name or "Enemy" in collided_entity.name or "Boss" in collided_entity.name:
                    player_score.add_points(50)
                    # remove enemy
                    if collided_entity.name in Entity.entity_dic:
                        Entity.entity_dic.pop(collided_entity.name)
                    # remove laser
                    if ent.name in Entity.entity_dic:
                        Entity.entity_dic.pop(ent.name)

    # CHECK PLAYER COLLISIONS WITH COOLDOWN
    for ent in list(Entity.entity_dic.values()):
        if ent is not player and not isinstance(ent, Laser):
            if player.get_rect().colliderect(ent.get_rect()):
                if current_time - player_last_hit_time > hit_cooldown:
                    health_bar.lose_health(1)
                    player_last_hit_time = current_time
                    if health_bar.current_health <= 0:
                        game_over = True

    # --- LEVEL PROGRESSION ---
    if player_score.value >= 500 and level == 1:
        level = 2
    elif player_score.value >= 1000 and level == 2:
        level = 3

    # --- DRAW ---
    screen.fill((55, 66, 91))
    player.draw_item(screen)
    health_bar.draw()
    player_score.draw(screen)

    for ent in Entity.entity_dic.values():
        if ent is not player:
            ent.draw_item(screen)

    pygame.display.flip()
