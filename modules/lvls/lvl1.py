import pygame
from os.path import join
from random import randint

pygame.init()

# Constants
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
FPS = 60

# Setup
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Galaxy Blaster")
clock = pygame.time.Clock()

# Load and scale images
player_img = pygame.image.load(join("images", "player.png")).convert_alpha()
player_img = pygame.transform.scale(player_img, (60, 60))  # Smaller player

laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_surf = pygame.transform.scale(laser_surf, (10, 30))  # Thin laser

meteor_surf = pygame.image.load(join("images", "slime.png")).convert_alpha()
meteor_surf = pygame.transform.scale(meteor_surf, (50, 50))  # Medium meteor

# Groups
all_sprites = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
meteor_group = pygame.sprite.Group()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = player_img
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.direction = pygame.Vector2()
        self.speed = 300
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
        self.lives = 3
        self.score = 0

    def laser_timer(self):
        if not self.can_shoot and pygame.time.get_ticks() - self.laser_shoot_time >= self.cooldown_duration:
            self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * self.speed * dt

        self.laser_timer()
        if keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, all_sprites, laser_group)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

# Laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups, laser_group):
        super().__init__(groups, laser_group)
        self.image = surf
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = -400

    def update(self, dt):
        self.rect.y += self.speed * dt
        if self.rect.bottom < 0:
            self.kill()

# Meteor class
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups, meteor_group):
        super().__init__(groups, meteor_group)
        self.image = surf
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        self.rect.y += 100 * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

# Create player
player = Player(all_sprites)

# Meteor spawn event
meteor_event = pygame.USEREVENT + 1
pygame.time.set_timer(meteor_event, 500)

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x = randint(0, WINDOW_WIDTH)
            Meteor(meteor_surf, (x, -50), all_sprites, meteor_group)

    # Update
    all_sprites.update(dt)

    # Laser-Meteor collision
    for laser in laser_group:
        hit_meteors = pygame.sprite.spritecollide(laser, meteor_group, True)
        if hit_meteors:
            laser.kill()
            player.score += 100

    # Player-Meteor collision
    if pygame.sprite.spritecollide(player, meteor_group, True):
        player.lives -= 1
        if player.lives <= 0:
            print("Game Over")
            running = False

    # Win condition
    if player.score >= 1000:
        print("Level Complete!")
        running = False

    # Draw
    display_surface.fill("black")
    all_sprites.draw(display_surface)

    # HUD
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {player.lives}", True, (255, 0, 0))
    display_surface.blit(score_text, (10, 10))
    display_surface.blit(lives_text, (10, 50))

    pygame.display.update()

pygame.quit()
