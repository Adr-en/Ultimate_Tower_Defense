import pygame
import time

pygame.init()

#Initialise projectiles in a list
projectiles = []

#Window settings
pygame.display.set_caption("UTD - Ultimate Tower Defense")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
size = screen.get_size()
clock = pygame.time.Clock()

#Load images
test = pygame.image.load("test.png").convert()
test = pygame.transform.smoothscale(test, (50, 50))  #Resize image
background = pygame.image.load("../Assets/background_level_1.jpeg").convert()
background = pygame.transform.smoothscale(background, (size))

tower = pygame.image.load("test_tower.png").convert()
tower = pygame.transform.smoothscale(tower, (100, 100))  #Resize tower
tower_rect = tower.get_rect(topleft=(1300, 600))  #Define hitbox

#Green squares (tower placement areas)
emp1 = pygame.Surface((50, 50))
emp1.fill("green")
emp1_rect = emp1.get_rect(topleft=(800, 600))
emplacement_1 = False

emp2 = pygame.Surface((50, 50))
emp2.fill("green")
emp2_rect = emp2.get_rect(topleft=(800, 200))
emplacement_2 = False

#Character movement variables
pos_adrien = 0
y = 400
velocity = 1  #Increased for smoother movement

running = True
dragging = False  #If tower is being dragged

while running:
    screen.fill("white")  #Clear screen at the start of the frame

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if tower_rect.collidepoint(event.pos):  #Click inside tower
                dragging = True  #Start dragging

        elif event.type == pygame.MOUSEBUTTONUP:

            if emp1_rect.collidepoint(event.pos) and dragging:
                emplacement_1 = True

            if emp2_rect.collidepoint(event.pos) and dragging :
                emplacement_2 = True

            dragging = False  # Stop dragging when mouse is released
            tower_rect = tower.get_rect(topleft=(1300, 600))

        elif event.type == pygame.MOUSEMOTION and dragging :
            tower_rect.center = event.pos  #Move tower while dragging

    #Draw elements
    pygame.draw.line(screen, "black", (0, 350), (1540, 350), 2)  #Top line
    pygame.draw.line(screen, "black", (0, 450), (1540, 450), 2)  #Bottom line

    screen.blit(test, (pos_adrien - 25, y - 25))  #Draw character
    screen.blit(tower, tower_rect)  #Draw tower
    screen.blit(background, (0, 0))

    screen.blit(emp1, (800, 600))  #Draw placement areas
    screen.blit(emp2, (800, 200))

    # Character movement logic
    pos_adrien += velocity
    if pos_adrien > 1490:
        pos_adrien = 0  #Reset character position to start again

    if emplacement_1 :
        screen.blit(tower, emp1_rect.topleft) #Place a tower at emplacement 1

        start_position = emp1_rect.bottomright
        target_position = (pos_adrien,y)

        pygame.draw.line(screen, "red", (start_position[0],start_position[1]), (target_position[0],target_position[1]), 2)

    if emplacement_2 :
        screen.blit(tower, emp2_rect.topleft) #Place a tower at emplacement 2

        start_position = emp2_rect.bottomright
        target_position = (pos_adrien, y)

        pygame.draw.line(screen, "red", (start_position[0], start_position[1]),(target_position[0], target_position[1]), 2)

    pygame.display.flip()  #Update the screen
    clock.tick(60)  #Limit frame rate to 60 fps to prevent speed issues

pygame.quit()
