import pygame











dico_type ={                                        # dictionnary containing all different types of enemies and their associated attributes
            1 : ["zombie1.png", "zombie1_frozen.png","zombie1_burned.png",(50,50), 100,1,3, 10],         # number of the type : image, size, health, speed, money
            2 : ["zombie2.png", "zombie2_frozen.png","zombie2_burned.png",(70,70), 400, 1,100, 5, 30],
            3 : ["zombie3.png", "zombie3_frozen.png","zombie3_burned.png",(10,10), 400, 1,100, 7, 30],
            4 : ["zombie4.png", "zombie4_frozen.png","zombie4_burned.png",(60,60), 400, 1,100, 9, 50],
            5 : ["zombie5.png", "zombie5_frozen.png","zombie5_burned.png",(80,80), 400, 1,100, 15, 100],
            6 : ["zombie6.png", "zombie6_frozen.png","zombie6_burned.png",(100,100), 400, 1,100, 15, 100],
            7 : ["soldier1.png", "soldier1_frozen.png", "soldier1_burned.png", (100, 100), 400, 1, 100, 15, 100],
            8 : ["soldier2.png", "soldier2_frozen.png", "soldier2_burned.png", (100, 100), 400, 1, 100, 15, 100],
            9 : ["boss.png", "boss_frozen.png", "boss_burned.png", (100, 100), 400, 1, 100, 15, 100],
           }





enemy_py_1_1 = pygame.image.load(dico_type[1][0][0]).convert_alpha()
enemy_py_1_1 = pygame.transform.smoothscale(enemy_py_1_1, dico_type[1][1])  # Resize image
enemy_py_1_1.set_colorkey((0, 0, 0))

enemy_py_1_2= pygame.image.load(dico_type[1][0][1]).convert_alpha()
enemy_py_1_2= pygame.transform.smoothscale(enemy_py_1_2, dico_type[1][1])  # Resize image
enemy_py_1_2.set_colorkey((0, 0, 0))

enemy_py_1_3= pygame.image.load(dico_type[1][0][2]).convert_alpha()
enemy_py_1_3= pygame.transform.smoothscale(enemy_py_1_3, dico_type[1][1])  # Resize image
enemy_py_1_3.set_colorkey((0, 0, 0))





enemy_py_2_1 = pygame.image.load(dico_type[2][0][0]).convert_alpha()
enemy_py_2_1 = pygame.transform.smoothscale(enemy_py_2_1, dico_type[2][1])  # Resize image
enemy_py_2_1.set_colorkey((0, 0, 0))

enemy_py_2_2 = pygame.image.load(dico_type[2][0][1]).convert_alpha()
enemy_py_2_2 = pygame.transform.smoothscale(enemy_py_2_2, dico_type[2][1])  # Resize image
enemy_py_2_2.set_colorkey((0, 0, 0))

enemy_py_2_3 = pygame.image.load(dico_type[2][0][2]).convert_alpha()
enemy_py_2_3 = pygame.transform.smoothscale(enemy_py_2_3, dico_type[2][1])  # Resize image
enemy_py_2_3.set_colorkey((0, 0, 0))

animation2 = [enemy_py_2_1, enemy_py_2_2, enemy_py_2_3]



enemy_py_3_1 = pygame.image.load(dico_type[3][0][0]).convert_alpha()
enemy_py_3_1 = pygame.transform.smoothscale(enemy_py_3_1, dico_type[2][1])  # Resize image
enemy_py_3_1.set_colorkey((0, 0, 0))

enemy_py_3_2 = pygame.image.load(dico_type[3][0][1]).convert_alpha()
enemy_py_3_2 = pygame.transform.smoothscale(enemy_py_3_2, dico_type[2][1])  # Resize image
enemy_py_3_2.set_colorkey((0, 0, 0))

enemy_py_3_3 = pygame.image.load(dico_type[3][0][2]).convert_alpha()
enemy_py_3_3 = pygame.transform.smoothscale(enemy_py_3_3, dico_type[2][1])  # Resize image
enemy_py_3_3.set_colorkey((0, 0, 0))

animation3 = [enemy_py_3_1, enemy_py_3_2, enemy_py_3_3]


enemy_py_4_1 = pygame.image.load(dico_type[4][0][0]).convert_alpha()
enemy_py_4_1 = pygame.transform.smoothscale(enemy_py_4_1, dico_type[2][1])  # Resize image
enemy_py_4_1.set_colorkey((0, 0, 0))

