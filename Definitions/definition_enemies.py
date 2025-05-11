import pygame
pygame.font.init()



#______________________________Currency_____________________________________________________________#

class Currency():
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

currency = Currency(200)
last_currency = Currency(currency.value)


font_score = pygame.font.SysFont(None, 72)
coin = pygame.image.load("Assets/coins.png")
coin = pygame.transform.smoothscale(coin, (1500, 840))
score_text = font_score.render(str(currency.value), True, "gold")

#___________________________________________________________________________________________________#

HP_player = 10
last_HP_player = HP_player

list_enemy = []         # list of all of the enemies alive on the board

waypoints = [(-50 , 260),           #path point for the enemies trajectory
             (250, 280),
             (400, 395),
             (500, 445),
             (620, 440),
             (670, 355),
             (710, 220),
             (800, 140),
             (930, 180),
             (980, 270),
             (1050, 340),
             (1150, 360),
             (1540, 360)]

dico_type = {               #dico to define the differents enemies and their capacities
    1: [pygame.image.load("Assets/zombie1.png"), pygame.image.load("Assets/zombie1_frozen.png"), pygame.image.load("Assets/zombie1_burned.png"), (80, 106), 100, 1, 20, 1],
    2: [pygame.image.load("Assets/zombie2.png"), pygame.image.load("Assets/zombie2_frozen.png"), pygame.image.load("Assets/zombie2_burned.png"), (80, 106), 100, 1, 20, 1],
    3: [pygame.image.load("Assets/zombie3.png"), pygame.image.load("Assets/zombie3_frozen.png"), pygame.image.load("Assets/zombie3_burned.png"), (80, 106), 100, 1, 20, 1],
    4: [pygame.image.load("Assets/zombie4.png"), pygame.image.load("Assets/zombie4_frozen.png"), pygame.image.load("Assets/zombie4_burned.png"), (80, 106), 100, 1, 20, 1],
    5: [pygame.image.load("Assets/zombie5.png"), pygame.image.load("Assets/zombie5_frozen.png"), pygame.image.load("Assets/zombie5_burned.png"), (80, 106), 100, 1, 20, 1],
    6: [pygame.image.load("Assets/zombie6.png"), pygame.image.load("Assets/zombie6_frozen.png"), pygame.image.load("Assets/zombie6_burned.png"), (80, 106), 100, 1, 20, 1],
    7: [pygame.image.load("Assets/soldier1.png"), pygame.image.load("Assets/soldier1_frozen.png"), pygame.image.load("Assets/soldier1_burned.png"), (80, 106), 150, 1, 30, 1],
    8: [pygame.image.load("Assets/soldier2.png"), pygame.image.load("Assets/soldier2_frozen.png"), pygame.image.load("Assets/soldier2_burned.png"), (80, 106), 150, 1, 30, 1],
    9: [pygame.image.load("Assets/boss.png"), pygame.image.load("Assets/boss_frozen.png"), pygame.image.load("Assets/boss_burned.png"), (80, 106), 1000, 1, 100, 2],
}



def remove_white_background(surface, threshold_min=183):
    """get an image and return it without all the pixels of color (x,x,x) with x the threshold"""
    surface = surface.convert_alpha()
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            r, g, b, a = surface.get_at((x, y))
            if  r > threshold_min and g > threshold_min and b > threshold_min:
                surface.set_at((x, y), (0, 0, 0, 0))  # rend le pixel totalement transparent
    return surface



def get_sprite_from_sheet(sheet, row, column, sprite_width, sprite_height):
    """
    Extracts a single sprite from a sprite sheet.
    """
    # Create a new surface with alpha for the extracted sprite
    sprite = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
    # Define the rectangle to copy
    rect = pygame.Rect(column * sprite_width, row * sprite_height, sprite_width, sprite_height)
    # Blit the corresponding part of the sheet onto the new surface
    sprite.blit(sheet, (0, 0), rect)
    return sprite

#____________________________________________Definition_of_the_Player's_Healthbar___________________________________________________#
color = "black"
Healthbar_image = pygame.image.load("Assets/health_ennemies.png").convert_alpha()
Healthbar_image = remove_white_background(Healthbar_image)
font_hp = pygame.font.SysFont(None, 35)
Hp_text = font_hp.render(str(HP_player) + " .hp", True, color)