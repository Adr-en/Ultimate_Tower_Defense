import pygame
from menu import*
from Class Ennemy import *

pygame.init()

running = True

while running:

    screen.fill("white")  #Clear screen at the start of the frame

    if main_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean = main_menu()

        pygame.draw.rect(screen,'black',((610,590),(710,665)))
    if choose_menu_boolean:
        choose_map_menu()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()