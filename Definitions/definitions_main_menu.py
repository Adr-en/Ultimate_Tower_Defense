import pygame

#Window settings
pygame.display.set_caption("Zombie Assault: Hopeless Resistance Against Annihilation")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
size = screen.get_size()
clock = pygame.time.Clock()

main_menu_background = pygame.image.load('Assets/Main_menu-background.png')
main_menu_background = pygame.transform.smoothscale(main_menu_background, size)

start_button_image = pygame.image.load('Assets/Start_button.png')
start_button_image = pygame.transform.smoothscale(start_button_image, size)
start_button = pygame.Surface((200, 75))
start_button_rect = start_button.get_rect(topleft=(705, 580))

option_button_image = pygame.image.load('Assets/Options_button.png')
option_button_image = pygame.transform.smoothscale(option_button_image, size)
option_button = pygame.Surface((200, 75))
option_button_rect = option_button.get_rect(topleft=(705, 660))

credits_button_image = pygame.image.load('Assets/Credits_button.png')
credits_button_image = pygame.transform.smoothscale(credits_button_image, size)
credits_button = pygame.Surface((200, 75))
credits_button_rect = credits_button.get_rect(topleft=(705, 735))

quit_button = pygame.Surface((130, 65))
quit_button_rect = quit_button.get_rect(topleft=(1470, 0))