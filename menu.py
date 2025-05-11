from Definitions.definitions_main_menu import*
from Definitions.definitions_choose_menu import*


#Definition of the booleans which will be used to navigate between menus and the game
main_menu_boolean = True
choose_menu_boolean = False
choosen_map = 0
credits_bool = False
option_bool = False

#Map pointer is a variable used to navigate and choose between the maps in the maps menu
map_pointer = 0


#The map menu function create and display the main menu of the game when the boolean "main menu boolean" is true
#It takes defined elements in "definitions_main_menu" and display them in order to create the main menu of the game
def main_menu() :

    global credits_bool
    global option_bool
    exit_game = True
    mouse_x, mouse_y = pygame.mouse.get_pos()       #Save the mouse position in the x/y plan

    screen.blit(main_menu_background, (0, 0))       #Display the background

    if 675 <= mouse_x <= 845 and 495 <= mouse_y < 570 :     #If the mouse position is on the start button
        screen.blit(start_button_image, (0,0))

    if 675 <= mouse_x <= 845 and 570 <= mouse_y < 635 :     #If the mouse position is on the option button
        screen.blit(option_button_image, (0, 0))

    if 675 <= mouse_x <= 845 and 635 <= mouse_y < 700 :     #If the mouse position is on the credits button
        screen.blit(credits_button_image, (0,0))

    if 1470 <= mouse_x <= 1520 and 0 <= mouse_y < 70 :     #If the mouse position is on the quit button
        screen.blit(quit_button_image, (0, 0))


    for event in pygame.event.get():        #Loop that verify if there is an event occurring

        if event.type == pygame.MOUSEBUTTONDOWN:        #If the mouse is clicked
            if start_button_rect.collidepoint(event.pos):       #If the user is clicking ON the start button

                global main_menu_boolean
                global choose_menu_boolean
                main_menu_boolean = False
                choose_menu_boolean = True
                return exit_game, main_menu_boolean, choose_menu_boolean, choosen_map       #If the start button is clicked, the menu changes

            if option_button_rect.collidepoint(event.pos):      #If the user is clicking ON the start button
                option_bool = True

            if credits_button_rect.collidepoint(event.pos):     #If the user is clicking ON the credits button
                credits_bool = True
                option_bool = False

            if quit_button_rect.collidepoint(event.pos):        #If the user is clicking ON the option button
                exit_game = False

            if credits_exit_rect.collidepoint(event.pos) :
                credits_bool = False

            if options_exit_rect.collidepoint(event.pos) :
                option_bool = False

    if credits_bool :
        screen.blit(credits, (0,0))

    if option_bool and not credits_bool :
        screen.blit(options, (0,0))

    return exit_game, main_menu_boolean, choose_menu_boolean, choosen_map        #Return the values of the different booleans used to navigate between menus


#The choose menu function create and display the choose menu when the boolean "choose menu boolean" is true
#It takes defined elements in "definitions_choose_menu" and display them in order to create the choose menu of the game
def choose_map_menu() :

    exit_game = True
    open_game_menu = False
    mouse_x, mouse_y = pygame.mouse.get_pos()       #Save the mouse position in the x/y plan

    global map_pointer

    map_pointer = (map_pointer + 3) % 3      #Ensures map_pointer stays within [0, 1, 2]
    match map_pointer:
        case 0:
            screen.blit(choose_menu_option1, (0, 0))
        case 1:
            screen.blit(choose_menu_option2, (0, 0))
        case 2:
            screen.blit(choose_menu_option3, (0, 0))

    if 500 <= mouse_x <= 590 and 705 <= mouse_y < 745 :
        screen.blit(left_arrow_highlight, (0,0))

    if 940 <= mouse_x <= 1030 and 705 <= mouse_y < 745 :
        screen.blit(right_arrow_highlight, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if left_arrow.collidepoint(event.pos):
                map_pointer -= 1

            if right_arrow.collidepoint(event.pos):
                map_pointer += 1

            if selection_map.collidepoint(event.pos) and map_pointer == 0:
                global choose_menu_boolean
                choose_menu_boolean = False
                global choosen_map
                choosen_map = 1
                return exit_game, main_menu_boolean, choose_menu_boolean,choosen_map

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                open_game_menu = True

            if event.key == pygame.K_ESCAPE and open_game_menu == True:
                open_game_menu = False

    return exit_game, main_menu_boolean, choose_menu_boolean,choosen_map