enemy_py_4_2 = pygame.image.load(dico_type[4][0][1]).convert_alpha()
enemy_py_4_2 = pygame.transform.smoothscale(enemy_py_4_2, dico_type[2][1])  # Resize image
enemy_py_4_2.set_colorkey((0, 0, 0))

enemy_py_4_3 = pygame.image.load(dico_type[4][0][2]).convert_alpha()
enemy_py_4_3 = pygame.transform.smoothscale(enemy_py_4_3, dico_type[2][1])  # Resize image
enemy_py_4_3.set_colorkey((0, 0, 0))

animation4 = [enemy_py_4_1, enemy_py_4_2, enemy_py_4_3]


enemy_py_5_1 = pygame.image.load(dico_type[5][0][0]).convert_alpha()
enemy_py_5_1 = pygame.transform.smoothscale(enemy_py_5_1, dico_type[5][1])  # Resize image
enemy_py_5_1.set_colorkey((0, 0, 0))

enemy_py_5_2 = pygame.image.load(dico_type[5][0][1]).convert_alpha()
enemy_py_5_2 = pygame.transform.smoothscale(enemy_py_5_2, dico_type[5][1])  # Resize image
enemy_py_5_2.set_colorkey((0, 0, 0))

enemy_py_5_3 = pygame.image.load(dico_type[5][0][2]).convert_alpha()
enemy_py_5_3 = pygame.transform.smoothscale(enemy_py_5_3, dico_type[5][1])  # Resize image
enemy_py_5_3.set_colorkey((0, 0, 0))

animation5 = [enemy_py_5_1, enemy_py_5_2, enemy_py_5_3]


enemy_py_6_1 = pygame.image.load(dico_type[5][0][0]).convert_alpha()
enemy_py_6_1 = pygame.transform.smoothscale(enemy_py_6_1, dico_type[5][1])  # Resize image
enemy_py_6_1.set_colorkey((0, 0, 0))

enemy_py_6_2 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_6_2 = pygame.transform.smoothscale(enemy_py_6_2, dico_type[5][1])  # Resize image
enemy_py_6_2.set_colorkey((0, 0, 0))

enemy_py_6_3 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_6_3 = pygame.transform.smoothscale(enemy_py_6_3, dico_type[5][1])  # Resize image
enemy_py_6_3.set_colorkey((0, 0, 0))

animation6 = [enemy_py_6_1, enemy_py_6_2, enemy_py_6_3]


enemy_py_7_1 = pygame.image.load(dico_type[5][0][0]).convert_alpha()
enemy_py_7_1 = pygame.transform.smoothscale(enemy_py_7_1, dico_type[5][1])  # Resize image
enemy_py_7_1.set_colorkey((0, 0, 0))

enemy_py_7_2 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_7_2 = pygame.transform.smoothscale(enemy_py_7_2, dico_type[5][1])  # Resize image
enemy_py_7_2.set_colorkey((0, 0, 0))

enemy_py_7_3 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_7_3 = pygame.transform.smoothscale(enemy_py_7_3, dico_type[5][1])  # Resize image
enemy_py_7_3.set_colorkey((0, 0, 0))

animation7 = [enemy_py_7_1, enemy_py_7_2, enemy_py_7_3]


enemy_py_8_1 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_8_1 = pygame.transform.smoothscale(enemy_py_8_1, dico_type[5][1])  # Resize image
enemy_py_8_1.set_colorkey((0, 0, 0))

enemy_py_8_2 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_8_2 = pygame.transform.smoothscale(enemy_py_8_2, dico_type[5][1])  # Resize image
enemy_py_8_2.set_colorkey((0, 0, 0))

enemy_py_8_3 = pygame.image.load(dico_type[5][0]).convert_alpha()
enemy_py_8_3 = pygame.transform.smoothscale(enemy_py_8_3, dico_type[5][1])  # Resize image
enemy_py_8_3.set_colorkey((0, 0, 0))

animation8 = [enemy_py_8_1, enemy_py_8_2, enemy_py_8_3]



"""
list_load = [enemy_py_1, enemy_py_2, enemy_py_3, enemy_py_4, enemy_py_5]

healthbar100 =
healthbar90 =
healthbar75 =
healthbar60 =
healthbar50 =
healthbar40 =
healthbar30 =
healthbar20 =
healthbar10 =

"""