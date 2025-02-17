from Definitions.definitions_main_menu import*

def main_menu() :

    exit_menu = True
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

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                exit_menu = choose_map_menu()

            if option_button_rect.collidepoint(event.pos):
                print("Option")

            if credits_button_rect.collidepoint(event.pos):
                print("Credits")

            if quit_button_rect.collidepoint(event.pos):
                exit_menu = False

    return exit_menu



def choose_map_menu() :

    exit_menu = True
    open_game_menu = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_menu = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                open_game_menu = True

            if event.key == pygame.K_ESCAPE and open_game_menu == True:
                open_game_menu = False

    print("Coucou")
    return exit_menu
