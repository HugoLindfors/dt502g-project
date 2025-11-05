from entities.items.items import Item
from pygame import rect
from entities.entity import Entity
class Scrap(Item):


    scrap_counter = 0

    def __init__(self, name = "empty", 
               img_path = "empty", 
               width = 200, 
               height = 200, 
               x = 0, 
               y = 0,
               target_entity_detect = "player"
               ):      
        super().__init__(name, img_path, width, height, x, y)

    def pick(self) -> int:
        e,c = self.check_collision()
        print(Entity.entity_dic)
        if self.name in Entity.entity_dic:
             if c and self.target_entity_detect == e.name:
                 Scrap.scrap_counter += 1
                 del  Entity.entity_dic[self.name]
                 print("yes")
       
        return Scrap.scrap_counter

        
            

        

   
    
    

        

    