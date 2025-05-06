from random import *
from pygame.math import Vector2
from menu import screen
from Definitions.definition_enemies import *
from time import time
import math

pygame.init()

list_enemy = []         # list of all of the enemies alive on the board

waypoints = [(-100,310),
             (-50 ,310),
             (250,320),
             (400, 435),
             (500,485),
             (620,480),
             (670, 395),
             (710,250),
             (800,180),
             (930,220),
             (980,310),
             (1050,380),
             (1150, 400),
             (1540,400)
             ]


HP_player = 10


def Display_Hp_player():

    if HP_player <= 0:
        print("Player died")

    global HP_player
    match HP_player:
        case 10:
            healthbar_player = get_image("healthbar.png"), (0,0))
        case 9:
            # healthbar_player = get_image("zombie1.png), (0,0))
        case 8:
            # healthbar_player = get_image("zombie1.png), (0,0))

        case 7:
            # healthbar_player = get_image("healthbar.png"), (0,0))

        case 6:
            # healthbar_player = get_image("healthbar.png"), (0,0))

        case 5:
            # healthbar_player = get_image("healthbar.png"), (0,0))

        case 4:
            # healthbar_player = get_image("healthbar.png"), (0,0))

        case 3:
            # healthbar_player = get_image("healthbar.png"), (0,0))

        case 2:
            # healthbar_player = get_image("healthbar.png"), (0,0))

        case 1:
            # healthbar_player = get_image("healthbar.png"), (0,0))



    screen.blit(healthbar_player, (10, 10) )

    font = pygame.font.SysFont(None, 10)
    score_text = font.render(str(HP_player) + " .pv", True, "black")
    screen.blit(score_text, (10, 10))
#-----------------------------------------------------------------------------------#






class Currency:
    """Class to manage the gold gain when killing enemies and ending waves"""
    def __init__(self):
        self.value = 0  # Start with 0 currency

    def add(self, amount):
        self.value += amount

    def get(self):
        return self.value

currency = Currency()


