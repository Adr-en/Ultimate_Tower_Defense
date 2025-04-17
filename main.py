import pygame
from menu import*
from games import*
import class_enemy

pygame.init()
running = True

dragging = False
skibidi = pygame.font.SysFont(None, 48)


while running:

    screen.fill("white")  #Clear screen at the start of the frame

    if main_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean, choosen_map = main_menu()

    if choose_menu_boolean:
        running, main_menu_boolean, choose_menu_boolean, choosen_map = choose_map_menu()

    if choosen_map == 1 :
        dragging = game_map_1(dragging)
        score_text = skibidi.render(str(class_enemy.currency.get()), True, "gold")
        screen.blit(score_text, (10, 10)) #Add a gold image and put it in the middle maybe




    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()
    clock.tick(60)

pygame.quit()