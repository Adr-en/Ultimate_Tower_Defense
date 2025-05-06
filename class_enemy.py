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

"""
def Display_Hp_player():

    if HP_player <= 0:
        print("Player died")

    global HP_player
    match HP_player:
        case 10:
            #healthbar_player = get(image)
        case 9:
            # healthbar_player = get(image)
        case 8:

        case 7:

        case 6:

        case 5:

        case 4:

        case 3:

        case 2:

        case 1:



    screen.blit(healthbar_player, (10, 10) )

    font = pygame.font.SysFont(None, 10)
    score_text = font.render(str(HP_player) + " .pv", True, "black")
    screen.blit(score_text, (10, 10))
#-----------------------------------------------------------------------------------#

"""




class Currency:
    """Class to manage the gold gain when killing enemies and ending waves"""
    def __init__(self):
        self.value = 300  # Start with 0 currency

    def add(self, amount):
        self.value += amount

    def get(self):
        return self.value

currency = Currency()


class Enemy:
    """Class enemy representing the enemies trying to go trough the map, it helps with moving them, interacting with
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

        """
        if movement[y] > 0.05:
            self.image = self.animation[1]
        elif movement[y] < -0.05:
            self.image = self.animation[2]
        else :
            self.image = self.animation[0]
        """

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



def is_in_range(tower):
    """Return the furthest enemy in range of the tower
        Tower is an object of type tower
        element and ele are object of type enemy"""

    tower_pos = Vector2(tower.dest)
    list_range = []
    for element in list_enemy:
        dist = tower_pos - element.pos
        dist = dist.length()
        if dist <= tower.range :
            list_range.append(element)

        furthest_ele = list_range[0]
        for elem in list_range:
            if furthest_ele.pos[0] < elem.pos[0]:
                furthest_ele = elem
        return furthest_ele


def wave(tempura):
    print("tempura: ", tempura)



    wave = 0

    if 3000 > tempura >= 0 : wave = 1
    elif 5000 > tempura > 3500 : wave = 2
    elif 8000 > tempura > 5500 : wave = 3
    elif 10000 > tempura > 7500 : wave = 4
    elif 12000 > tempura > 9500 : wave = 5
    elif 14000 > tempura > 11500 : wave = 6
    elif 16000 > tempura > 13500 : wave = 7
    elif 1800 > tempura > 15500 : wave = 8
    elif 20000 > tempura > 17500 : wave = 9
    elif 22000 > tempura > 19500 : wave = 10


    match wave :
        #case 0:

        case 1:
            # 8 perso
            if tempura % 300 == 0:
               spawn(1)

        case 2:
            #12
            if tempura % 200 == 0:
               spawn(1)

        case 3:
            #24
            if tempura % 100 == 0:
                spawn(1)

        case 4:
            if tempura % 300 == 0:
                spawn(1)
            if tempura % 300 == 0:
                spawn(2)

        case 5:
            if tempura % 300 == 0:
                spawn(1)
            if tempura % 150 == 0:
                spawn(2)


        case 6:
            if tempura % 300 == 0:
                spawn(2)
            if tempura % 100 == 0:
                spawn(3)


        case 7:
            if tempura % 300 == 0:
                spawn(1)
            if tempura % 500 == 0:
                spawn(3)
            if tempura % 100 == 0:
                spawn(4)


        case 8:
            if tempura % 300 == 0:
                spawn(2)
            if tempura % 500 == 0:
                spawn(3)
            if tempura % 100 == 0:
                spawn(4)


        case 9:
            if tempura % 400 == 0:
                spawn(3)
            if tempura % 400 == 0:
                spawn(4)
            if tempura % 300 == 0:
                spawn(5)

        case 10:
            if tempura % 80 == 0:
                spawn(1)
            if tempura % 150 == 0:
                spawn(2)
            if tempura % 200 == 0:
                spawn(4)
            if tempura % 100 == 0:
                spawn(5)


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










