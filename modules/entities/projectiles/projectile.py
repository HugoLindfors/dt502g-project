from modules.entities.entity import Entity
from pygame import Surface

class Laser(Entity):
    laser_instance_index = 0
    def __init__(
        self,
        name: str = "empty",
        img_path: str = "empty",
        width: int = 200,
        height: int = 200,
        x: int = 0,
        y: int = 0,
                ):
        Laser.laser_instance_index += 1
        super().__init__(f"{name}{Laser.laser_instance_index}",img_path,width,height,x,y)
        self.speed = -1000
        

    def update(self,screen: Surface):
    
        x,y = self.get_position()
        self.set_position(x,y-1)   
        if self.get_rect().bottom < 0:
            Entity.entity_dic.pop(self.name)
        
            