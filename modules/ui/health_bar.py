import pygame
from pygame import image, transform

class HealthBar:
    def __init__(self, screen, max_health=3, heart_image_path="images/heart.png", gray_heart_image_path="images/gray_heart.png", heart_size=(40,40), padding=10):
        self.screen = screen
        self.max_health = max_health
        self.current_health = max_health
        self.heart_size = heart_size
        self.padding = padding
        self.heart_image = transform.scale(image.load(heart_image_path).convert_alpha(), heart_size)
        self.gray_heart_image = transform.scale(image.load(gray_heart_image_path).convert_alpha(), heart_size)

    def set_health(self, health: int):
        self.current_health = max(0, min(self.max_health, health))

    def lose_health(self, amount=1):
        self.current_health = max(0, self.current_health - amount)

    def draw(self):
        for i in range(self.max_health):
            x = self.padding + i * (self.heart_size[0] + self.padding)
            y = self.screen.get_height() - self.heart_size[1] - self.padding
            self.screen.blit(self.heart_image if i < self.current_health else self.gray_heart_image, (x, y))
