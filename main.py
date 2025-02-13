import pygame
from menu import main_menu

pygame.init()

#Window settings
pygame.display.set_caption("Zombie Assault: Hopeless Resistance Against Annihilation")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
size = screen.get_size()
clock = pygame.time.Clock()

running = True
while running:
    screen.fill("white")  #Clear screen at the start of the frame

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    running = main_menu(size,screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()