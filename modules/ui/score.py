import pygame

class Score:
    def __init__(self, x, y, width=120, height=60, font_size=36):
        self.value = 0  # standardized attribute
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont(None, font_size)
        self.text_color = (255, 255, 255)
        self.bg_color = (0, 0, 0)

    def add_points(self, points):
        self.value += points

    def reset_score(self):
        self.value = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 3)

        text_surface = self.font.render(f"Score: {self.value}", True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
