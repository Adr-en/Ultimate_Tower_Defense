import pygame

#Initializing window settings
screen = pygame.display.set_mode((1520, 775))
size = screen.get_size()

background_map_1 = pygame.image.load("Assets/background_level_1.jpeg")
background_map_1 = pygame.transform.smoothscale(background_map_1, size)