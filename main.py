import pygame
from menu import*
from class_enemy import *


pygame.init()

running = True
i = 0
while running:

    screen.fill("white")  #Clear screen at the start of the frame

    if main_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean = main_menu()

    if choose_menu_boolean:
        choose_map_menu()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False



    pygame.display.flip()
    clock.tick(60)

pygame.quit()