from pygame import image, transform, rect, Surface, error
from entities.entity import Entity
class Item(Entity):
  
  
  def __init__(self, name = "empty", 
               img_path = "empty", 
               width = 200, 
               height = 200, 
               x = 0, 
               y = 0):
    
    super().__init__(name, img_path, width, height, x, y)

  def pick(self,func: function, entity_rect: rect.Rect)-> bool:
        pass
