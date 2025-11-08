from modules.entities.entity import Entity
from pygame import Surface

class Laser(Entity):
    laser_instance_index = 0

    def __init__(self, x=0, y=0, width=10, height=30, img_path="images/laser.png",direction=-1):
        Laser.laser_instance_index += 1
        super().__init__(f"laser{Laser.laser_instance_index}", img_path, width, height, x, y)
        self.speed = -1000
        self.immune_entity_id = "player"
        self.direction = direction  # -1 for up, 1 for down

    def update(self, screen: Surface):
        # Move laser
        x, y = self.get_position()
        y += self.speed * Entity.dt * self.direction
        self.set_position(x, y)

        # Remove laser if offscreen
        if self.get_rect().bottom < 0 and self.get_rect().bottom < screen.get_height():
            if self.name in Entity.entity_dic:
                Entity.entity_dic.pop(self.name)
