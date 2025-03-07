import pygame

#Window settings
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
size = screen.get_size()

choose_menu_option1 = pygame.image.load("Assets/Map-Options1.png")
choose_menu_option1 = pygame.transform.smoothscale(choose_menu_option1, size)

choose_menu_option2 = pygame.image.load("Assets/Map-Options2.png")
choose_menu_option2 = pygame.transform.smoothscale(choose_menu_option2, size)

choose_menu_option3 = pygame.image.load("Assets/Map-Options3.png")
choose_menu_option3 = pygame.transform.smoothscale(choose_menu_option3, size)

left_arrow_highlight = pygame.image.load("Assets/Left_Arrow_highlighted.png")
left_arrow_highlight = pygame.transform.smoothscale(left_arrow_highlight, size)
left_arrow = pygame.Surface((100, 50))
left_arrow = left_arrow.get_rect(topleft=(525, 815))

right_arrow_highlight = pygame.image.load("Assets/Right_Arrow_highlighted.png")
right_arrow_highlight = pygame.transform.smoothscale(right_arrow_highlight, size)
right_arrow = pygame.Surface((100, 50))
right_arrow = right_arrow.get_rect(topleft=(985, 815))