import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
screen_width = 700
screen_height = 500
# Set the width and height of the screen [width, height]
#size = (700, 500)

screen = pygame.display.set_mode((screen_width,screen_height))
 
pygame.display.set_caption("DT502G Project - The Game")


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
x = 200
y = 200
vel = 10
rect_width = 20
rect_height = 20

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0: 
        x -= vel 
		
    if keys[pygame.K_RIGHT] and x<screen_width-rect_width: 
        x += vel 
		
    if keys[pygame.K_UP] and y>0: 
        y -= vel 
		
    if keys[pygame.K_DOWN] and y<screen_height-rect_height: 
        y += vel
    # --- Screen-clearing code goes here
    

    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
  
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen,RED,(x,y,rect_width,rect_height)) #(förflyttning i x-led, förflyttning i y-led, bredd, höjd)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()