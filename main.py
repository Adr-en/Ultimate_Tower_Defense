import pygame
from menu import*
from games import*

pygame.init()
running = True

dragging = False
exit_game = True

while running:

    screen.fill("white")  #Clear screen at the start of the frame

    if main_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean, choosen_map = main_menu()

    if choose_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean, choosen_map = choose_map_menu()

    if choosen_map == 1 and not main_menu_boolean:
        dragging, main_menu_boolean, choosen_map = game_map_1(dragging, main_menu_boolean, choosen_map)
        if main_menu_boolean:
            choosen_map = 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()