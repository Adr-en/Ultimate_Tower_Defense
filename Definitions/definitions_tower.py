import pygame

elandor1 = pygame.image.load("Assets/elandor1.png").convert_alpha()
elandor1 = pygame.transform.smoothscale(elandor1, (70, 110))

elandor2 = pygame.image.load("Assets/elandor2.png").convert_alpha()
elandor2 = pygame.transform.smoothscale(elandor2, (70, 110))

elandor3 = pygame.image.load("Assets/elandor3.png").convert_alpha()
elandor3 = pygame.transform.smoothscale(elandor3, (70, 110))

elandor = [elandor1, elandor2, elandor3]