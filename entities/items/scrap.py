from entities.items.items import Item
from pygame import rect

class Scrap(Item):


    scrap_counter = 0

    def __init__(self, name = "empty", 
               img_path = "empty", 
               width = 200, 
               height = 200, 
               x = 0, 
               y = 0):      
        super().__init__(name, img_path, width, height, x, y)

    def scrape_logic(self) -> None:
        Scrap.scrap_counter += 1
        return Scrap.scrap_counter
        
            

        

   
    
    

        

    