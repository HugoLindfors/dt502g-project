from entities.items.items import Item
from pygame import rect


img_path = "img/player.png"
class Scrap(Item):

    scrap_counter = 0
    
    def __init__(
        self,
        name: str,
        width: int,
        height: int,
        x: int,
        y: int,
    ):

        super().__init__(name, img_path, width, height, x, y)
        self.scrap_counter = 0

    def pick_scrap(self, player_rect: rect.Rect):
        if self.check_collision(player_rect):
            print("got it!")
            self.scrap_counter += 1

    def get_scrap_counter(self):
        return self.scrap_counter
    