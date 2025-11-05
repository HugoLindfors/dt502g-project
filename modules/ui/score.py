import pygame

class score:
    def __init__(self, x, y, width= 120, height = 60, font_size= 36):
        self.score = 0
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, font_size)
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)

    def add_points(self, points):
        self.score += points
    
    def reset_score(self):
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

        text_surface = self.font.render(f"score: {self.score}", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

