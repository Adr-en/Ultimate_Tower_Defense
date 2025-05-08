import pygame

#missing the convert alpha
#resize the healthbar
#adjust the zombies





dico_type = {
    1: [pygame.image.load("Assets/zombie1.png"), pygame.image.load("Assets/zombie1_frozen.png"), pygame.image.load("Assets/zombie1_burned.png"), (50, 50), 100, 1, 3, 1],
    2: [pygame.image.load("Assets/zombie2.png"), pygame.image.load("Assets/zombie2_frozen.png"), pygame.image.load("Assets/zombie2_burned.png"), (50, 50), 100, 1, 3, 1],
    3: [pygame.image.load("Assets/zombie3.png"), pygame.image.load("Assets/zombie3_frozen.png"), pygame.image.load("Assets/zombie3_burned.png"), (50, 50), 100, 1, 3, 1],
    4: [pygame.image.load("Assets/zombie4.png"), pygame.image.load("Assets/zombie4_frozen.png"), pygame.image.load("Assets/zombie4_burned.png"), (50, 50), 100, 1, 3, 1],
    5: [pygame.image.load("Assets/zombie5.png"), pygame.image.load("Assets/zombie5_frozen.png"), pygame.image.load("Assets/zombie5_burned.png"), (100, 100), 100, 1, 3, 1],
    6: [pygame.image.load("Assets/zombie6.png"), pygame.image.load("Assets/zombie6_frozen.png"), pygame.image.load("Assets/zombie6_burned.png"), (50, 50), 100, 1, 3, 1],
    7: [pygame.image.load("Assets/soldier1.png"), pygame.image.load("Assets/soldier1.png"), pygame.image.load("Assets/soldier1_burned.png"), (50, 50), 100, 1, 3, 1],
    8: [pygame.image.load("Assets/soldier2.png"), pygame.image.load("Assets/soldier2_frozen.png"), pygame.image.load("Assets/soldier2_burned.png"), (50, 50), 100, 1, 3, 1],
    9: [pygame.image.load("Assets/boss.png"), pygame.image.load("Assets/boss_frozen.png"), pygame.image.load("Assets/boss_burned.png"), (50, 50), 100, 1, 3, 2],
}




def remove_white_background(surface, threshold=183):
    surface = surface.convert_alpha()
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            r, g, b, a = surface.get_at((x, y))
            if r > threshold and g > threshold and b > threshold:
                surface.set_at((x, y), (0, 0, 0, 0))  # rend le pixel totalement transparent
    return surface


Healthbar_image = pygame.image.load("Assets/health_ennemies.png").convert_alpha()
Healthbar_image = remove_white_background(Healthbar_image)



def get_sprite_from_sheet(sheet, row, column, sprite_width, sprite_height):
    """
    Extracts a single sprite from a sprite sheet.

    Parameters:
    - sheet (pygame.Surface): The sprite sheet.
    - row (int): The row number (starting from 0).
    - column (int): The column number (starting from 0).
    - sprite_width (int): Width of a single sprite.
    - sprite_height (int): Height of a single sprite.

    Returns:
    - pygame.Surface: The extracted sprite.
    """
    # Create a new surface with alpha for the extracted sprite
    sprite = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
    # Define the rectangle to copy
    rect = pygame.Rect(column * sprite_width, row * sprite_height, sprite_width, sprite_height)
    # Blit the corresponding part of the sheet onto the new surface
    sprite.blit(sheet, (0, 0), rect)
    return sprite