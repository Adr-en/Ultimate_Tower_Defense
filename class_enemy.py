from random import *
from time import time

from pygame.math import Vector2
from pygame.transform import scale

from Definitions.definition_enemies import *
from menu import screen

pygame.init()
currency = 0

list_enemy = []         # list of all of the enemies alive on the board

waypoints = [(-100, 260),
             (-50 , 260),
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





HP_player = 10


def Display_Hp_player():
    global HP_player
    if HP_player <= 0:
        print("Player died")

    healthbar_player = get_sprite_from_sheet(Healthbar_image, 10 - HP_player, 0, 90, 20)
    healthbar_player = pygame.transform.smoothscale(healthbar_player, (250, 45))
    screen.blit(healthbar_player,(5, 0))

    color = "black"
    if HP_player < 9: color = "black"
    font = pygame.font.SysFont(None, 20)
    score_text = font.render(str(HP_player) + " .hp", True, color)
    screen.blit(score_text, (230, 17))

#-----------------------------------------------------------------------------------#

def Coins():
    font = pygame.font.SysFont(None, 48)
    score_text = font.render(str(currency), True, "gold")  # .get()
    screen.blit(score_text, (40, 40))  # Add a gold image and put it in the middle maybe
    coin = pygame.image.load("Assets/coins.png")
    coin = pygame.transform.smoothscale(coin, (1000, 560))
    screen.blit(coin, (-8, 25))

"""

class Currency:
    \"""Class to manage the gold gain when killing enemies and ending waves\"""
    def __init__(self):
        self.value = 300  # Start with 0 currency

    def add(self, amount):
        self.value += amount

    def get(self):
        return self.value

currency = Currency()
"""

class Enemy:
    """Class enemy representing the enemies trying to go trough the map, it helps with moving them, interacting with
    them manipulating each entities separatly.
    It allows to make an enemy with some personal attributes, his representation on the map, some points by which he has to pass
    , his position, the number of the points by which he is passing, the size of the image that will be used to draw him, the speed
    movements and his health."""


    def __init__(self, base_image, image_frozen, image_burned, size, health_init,base_speed, money, dmg):
        #affichage
        self.image = base_image
        self.base_image = base_image
        self.size = size

        #trajectoire
        self.waypoints = waypoints              #list of points of the trajectory
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory in the waypoint list

        self.variation = (randint(-5, 5),randint(-5, 5))
        self.base_speed = base_speed + (self.variation[0] / 10)
        self.speed = base_speed

        #autre
        self.health = health_init
        self.health_init = health_init

        self.chrono_slowed = 0
        self.image_frozen = image_frozen
        self.image_burned = image_burned

        self.money = money
        self.dmg = dmg

        #animation
        self.chrono_animation = time()
        self.animation_col = 0
        self.animation_row = 1


        self.base_image.set_colorkey((113, 107, 104))
        self.image_frozen.set_colorkey((113, 107, 104))

    def enemy_management(self):
        """Centralization of every function to make enemies work, however it is to be completed"""
        self.move()
        self.healthbar_zombie()
        #screen.blit(self.image, self.pos)



    def move(self):
        """Make an enemy move in function of his own speed and trajectory
           If the enemy go entirely through the map, the player lost a point of life
           Use of the Vector library to simplify calcul with coordinates:
           length() to get the distance
           normalize() to """

        target = Vector2(self.waypoints[self.target_waypoint]) + self.variation #represent the point of the trajectory that we target in teh form of a vector
        movement = target - self.pos                    #represent the distance between the target and the position (it's a vector)
        dist = movement.length()                        # represent the distance in the form of an integer not a vector


        if movement[1] > 10:
            self.animation_row = 0
        elif movement[1] < -10:
            self.animation_row = 2
        else :
            self.animation_row = 1



        self.speed = self.base_speed
        if time() - self.chrono_slowed < 2:
            self.speed = self.base_speed / 2
            self.image = self.image_frozen
        else :
            self.image = self.base_image

        self.animation()
        image = get_sprite_from_sheet(self.image , self.animation_row, self.animation_col, 90, 120)

        screen.blit(image, self.pos)

        #Management of speed in function of the chrono




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

        #currency.add(self.money)
        global currency
        currency += self.money
        if self in list_enemy :
            list_enemy.remove(self)

        return

    def slowed(self):
        self.chrono_slowed = time()


    def ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr(self):
        global HP_player
        HP_player -= self.dmg
        list_enemy.remove(self)
        return

        #self.variation = (randint(-20, 20),randint(-20, 20))
        #self.speed = 30


    def animation(self):

        if time() - self.chrono_animation > 0.7:

            self.chrono_animation = time()
            self.animation_col += 1

            if self.animation_col > 3:
                self.animation_col = 0


def spawn(type):
    """Make an enemy spawn and put him in the list"""

    data = dico_type[type]
    bad_guy = Enemy(
        data[0],        # normal sprite (AnimateSprite)
        data[1],        # frozen sprite (AnimateSprite)
        data[2],        # burned sprite (AnimateSprite)
        data[3],        # size (tuple)
        data[4],        # health (int)
        data[5],        # speed  (int)
        data[6],        # money reward
        data[7],        # additional value (e.g. damage or level)
    )
    list_enemy.append(bad_guy)



def wave(tempura):


    if 2000> tempura > 10 :
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














"""



bomber_img = pygame.image.load("Assets/Quit_button.png").convert_alpha()
bomber_img = pygame.transform.scale(bomber_img, (50, 70))

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

        def move(self):

            target = Vector2(self.waypoints[
                                 self.target_waypoint]) + self.variation  # represent the point of the trajectory that we target in teh form of a vector
            movement = target - self.pos  # represent the distance between the target and the position (it's a vector)
            dist = movement.length()  # represent the distance in the form of an integer not a vector

            if dist >= self.speed:
                self.pos += movement.normalize() * self.speed

            else:
                if dist != 0:
                    self.pos += movement.normalize() * dist
                else:
                    self.target_waypoint += 1

            if self.target_waypoint >= len(
                    self.waypoints):  # if the enemy attain his last target point he disappear and make the player lose a life
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
            if not self.active:
                return

            rect = bomber_img.get_rect(center=(self.pos[0], self.pos[1]))
            surface.blit(bomber_img, rect.topleft)

            self.pos = Vector2(self.waypoints[0])
            self.target_waypoint = 1  # position of the actual point of the trajectory in the waypoint list


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






