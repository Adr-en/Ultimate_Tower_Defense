import pygame

def main_menu(size,screen) :

    exit_menu = True
    (start_button_rect,option_button_rect,credits_button_rect, quit_button_rect) = definition_elements(size,screen,main_menu)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button_rect.collidepoint(event.pos):
                print("Start")

            if option_button_rect.collidepoint(event.pos):
                print("Option")

            if credits_button_rect.collidepoint(event.pos):
                print("Credits")

            if quit_button_rect.collidepoint(event.pos):
                exit_menu = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_menu = False

    if 710 <= mouse_x <= 910 and 590 <= mouse_y < 665 :
        pygame.draw.rect(screen, "lightblue", (710, 590, 200, 75), 2)

    if 710 <= mouse_x <= 910 and 665 <= mouse_y < 740 :
        pygame.draw.rect(screen, "lightblue", (710, 665, 200, 75), 2)

    if 710 <= mouse_x <= 910 and 740 <= mouse_y < 815 :
        pygame.draw.rect(screen, "lightblue", (710, 740, 200, 75), 2)

    return exit_menu


def definition_elements(size,screen,menu) :

    if menu == main_menu :
        main_menu_background = pygame.image.load('Assets/main_menu_v1.jpeg')
        main_menu_background = pygame.transform.smoothscale(main_menu_background, size)

        start_button = pygame.Surface((200, 75))
        start_button_rect = start_button.get_rect(topleft=(710, 590)) #Maybe not the same place

        option_button = pygame.Surface((200, 75))
        option_button_rect = option_button.get_rect(topleft=(710, 665))

        credits_button = pygame.Surface((200, 75))
        credits_button_rect = credits_button.get_rect(topleft=(710, 740))

        quit_button = pygame.Surface((30, 30)) #It will be an image (don't forget to smoothscale)
        quit_button_rect = quit_button.get_rect(topleft=(1560, 10))

        screen.blit(start_button,start_button_rect)
        screen.blit(option_button, option_button_rect)
        screen.blit(credits_button, credits_button_rect)
        screen.blit(quit_button, quit_button_rect)
        screen.blit(main_menu_background, (0, 0)) #MUST put the background on top of the buttons
        pygame.draw.line(screen, "red", (1560, 10), (1590, 40), 5)
        pygame.draw.line(screen, "red", (1590, 10), (1560, 40), 5)

        return start_button_rect, option_button_rect, credits_button_rect, quit_button_rect



