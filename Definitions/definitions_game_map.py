import pygame
pygame.font.init()

#Initializing window settings
screen = pygame.display.set_mode((1520, 775))
size = screen.get_size()
clock = pygame.time.Clock()
dt = (clock.tick(60) / 1000)

background_map_1 = pygame.image.load("Assets/background_level_1.jpg")
background_map_1 = pygame.transform.smoothscale(background_map_1, size)

coins = pygame.image.load("Assets/coins.png").convert_alpha()

initial_archer_card_pos = (850, 600)
card_archer = pygame.image.load("Assets/cards_archer.png").convert_alpha()
card_archer = pygame.transform.smoothscale(card_archer, (125, 175))
card_archer_rect = card_archer.get_rect(topleft=(initial_archer_card_pos[0], initial_archer_card_pos[1]))

initial_firemage_card_pos = (980,600)
card_firemage = pygame.image.load("Assets/cards_firemage.png").convert_alpha()
card_firemage = pygame.transform.smoothscale(card_firemage, (125, 175))
card_firemage_rect = card_firemage.get_rect(topleft=(initial_firemage_card_pos[0], initial_firemage_card_pos[1]))

initial_icemage_card_pos = (1110,600)
card_icemage = pygame.image.load("Assets/cards_icemage.png").convert_alpha()
card_icemage = pygame.transform.smoothscale(card_icemage, (125, 175))
card_icemage_rect = card_icemage.get_rect(topleft=(initial_icemage_card_pos[0], initial_icemage_card_pos[1]))

initial_rockshooter_card_pos = (1240,600)
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

buttons_surface = pygame.Surface((60,55))
play_pause_continue_button_rect = buttons_surface.get_rect(topleft=(1380,15))

play_button_selected = pygame.image.load("Assets/start_selected.png").convert_alpha()
play_button_selected = pygame.transform.smoothscale(play_button_selected, size)

continue_button = pygame.image.load("Assets/continue.png").convert_alpha()
continue_button = pygame.transform.smoothscale(continue_button, size)

pause_button = pygame.image.load("Assets/pause.png").convert_alpha()
pause_button = pygame.transform.smoothscale(pause_button, size)

font_level = pygame.font.SysFont(None,48)
dragging_card = None
game_active = False
game_paused = False
hut_built_boolean = False
button = "Start"

upgrade_panel_tower_1 = False
upgrade_panel_tower_2 = False
upgrade_panel_tower_3 = False
upgrade_panel_tower_4 = False
upgrade_panel_tower_5 = False

hut_available = pygame.image.load("Assets/hut1.png").convert_alpha()
hut_available = pygame.transform.smoothscale(hut_available, (200,200))
hut_available_rect = hut_available.get_rect(topleft=(280,500))

hut_built = pygame.image.load("Assets/hut2.png").convert_alpha()
hut_built = pygame.transform.smoothscale(hut_built, (200, 200))
hut_built_rect = hut_built.get_rect(topleft=(280,500))

initial_adriboom_card_pos = (1370, 600)
card_adriboom = pygame.image.load("Assets/cards_adriboom.png").convert_alpha()
card_adriboom = pygame.transform.smoothscale(card_adriboom, (125,175))
card_adriboom_rect = card_adriboom.get_rect(topleft=(initial_adriboom_card_pos))

tree = pygame.image.load("Assets/tree.png").convert_alpha()
tree = pygame.transform.smoothscale(tree, size)

pause_screen = pygame.image.load("Assets/pause_screen.png").convert_alpha()
pause_screen = pygame.transform.smoothscale(pause_screen, size)

pause_continue = pygame.image.load("Assets/pause_continue.png").convert_alpha()
pause_continue = pygame.transform.smoothscale(pause_continue, size)
pause_continue_surface = pygame.Surface((320,75)).convert_alpha()
pause_continue_rect = pause_continue_surface.get_rect(topleft=(600,320))

pause_menu = pygame.image.load("Assets/pause_menu.png").convert_alpha()
pause_menu = pygame.transform.smoothscale(pause_menu, size)
pause_menu_surface = pygame.Surface((320,75)).convert_alpha()
pause_menu_rect = pause_menu_surface.get_rect(topleft=(600,400))

pause_quit = pygame.image.load("Assets/pause_quit.png").convert_alpha()
pause_quit = pygame.transform.smoothscale(pause_quit, size)
pause_quit_surface = pygame.Surface((320,75)).convert_alpha()
pause_quit_rect = pause_quit_surface.get_rect(topleft=(600,490))

tutorial_button = pygame.image.load("Assets/tutorials.png").convert_alpha()
tutorial_button = pygame.transform.smoothscale(tutorial_button, size)
tutorial_button_surface = pygame.Surface((50,60)).convert_alpha()
tutorial_button_rect =tutorial_button_surface.get_rect(topleft=(1320,15))

tutorial_button_selected = pygame.image.load("Assets/tutorials_selected.png").convert_alpha()
tutorial_button_selected = pygame.transform.smoothscale(tutorial_button_selected, size)

tutorials_open = False
current_tutorial = 1

tutorials_exit = pygame.image.load("Assets/tutorials_exit.png").convert_alpha()
tutorials_exit = pygame.transform.smoothscale(tutorials_exit, size)
tutorials_exit_surface = pygame.Surface((60,60)).convert_alpha()
tutorials_exit_rect = tutorials_exit_surface.get_rect(topleft=(1310,110))

tutorials_changing = pygame.Surface((330,50)).convert_alpha()
tutorials_changing_rect = tutorials_changing.get_rect(topleft=(600,650))

tutorial_1 = pygame.image.load("Assets/tutorials1.png").convert_alpha()
tutorial_1 = pygame.transform.smoothscale(tutorial_1, size)

tutorial_2 = pygame.image.load("Assets/tutorials2.png").convert_alpha()
tutorial_2 = pygame.transform.smoothscale(tutorial_2, size)