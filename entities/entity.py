from pygame import image
from pygame import transform
from pygame import rect
from pygame import Surface
from pygame import error

class Entity:


    def __init__(
        self,
        name: str = "empty",
        img_path: str = "empty",
        width: int = 200,
        height: int = 200,
        x: int = 0,
        y: int = 0,
    ):
        self.name = name
        self.x = x
        self.y = y
        try:
            self.image = image.load(img_path)
            self.image = transform.scale(self.image, (width, height))
        except (error, FileNotFoundError) as e:
            print(f"No image at {img_path} > Item class error: {e}")
            self.image = Surface((width, height))
            self.image.fill((0,0,0))

    def __str__(self):
        return f"{self.name}"

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def get_img(self):
        return self.image

    def get_rect(self) -> rect.Rect:
        hitbox_x, hitbox_y = self.get_position()
        return self.get_img().get_rect(topleft=(hitbox_x, hitbox_y))

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw_item(self, screen: Surface) -> None:
        screen.blit(self.get_img(), self.get_position())

    def check_collision(self, player_pos: rect.Rect) -> bool:
        return self.get_rect().colliderect(player_pos)
