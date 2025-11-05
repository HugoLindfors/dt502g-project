import pygame
from pygame import image, transform

class health_bar:
    def __init__(self, screen, max_health=3, heart_image_path="images/heart.png",
                 gray_heart_image_path="images/gray_heart.png", heart_size=(40, 40), padding=10):
        
        self.screen = screen
        self.max_health = max_health
        self.current_health = max_health
        self.heart_size = heart_size
        self.padding = padding


        self.heart_image = image.load(heart_image_path).convert_alpha()
        self.heart_image = transform.scale(self.heart_image, heart_size)

        self.gray_heart_image = image.load(gray_heart_image_path).convert_alpha()
        self.gray_heart_image = transform.scale(self.gray_heart_image, heart_size)

    def set_health(self, health):
        self.current_health = max(0, min(self.max_health, health)) 


    def draw(self):
        for i in range(self.max_health):
            x = self.padding + i * (self.heart_size[0] + self.padding)
            y = self.screen.get_height() - self.heart_size[1] - self.padding 
            if i < self.current_health:
                self.screen.blit(self.heart_image, (x, y))
            else:
                self.screen.blit(self.gray_heart_image, (x, y))
    
    def lose_health(self, amount=1):
        self.current_health = max(0, self.current_health - amount)