class Enemy:
    """Classe enemy representing the enemies trying to go trough the map, it helps with moving them, interacting with
    them manipulating each entities separatly.
    It allows to make an enemy with some personal attributes, his representation on the map, some points by which he has to pass
    , his position, the number of the points by which he is passing, the size of the image that will be used to draw him, the speed
    movements and his health."""


    def __init__(self, image, image_frozen, image_burned, size, health_init,base_speed, money, dmg):
        #affichage
        self.image = image
        self.base_image = image
        self.size = size

        #trajectoire
        self.waypoints = waypoints              #list of points of the trajectory
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory in the waypoint list

        self.variation = (randint(-18, 18),randint(-18, 18))
        self.base_speed = base_speed + self.variation[0] / 21
        self.speed = base_speed

        #autre
        self.health = health_init
        self.health_init = health_init

        self.chrono_slowed = 0
        self.image_frozen = image_frozen

        self.image_burned = image_burned

        self.money = money
        self.dmg = dmg


    def enemy_management(self):
        """Centralization of every function to make enemies work, however it is to be completed"""
        self.move()
        self.healthbar_zombie()
        screen.blit(self.image, self.pos)



    def move(self):
        """Make an enemy move in function of his own speed and trajectory
           If the enemy go entirely through the map, the player lost a point of life
           Use of the Vector library to simplify calcul with coordinates:
           length() to get the distance
           normalize() to """

        target = Vector2(self.waypoints[self.target_waypoint]) + self.variation #represent the point of the trajectory that we target in teh form of a vector
        movement = target - self.pos                    #represent the distance between the target and the position (it's a vector)
        dist = movement.length()                        # represent the distance in the form of an integer not a vector


        if movement[1] > 0.05:
            self.image = self.animation[1]
        elif movement[1] < -0.05:
            self.image = self.animation[2]
        else :
            self.image = self.animation[0]


        #Management of speed in function of the chrono
        self.speed = self.base_speed
        if time() - self.chrono_slowed < 2:
            self.speed = self.base_speed / 2


        if dist >= self.speed :
            self.pos += movement.normalize() * self.speed

        else :
            if dist != 0 :
                self.pos += movement.normalize() * dist
            else :
                self.target_waypoint += 1


        if self.target_waypoint >= len(self.waypoints):                 #if the enemy attain his last target point he disappear and make the player lose a life
            self.ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr()


    def damaged(self, damage):
        """Allow to make an enemy take damage and make him die if necessary
        Parameter : an object of type enemy and the damage that he have to take of type integer
        Return : nothing"""


        self.health -= damage
        if self.health <= 0 :
            self.health = 0
            self.die()


    def healthbar_zombie(self):
        """Draw the healthbar and update it in function of HP left"""

        proportion = self.health / self.health_init

        healthbar = pygame.Rect(self.pos[0] - 5, self.pos[1] - 20, 75 * proportion, 10)
        color = (0, 255, 0)

        if proportion < 0.80:
            color = (127, 255, 0)
            if proportion < 0.60:
              color = (255, 255, 0)
        if proportion < 0.45:
            color = (255, 120, 9)
        if proportion < 0.2:
            color = (255, 0, 0)

        pygame.draw.rect(screen, color, healthbar)

        color_border = (0, 0, 0)
        border = pygame.Rect(self.pos[0] - 5, self.pos[1] - 20, 76, 11)
        pygame.draw.rect(screen, color_border, border, 1)

        # Player


    def die(self):
        """Remove an object enemy from the list and give the player the associated exp and money """

        currency.add(self.money)

        if not self in list_enemy :
            return currency
        list_enemy.remove(self)

        return currency

    def slowed(self):
        self.chrono_slowed = time()


    def ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr(self):
        global HP_player
        HP_player -= self.dmg
        list_enemy.remove(self)
        return

        self.variation = (randint(-20, 20),randint(-20, 20))

        self.speed = 30

    def move(self):

        target = Vector2(self.waypoints[self.target_waypoint]) + self.variation #represent the point of the trajectory that we target in teh form of a vector
        movement = target - self.pos                    #represent the distance between the target and the position (it's a vector)
        dist = movement.length()                        # represent the distance in the form of an integer not a vector







        if dist >= self.speed :
            self.pos += movement.normalize() * self.speed

        else :
            if dist != 0 :
                self.pos += movement.normalize() * dist
            else :
                self.target_waypoint += 1


        if self.target_waypoint >= len(self.waypoints):                 #if the enemy attain his last target point he disappear and make the player lose a life
            self.active = False


    def update(self, dt):
        self.move()
        for el in list_enemy:
            dis_enemy = math.sqrt(
                ((el.pos[1] - el.size[1] / 2) - self.pos[1]) ** 2 +
                ((el.pos[0] - el.size[0] / 2) - self.pos[0]) ** 2
            )
            if dis_enemy <= 35:
                for target in list_enemy:
                    dis = math.sqrt(
                        ((target.pos[1] - target.size[1] / 2) - self.pos[1]) ** 2 +
                        ((target.pos[0] - target.size[0] / 2) - self.pos[0]) ** 2
                    )
                    if dis <= 70:
                        target.damaged(self.damage)
                self.active = False
                return

    def draw(self, surface):
        if not self.active :
            return

        rect = bomber_img.get_rect(center=(self.pos[0], self.pos[1]))
        surface.blit(bomber_img, rect.topleft)


        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory in the waypoint list

def spawn(type):
    """Make an enemy spawn and put him in the list"""

    ### load in another file to get the same image


    bad_guy = Enemy(list_load[type-1], dico_type[type][1], dico_type[type][2], dico_type[type][3], dico_type[type][4], dico_type[type][5])
    list_enemy.append(bad_guy)

bomber_img = pygame.image.load("Assets/Quit_button.png").convert_alpha()
bomber_img = pygame.transform.scale(bomber_img, (50, 70))

class Bombers:
    def __init__(self):
        self.waypoints = waypoints[::-1]
        self.spawn_speed = 4
        self.active = True
        self.damage = 50



