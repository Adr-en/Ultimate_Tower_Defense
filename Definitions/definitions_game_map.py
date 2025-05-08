import pygame

from class_projectile import clock

#Initializing window settings
screen = pygame.display.set_mode((1520, 775))
size = screen.get_size()
clock = pygame.time.Clock()
dt = (clock.tick(60) / 1000)

background_map_1 = pygame.image.load("Assets/background_level_1.jpg")
background_map_1 = pygame.transform.smoothscale(background_map_1, size)

coins = pygame.image.load("Assets/coins.png").convert_alpha()

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

tower_emp1_rect = pygame.draw.rect(screen, (255, 0, 0),(105, 360,75,125), 2)
tower_emp1_upgrade_rect = pygame.draw.rect(screen, "black", (190,365,40,50),2)
tower_emp1_delete_rect = pygame.draw.rect(screen, "black", (190,425,50,40),2)

tower_emp2_rect = pygame.draw.rect(screen, (255, 0, 0),(490, 225,75,125), 2)
tower_emp2_upgrade_rect = pygame.draw.rect(screen, "black", (575,230,40,50),2)
tower_emp2_delete_rect = pygame.draw.rect(screen, "black", (575,290,50,40),2)

tower_emp3_rect = pygame.draw.rect(screen, (255, 0, 0),(840, 270,75,125), 2)
tower_emp3_upgrade_rect = pygame.draw.rect(screen, "black", (925,275,40,50),2)
tower_emp3_delete_rect = pygame.draw.rect(screen, "black", (925,335,50,40),2)

tower_emp4_rect = pygame.draw.rect(screen, (255, 0, 0),(1205, 450,75,125), 2)
tower_emp4_upgrade_rect = pygame.draw.rect(screen, "black", (1290,455,40,50),2)
tower_emp4_delete_rect = pygame.draw.rect(screen, "black", (1290,515,50,40),2)

tower_emp5_rect = pygame.draw.rect(screen, (255, 0, 0),(1330, 215,75,125), 2)
tower_emp5_upgrade_rect = pygame.draw.rect(screen, "black", (1415,220,40,50),2)
tower_emp5_delete_rect = pygame.draw.rect(screen, "black", (1415,280,50,40),2)

upgrade_panel_gray = pygame.image.load("Assets/upgrade_gray.png").convert_alpha()
upgrade_panel_gary = pygame.transform.smoothscale(upgrade_panel_gray, (100, 150))

upgrade_panel = pygame.image.load("Assets/upgrade_button.png").convert_alpha()
upgrade_panel = pygame.transform.smoothscale(upgrade_panel, (100, 150))

play_button = pygame.image.load("Assets/start.png").convert_alpha()
play_button = pygame.transform.smoothscale(play_button, size)
play_button_rect = play_button.get_rect(topleft=(0,0))

play_button_selected = pygame.image.load("Assets/start_selected.png").convert_alpha()
play_button_selected = pygame.transform.smoothscale(play_button_selected, size)
play_button_selected_rect = play_button_selected.get_rect(topleft=(0,0))

continue_button = pygame.image.load("Assets/continue.png").convert_alpha()
continue_button = pygame.transform.smoothscale(continue_button, size)
continue_button_rect = continue_button.get_rect(topleft=(0,0))

pause_button = pygame.image.load("Assets/pause.png").convert_alpha()
pause_button = pygame.transform.smoothscale(pause_button, size)
pause_button_rect = pause_button.get_rect(topleft=(0,0))



