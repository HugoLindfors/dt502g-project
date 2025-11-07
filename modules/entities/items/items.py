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
        for key in list(Entity.entity_dic):
          x,y = Entity.entity_dic[key].get_position()
          Entity.entity_dic[key].set_position(x,y+2)
          if y >= screen.get_height():
              del Entity.entity_dic[key]