def wave(tempura):


    if 2000> tempura > 500 :
        if not (tempura%300):
            spawn(randint(1,7))


    if 4000> tempura > 2500 :
        if not (tempura%250):
            spawn(randint(1,7))


    if 6000> tempura > 4500 :
        if not (tempura%200):
            spawn(randint(1,7))


    if 8000> tempura > 6500 :
        if not (tempura%150):
            spawn(randint(1,7))


    if 10000> tempura > 8500 :
        if not (tempura%100):
            spawn(randint(1,7))


    if 12000> tempura > 10500 :
        if not (tempura%250):
            spawn(randint(1,7))
        if not (tempura%250):
            spawn(randint(7,9))


    if 14000> tempura > 12500 :
        if not (tempura%250):
            spawn(randint(1,7))
        if not (tempura%200):
            spawn(randint(7,9))

    if 14000> tempura > 12500 :
        if not (tempura%200):
            spawn(randint(1,7))
        if not (tempura%150):
            spawn(randint(7,9))

    if 14000> tempura > 12500 :
        if not (tempura%200):
            spawn(randint(1,7))
        if not (tempura%100):
            spawn(randint(7,9))

    if 14000> tempura > 12500 :
        if not (tempura%150):
            spawn(randint(1,7))
        if not (tempura%250):
            spawn(randint(7,9))

        if not (tempura%1500):
            spawn(9)

bomber_img = pygame.image.load("Assets/Quit_button.png").convert_alpha()
bomber_img = pygame.transform.scale(bomber_img, (50, 70))

class Bombers:
    def __init__(self, att1, att2, att3):
        self.waypoints = waypoints[::-1]
        self.spawn_speed = 4
        self.active = True
        self.damage = 50


        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory in the waypoint list

        self.variation = (randint(-20, 20),randint(-20, 20))

        self.speed = 30

    def move(self):

        target = Vector2(self.waypoints[self.target_waypoint]) + self.variation #represent the point of the trajectory that we target in teh form of a vector
        movement = target - self.pos                    #represent the distance between the target and the position (it's a vector)
        dist = movement.length()                        # represent the distance in the form of an integer not a vector







        if dist >= self.speed :
            self.pos += movement.normalize() * self.speed

        else :
            if dist != 0 :
                self.pos += movement.normalize() * dist
            else :
                self.target_waypoint += 1


        if self.target_waypoint >= len(self.waypoints):                 #if the enemy attain his last target point he disappear and make the player lose a life
            self.active = False


    def update(self, dt):
        self.move()
        for el in list_enemy:
            dis_enemy = math.sqrt(
                ((el.pos[1] - el.size[1] / 2) - self.pos[1]) ** 2 +
                ((el.pos[0] - el.size[0] / 2) - self.pos[0]) ** 2
            )
            if dis_enemy <= 35:
                for target in list_enemy:
                    dis = math.sqrt(
                        ((target.pos[1] - target.size[1] / 2) - self.pos[1]) ** 2 +
                        ((target.pos[0] - target.size[0] / 2) - self.pos[0]) ** 2
                    )
                    if dis <= 70:
                        target.damaged(self.damage)
                self.active = False
                return

    def draw(self, surface):
        if not self.active :
            return

        rect = bomber_img.get_rect(center=(self.pos[0], self.pos[1]))
        surface.blit(bomber_img, rect.topleft)
""" 
Reste à faire : 

- fenetre de mort du joueur
- 

"""


























    import pygame

    class AnimateSprite(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.sprite_sheet = pygame.image.load('Assets/player.png')
            self.animation_idx = 0
            self.images = {
                'down': self.get_images(0),  # separates each image by pixels (x-axis)
                'left': self.get_images(120),
                'right': self.get_images(240),
                'up': self.get_images(360)
            }
            self.current_frame = 0
            self.clock = 0  # to regulate the loop of the movement
            self.speed = 1
            self.image = self.images['down'][self.current_frame]
            self.rect = self.image.get_rect()

        def change_animation(self, name):
            if name in self.images:
                self.image = self.images[name][self.animation_idx]
                self.image.set_colorkey((60, 55, 49))  # color of the background
                self.clock += self.speed * 8

                if self.clock > 110:
                    self.animation_idx += 1
                    if self.animation_idx >= len(self.images[name]):
                        self.animation_idx = 0
                    self.clock = 0

        def get_images(self, y):
            images = []
            for i in range(0, 3):
                x = i * 90
                images.append(self.get_image(x, y))
            return images

        def get_image(self, x, y, dimension):
            image = pygame.Surface(dimension, pygame.SRCALPHA)
            image.blit(self.sprite_sheet, (0, 0), (x, y, dimension[0], dimension[1+]))
            image.set_colorkey((60, 55, 49))
            return image




