from random import *
from time import time

from pygame.math import Vector2
from Definitions.definition_enemies import *
from menu import screen


pygame.init()

def Display_Hp_player():
    """Display the healtbar and health points of the player"""
    global HP_player
    global Hp_text

    if HP_player <= 0 :
        global game_active
        game_active = False
        return True

    if HP_player < last_HP_player:
        Hp_text = font_hp.render(str(HP_player) + " .hp", True, color)

    healthbar_player = get_sprite_from_sheet(Healthbar_image, 10 - HP_player, 0, 90, 20)
    healthbar_player = pygame.transform.smoothscale(healthbar_player, (300, 54))
    screen.blit(healthbar_player,(-20, -5))
    screen.blit(Hp_text, (250, 10))

#---------------------------------------------------------------------------------------------#

def Coins():
    """Display the coins of the player"""
    global score_text

    if last_currency.get_value() > currency.get_value() or currency.get_value() > last_currency.get_value() :
        score_text = font_score.render(str(currency.value), True, "gold")

    screen.blit(score_text, (60, 45))
    screen.blit(coin, (-8, 25))

#---------------------------------------------------------------------------------------------#




class Enemy:
    """Class enemy representing the enemies trying to go through the map, it helps with moving them, interacting with
    them manipulating each entity separately.
    It allows to make an enemy with some personal attributes, his representation on the map, the references for
    his image in function of his state (normal, frozen or burned), his size, some points by which he has to pass
    , his position, the number of the points he already passed, the speedand some variable to manage it, his health etc..."""


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

        self.burned = False
        self.image_burned = image_burned

        self.money = money
        self.dmg = dmg

        #animation
        self.chrono_animation = time()
        self.animation_col = 0
        self.animation_row = 1


        self.base_image.set_colorkey((113, 107, 104))
        self.image_frozen.set_colorkey((113, 107, 104))
        self.image_burned.set_colorkey((113, 107, 104))



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

        self.animation()



        self.speed = self.base_speed

        if time() - self.chrono_slowed < 2:
            self.speed = self.base_speed / 2
            self.image = self.image_frozen
        elif self.burned :
            self.image = self.image_burned
        else :
            self.image = self.base_image




        if dist >= self.speed :
            self.pos += movement.normalize() * self.speed

        else :
            if dist != 0 :
                self.pos += movement.normalize() * dist
            else :
                self.target_waypoint += 1


        if self.target_waypoint >= len(self.waypoints):                 #if the enemy attain his last target point he disappear and make the player lose a life
            self.player_damage()



    def draw(self) :
        """Display the zombie at his position"""

        image = get_sprite_from_sheet(self.image, self.animation_row, self.animation_col, 90, 120)
        image = pygame.transform.scale(image, self.size)
        screen.blit(image, self.pos)
        self.burned = False
        self.healthbar_zombie()


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

        healthbar = pygame.Rect(self.pos[0] +5 , self.pos[1] - 20, 75 * proportion, 10)
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
        border = pygame.Rect(self.pos[0] +5 , self.pos[1] - 20, 76, 11)
        pygame.draw.rect(screen, color_border, border, 1)




    def die(self):
        """Remove an object enemy from the list and give the player the associated exp and money """


        global currency
        currency.value = currency.get_value()+ self.money
        if self in list_enemy :
            list_enemy.remove(self)

        return

    def slowed(self):
        """Put the chrono for slowed enemies at 0"""
        self.chrono_slowed = time()

    def burned(self):
        """Used to display the image of a burned zombie"""
        self.burned = True

    def player_damage(self):
        """Change the player's health point if a zombie goes through the whole map"""

        global HP_player
        HP_player -= self.dmg
        list_enemy.remove(self)
        return



    def animation(self):
        """Change images of zombies to make the walking animation"""

        if time() - self.chrono_animation > 0.7:

            self.chrono_animation = time()
            self.animation_col += 1

            if self.animation_col > 3:
                self.animation_col = 0


def spawn(type):
    """Make an enemy spawn and put him in the list"""

    data = dico_type[type]
    bad_guy = Enemy(
        data[0],        # normal sprite
        data[1],        # frozen sprite
        data[2],        # burned sprite
        data[3],        # size (tuple)
        data[4],        # health (int)
        data[5],        # speed  (int)
        data[6],        # money reward (int)
        data[7],        # damage to player (int)
    )
    list_enemy.append(bad_guy)



def wave(tempura):
    """Make zombies spawn in function of a patern"""


    if 4000> tempura :
        if tempura%10 == 0:
            spawn(randint(1,7))


    if 4000> tempura > 2500 :
        if not (tempura%150):
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