import pygame

# definir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses à faire à la création de l'entité
    def __init__(self, sprite_name): # sprite_name pour avoir tout type de sprite
        super().__init__()
        self.image = pygame.image.load(f'Assets/{sprite_name}.png')
        self.rect = self.image.get_rect()

        self.animation_idx = 0
        self.images = {
            'down': self.get_images(0), #separates each image by pixels (y-axis)
            'right': self.get_images(120),
            'up': self.get_images(240)
        }
        self.current_frame = 0
        self.clock = 0 #to regulate the loop of the movement
        self.speed = 1
        self.image = self.images['right'][self.current_frame]

    def change_animation(self, name):
        if name in self.images:
            self.image = self.images[name][self.animation_idx]
            self.image.set_colorkey((113, 107, 104))
            self.clock += self.speed*8

            if self.clock > 110:
                self.animation_idx += 1
                if self.animation_idx >= len(self.images[name]):
                    self.animation_idx = 0
                self.clock = 0

# definir une fonction pour charger les images d'un sprite
    def get_images(self, y):
        images = []
        for i in range(0, 4):
            x = i * 90
            images.append(self.get_image(x, y))
        return images

    def get_image(self, x, y):
        image = pygame.Surface((90, 120), pygame.SRCALPHA)
        image.blit(self.image, (0, 0), (x, y, 90, 120))
        image.set_colorkey((113, 107, 104))
        return image