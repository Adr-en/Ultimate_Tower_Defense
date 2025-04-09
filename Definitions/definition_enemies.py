import pygame


dico_type ={                                        # dictionnary containing all different types of enemies and their associated attributes
            1 : ["Assets/zombie1.png", (50,50), 100,2],         # number of the type : image, size, health
            2 : ["Assets/zombie2.png", (70,70), 400, 1],
           }




enemy_py_1 = pygame.image.load(dico_type[1][0]).convert_alpha()
enemy_py_1 = pygame.transform.smoothscale(enemy_py_1, dico_type[1][1])  # Resize image
enemy_py_1.set_colorkey((0, 0, 0))

enemy_py_2 = pygame.image.load(dico_type[2][0]).convert_alpha()
enemy_py_2 = pygame.transform.smoothscale(enemy_py_2, dico_type[2][1])  # Resize image
enemy_py_2.set_colorkey((0, 0, 0))




list_load = [enemy_py_1, enemy_py_2]