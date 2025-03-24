import pygame

''' 
    In this file, all necessary elements are defined and initialised in order for the main_menu function 
                        to display them to create the main menu of the game 
'''

#Initializing window settings
pygame.display.set_caption("Zombie Assault: Hopeless Resistance Against Annihilation")
screen = pygame.display.set_mode((1520, 775),0)
size = screen.get_size()
clock = pygame.time.Clock()


#Initializing the main menu background and resizing it
main_menu_background = pygame.image.load('Assets/Main_menu-background.png')
main_menu_background = pygame.transform.smoothscale(main_menu_background, size)


#Initializing the start button
start_button_image = pygame.image.load('Assets/Start_button.png')
start_button_image = pygame.transform.smoothscale(start_button_image, size)
start_button = pygame.Surface((170, 75))
start_button_rect = start_button.get_rect(topleft=(675, 495))


#Initializing the option button
option_button_image = pygame.image.load('Assets/Options_button.png')
option_button_image = pygame.transform.smoothscale(option_button_image, size)
option_button = pygame.Surface((170, 65))
option_button_rect = option_button.get_rect(topleft=(675, 570))


#Initializing the credits button
credits_button_image = pygame.image.load('Assets/Credits_button.png')
credits_button_image = pygame.transform.smoothscale(credits_button_image, size)
credits_button = pygame.Surface((170, 65))
credits_button_rect = credits_button.get_rect(topleft=(675, 635))


#Initializing the quit game button
quit_button_image = pygame.image.load('Assets/Quit_button.png')
quit_button_image = pygame.transform.smoothscale(quit_button_image, size)
quit_button = pygame.Surface((140, 70))
quit_button_rect = quit_button.get_rect(topleft=(1380, 0))