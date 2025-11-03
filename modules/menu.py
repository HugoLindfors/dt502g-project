import pygame
import random
from pygame import image, display

# MENU CLASS
class Menu:
    def __init__(self, screen, screen_width, screen_height, title_image_path, star_image_path, num_stars=50):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        # TITLE START MENU
        self.title_image = image.load(title_image_path).convert_alpha()
        self.title_rect = self.title_image.get_rect(center=(screen_width // 2, screen_height // 3))

        # STAR IMAGE
        self.star_image = image.load(star_image_path).convert_alpha()
        self.star_image = pygame.transform.scale(self.star_image, (20, 20))
        self.star_width, self.star_height = self.star_image.get_size()

        # CREATE RANDOM STAR POSITIONS
        self.num_stars = num_stars
        self.star_positions = [
            (random.randint(0, screen_width - self.star_width),
             random.randint(0, screen_height - self.star_height))
            for _ in range(self.num_stars)
        ]

    # DRAW START MENU
    def draw(self):
        self.screen.fill((0, 0, 0))
        
        # DRAW STARS
        for pos in self.star_positions:
            self.screen.blit(self.star_image, pos)

        # DRAW GAME LOGO
        self.screen.blit(self.title_image, self.title_rect)

        # DRAW "PRESS ENTER TO START"
        font = pygame.font.SysFont(None, 60)
        text = font.render("Press ENTER to Start", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 1.6))
        self.screen.blit(text, text_rect)

        # UPDATE DISPLAY
        pygame.display.flip()
