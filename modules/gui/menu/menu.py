import random
import pygame.font as pygame_font
from pygame import display, image, transform, Surface
from colors import *


# MENU CLASS
class Menu:
    screen: Surface
    screen_width: int
    screen_height: int

    def __init__(
        self,
        screen: Surface,
        screen_width: int,
        screen_height: int,
        title_image_path: str,
        star_image_path: str,
        star_count=50,
    ):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        # TITLE START MENU
        self.title_image = image.load(title_image_path).convert_alpha()
        self.title_rect = self.title_image.get_rect(
            center=(screen_width // 2, screen_height // 3)
        )

        # STAR IMAGE
        self.star_image = image.load(star_image_path).convert_alpha()
        self.star_image = transform.scale(self.star_image, (20, 20))
        self.star_width, self.star_height = self.star_image.get_size()

        # CREATE RANDOM STAR POSITIONS
        self.star_count = star_count
        self.star_positions = [
            (
                random.randint(0, screen_width - self.star_width),
                random.randint(0, screen_height - self.star_height),
            )
            for _ in range(self.star_count)
        ]

    # DRAW START MENU
    def draw(self):
        self.screen.fill(BLACK)

        # DRAW STARS
        for star_pos in self.star_positions:
            self.screen.blit(self.star_image, star_pos)

        # DRAW GAME LOGO
        self.screen.blit(self.title_image, self.title_rect)

        # DRAW "PRESS ENTER TO START"
        pygame_font.SysFont(None, 60)
        text = pygame_font.render("Press ENTER to Start", True, WHITE)
        text_rect = text.get_rect(
            center=(self.screen_width // 2, self.screen_height // 1.6)
        )
        self.screen.blit(text, text_rect)

        # UPDATE DISPLAY
        display.flip()
