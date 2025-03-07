from Definitions.definitions_main_menu import*
from Definitions.definitions_choose_menu import*

main_menu_boolean = True
choose_menu_boolean = False

map_pointer = 0

def main_menu() :

    exit_game = True
    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.blit(start_button, start_button_rect)
    screen.blit(option_button, option_button_rect)
    screen.blit(credits_button, credits_button_rect)
    screen.blit(quit_button, quit_button_rect)
    screen.blit(main_menu_background, (0, 0))  # MUST put the background on top of the buttons

    if 710 <= mouse_x <= 910 and 590 <= mouse_y < 665 :
        screen.blit(start_button_image, (0,0))

    if 710 <= mouse_x <= 910 and 665 <= mouse_y < 740 :
        screen.blit(option_button_image, (0, 0))

    if 710 <= mouse_x <= 910 and 740 <= mouse_y < 815 :
        screen.blit(credits_button_image, (0,0))

    if 1470 <= mouse_x <= 1600 and 0 <= mouse_y < 65 :
        screen.blit(quit_button_image, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):

                global main_menu_boolean
                global choose_menu_boolean
                main_menu_boolean = False
                choose_menu_boolean = True
                return exit_game, main_menu_boolean, choose_menu_boolean

            if option_button_rect.collidepoint(event.pos):
                print("Option")

            if credits_button_rect.collidepoint(event.pos):
                print("Credits")

            if quit_button_rect.collidepoint(event.pos):
                exit_game = False

    return exit_game, main_menu_boolean, choose_menu_boolean



def choose_map_menu() :

    exit_game = True
    open_game_menu = False
    mouse_x, mouse_y = pygame.mouse.get_pos()

    global map_pointer

    map_pointer = (map_pointer + 3) % 3  #Ensures map_pointer stays within [0, 1, 2]
    match map_pointer:
        case 0:
            screen.blit(choose_menu_option1, (0, 0))
        case 1:
            screen.blit(choose_menu_option2, (0, 0))
        case 2:
            screen.blit(choose_menu_option3, (0, 0))

    if 525 <= mouse_x <= 625 and 815 <= mouse_y < 865 :
        screen.blit(left_arrow_highlight, (0,0))

    if 985 <= mouse_x <= 1085 and 815 <= mouse_y < 865 :
        screen.blit(right_arrow_highlight, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if left_arrow.collidepoint(event.pos):
                map_pointer -= 1

            if right_arrow.collidepoint(event.pos):
                map_pointer += 1

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                open_game_menu = True

            if event.key == pygame.K_ESCAPE and open_game_menu == True:
                open_game_menu = False


    return exit_game
