from pygame import image, transform, rect, Surface, error
from modules.entities.entity import Entity
class Item(Entity):
  
  
  def __init__(self, name = "empty", 
               img_path = "empty", 
               width = 200, 
               height = 200, 
               x = 0, 
               y = 0):
    
    super().__init__(name, img_path, width, height, x, y)

  def pick(self)-> bool:
        pass
  
  def update(self,screen: Surface):
      x,y = self.get_position()
      self.set_position(x,y+2)
