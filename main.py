import pygame
from menu import*
from games import*
import class_enemy

pygame.init()
running = True

dragging = False

while running:

    screen.fill("white")  #Clear screen at the start of the frame

    if main_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean, choosen_map = main_menu()

    if choose_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean, choosen_map = choose_map_menu()

    if choosen_map == 1 :
        dragging = game_map_1(dragging)





    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()