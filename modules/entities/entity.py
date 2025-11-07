from pygame import image, transform, rect, Surface, error
import math
class Entity:


    entity_dic = {}

    dt = 0

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
            self.image.fill((0, 0, 0))
        Entity.entity_dic[self.name] = self
        print(Entity.entity_dic)

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
    #overwrite the function if you want
    def update(self,screen: Surface):
        pass
    
    def pass_dt(a:float):
        Entity.dt = a

    def check_collision(self) -> tuple["Entity | None", bool]:
        for key in Entity.entity_dic:
            if Entity.entity_dic[key] is not self:
                if self.get_rect().colliderect(Entity.entity_dic[key].get_rect()):
                    return (Entity.entity_dic[key], True)
            else:
                continue
        return (None, False)
        


            
    

            

