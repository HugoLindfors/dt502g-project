import pygame
import random
from pygame import image, transform

class Menu:
    def __init__(self, screen, screen_width, screen_height, title_image_path, star_image_path, game_over_image_path, num_stars=50):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.SysFont(None, 60)

        # Load title image without forcing a weird size
        self.title_image = image.load(title_image_path).convert_alpha()
        self.title_rect = self.title_image.get_rect(center=(screen_width//2, screen_height//3))

        self.star_image = transform.scale(image.load(star_image_path).convert_alpha(), (20,20))
        self.star_positions = [(random.randint(0, screen_width-20), random.randint(0, screen_height-20)) for _ in range(num_stars)]

        self.game_over_image = transform.scale(image.load(game_over_image_path).convert_alpha(), (400, 100))
        self.game_over_rect = self.game_over_image.get_rect(center=(screen_width//2, screen_height//2))

    def draw_background(self):
        self.screen.fill((0,0,0))
        for pos in self.star_positions:
            self.screen.blit(self.star_image, pos)

    def draw(self):
        self.draw_background()
        self.screen.blit(self.title_image, self.title_rect)
        text = self.font.render("Press ENTER to Start", True, (255,255,255))
        self.screen.blit(text, text.get_rect(center=(self.screen_width//2, self.screen_height//1.6)))
        pygame.display.flip()

    def draw_game_over(self):
        self.draw_background()
        self.screen.blit(self.game_over_image, self.game_over_rect)
        text = self.font.render("Press ENTER to Restart or ESC to Quit", True, (255,255,255))
        self.screen.blit(text, text.get_rect(center=(self.screen_width//2, self.screen_height//1.6)))
        pygame.display.flip()
