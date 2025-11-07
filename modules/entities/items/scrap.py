from .items import Item
from pygame import rect
from modules.entities.entity import Entity



class Scrap(Item):


    scrap_counter = 0
    scrap_index = 0
    def __init__(self,
               name = "empty",
               image_path = "empty",
               width = 200, 
               height = 200, 
               x = 0, 
               y = 0,
               target_entity_detect = "player"
               ):     
        self.target_entity_detect = target_entity_detect 
        Scrap.scrap_index +=1

        super().__init__(f"scrap{Scrap.scrap_index}", image_path, width, height, x, y)
        
    def pick(self) -> int:
        e,c = self.check_collision()
        print(Entity.entity_dic)
        if c and self.target_entity_detect == e.name:
             Scrap.scrap_counter += 1
             Entity.entity_dic.pop(self.name)
             print("yes")
             print(Entity.entity_dic)
       
        return Scrap.scrap_counter

        
            

        

   
    
    

        

