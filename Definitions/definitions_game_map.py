import pygame

#Initializing window settings
screen = pygame.display.set_mode((1520, 775))
size = screen.get_size()

background_map_1 = pygame.image.load("Assets/background_level_1.jpg")
background_map_1 = pygame.transform.smoothscale(background_map_1, size)

tower_test = pygame.image.load("Assets/default_tower.png").convert_alpha()
tower_test = pygame.transform.smoothscale(tower_test, (75, 125))
tower_test_rect = tower_test.get_rect(topleft=(1400, 600))

initial_archer_card_pos = (800, 600)
card_archer = pygame.image.load("Assets/cards_archer.png").convert_alpha()
card_archer = pygame.transform.smoothscale(card_archer, (125, 175))
card_archer_rect = card_archer.get_rect(topleft=(initial_archer_card_pos[0], initial_archer_card_pos[1]))

initial_firemage_card_pos = (930,600)
card_firemage = pygame.image.load("Assets/cards_firemage.png").convert_alpha()
card_firemage = pygame.transform.smoothscale(card_firemage, (125, 175))
card_firemage_rect = card_firemage.get_rect(topleft=(initial_firemage_card_pos[0], initial_firemage_card_pos[1]))

initial_icemage_card_pos = (1060,600)
card_icemage = pygame.image.load("Assets/cards_icemage.png").convert_alpha()
card_icemage = pygame.transform.smoothscale(card_icemage, (125, 175))
card_icemage_rect = card_icemage.get_rect(topleft=(initial_icemage_card_pos[0], initial_icemage_card_pos[1]))

initial_rockshooter_card_pos = (1190,600)
card_rockshooter = pygame.image.load("Assets/cards_rockshooter.png").convert_alpha()
card_rockshooter = pygame.transform.smoothscale(card_rockshooter,(125,175))
card_rockshooter_rect = card_rockshooter.get_rect(topleft=(initial_rockshooter_card_pos[0],initial_rockshooter_card_pos[1]))