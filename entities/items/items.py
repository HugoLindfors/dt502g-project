from pygame import image
from pygame import transform
from pygame import rect
class item:

    def __init__(
        self,
        name: str = "empty",
        img_path: str = "empty",
        width: int = 200,
        height: int = 200,
        x: int = 0,
        y: int = 0
    ):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = rect.Rect(x,y,width,height)
        try:
            self.image = image.load(img_path)
            self.image = transform.scale(self.image, (self.width, self.height))
        except image.error as e:
            print(f"No image at {img_path}: {e}")
            self.image = image.surface((self.width, self.height))

    def __str__(self):
        return f"{self.name}"

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.move_entity()
    
    def move_entity(self) -> None:
        x,y = self.get_position()
        hitbox = self.get_rect()
        hitbox.move
        


    def get_rect(self)-> rect:
        return self.rect

    def check_collision(self, player_pos: tuple[int, int]) -> bool:
        player_x, player_y = player_pos
        item_x, item_y = self.get_position()
        return (item_x < player_x < item_x + self.width and
                item_y < player_y < item_y + self.height)
    
    def get_size(self) -> tuple[int, int]:
        return self.width, self.height