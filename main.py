import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# --- Screen Setup ---
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h  # Get full display size
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption("DT502G Project - The Game")

# --- Load and Scale Player Image ---
player_img = pygame.image.load('img/player.png').convert_alpha()

# Resize image (change 80, 80 to any size you want)
player_img = pygame.transform.scale(player_img, (80, 80))
player_width, player_height = player_img.get_size()


x, y = 200, 200
vel = 10

# --- Main Loop ---
done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True

        
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1

    if dx != 0 and dy != 0:
        dx *= 0.7071  # 1/sqrt(2)
        dy *= 0.7071

    x += dx * vel
    y += dy * vel
    x = max(0, min(screen_width - player_width, x))
    y = max(0, min(screen_height - player_height, y))
    
    screen.fill(WHITE)
    screen.blit(player_img, (x, y))

    
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
  
    
 
    # --- Drawing code should go here
    # pygame.draw.rect(screen,RED,(x,y,rect_width,rect_height)) #(förflyttning i x-led, förflyttning i y-led, bredd, höjd)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()