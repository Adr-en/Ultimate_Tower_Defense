import pygame
from menu import*

pygame.init()

running = True
while running:

    screen.fill("white")  #Clear screen at the start of the frame

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    running = main_menu()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()