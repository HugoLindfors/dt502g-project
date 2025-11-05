from pygame import image, transform, Surface, error
from pygame.rect import Rect
from colors import *


class Entity:

    def __init__(
        self,
        name="",
        image_path="",
        width=200,
        height=200,
        xpos=0,
        ypos=0,
    ):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        try:
            self.image = image.load(image_path)
            self.image = transform.scale(self.image, (width, height))
        except (error, FileNotFoundError) as e:
            print(f"No image at {image_path} > Item class error: {e}")
            self.image = Surface((width, height))
            self.image.fill(BLACK)

    def __str__(self):
        return rf"{self.name}"

    def get_position(self) -> tuple[int, int]:
        return self.xpos, self.ypos

    def get_image(self):
        return self.image

    def get_rect(self) -> Rect:
        hitbox_x, hitbox_y = self.get_position()
        return self.get_image().get_rect(topleft=(hitbox_x, hitbox_y))

    def set_position(self, xpos: int, ypos: int) -> None:
        self.xpos = xpos
        self.ypos = ypos

    def draw(self, master: Surface) -> None:
        master.blit(self.get_image(), self.get_position())

    def check_collision(self, player_pos: Rect) -> bool:
        return self.get_rect().colliderect(player_pos)
