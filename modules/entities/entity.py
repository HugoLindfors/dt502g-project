from pygame import image, transform, Surface, Rect, error

class Entity:
    entity_dic = {}
    dt = 0  # Delta time for movement calculations

    def __init__(self, name="empty", img_path="empty", width=200, height=200, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        try:
            self.image = image.load(img_path).convert_alpha()
            self.image = transform.scale(self.image, (width, height))
        except (error, FileNotFoundError) as e:
            print(f"No image at {img_path} > Entity error: {e}")
            self.image = Surface((width, height))
            self.image.fill((0, 0, 0))
        Entity.entity_dic[self.name] = self

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_img(self):
        return self.image

    def get_rect(self):
        return self.get_img().get_rect(topleft=self.get_position())

    def draw_item(self, screen: Surface):
        screen.blit(self.get_img(), self.get_position())

    def update(self, screen: Surface):
        pass

    @staticmethod
    def pass_dt(a: float):
        Entity.dt = a

    def check_collision(self):
        for entity in Entity.entity_dic.values():
            if entity is not self and self.get_rect().colliderect(entity.get_rect()):
                return entity, True
        return None, False
