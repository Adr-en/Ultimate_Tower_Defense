from random import *
from pygame.math import Vector2
from menu import screen
from Definitions.definition_enemies import *
from time import time

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





class enemy:
    """Classe enemy representing the enemies trying to go trough the map, it helps with moving them, interacting with
    them manipulating each entities separatly.
    It allows to make an enemy with some personal attributes, his representation on the map, some points by which he has to pass
    , his position, the number of the points by which he is passing, the size of the image that will be used to draw him, the speed
    movements and his health."""


    def __init__(self, image, size, health_init,base_speed):
        #affichage
        self.image = image
        self.size = size

        #trajectoire
        self.waypoints = waypoints              #list of points of the trajectory
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory in the waypoint list

        self.variation = (randint(-20, 20),randint(-20, 20))
        self.base_speed = base_speed + self.variation[0] / 21
        self.speed = base_speed

        #autre
        self.health = health_init
        self.health_init =health_init


        self.chrono_slowed = 0




    def enemy_management(self):
        """Centralization of every function to make enemies work, however it is to be completed"""
        self.move()
        self.healthbar()





    def move(self):
        """Make an enemy move in function of his own speed and trajectory
           If the enemy go entirely through the map, the player lost a point of life
           Use of the Vector library to simplify calcul with coordinates:
           length() to get the distance
           normalize() to """

        self.healthbar()                        #not sur we need it here if enemy_management() works

        target = Vector2(self.waypoints[self.target_waypoint]) + self.variation #represent the point of the trajectory that we target in teh form of a vector
        movement = target - self.pos                    #represent the distance between the target and the position (it's a vector)
        dist = movement.length()                        # represent the distance in the form of an integer not a vector



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
            self.die()
            ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr()






    def damaged(self, damage):
        """Allow to make an enemy take damage and make him die if necessary
        Parameter : an object of type enemy and the damage that he have to take of type integer
        Return : nothing"""

        self.health -= damage
        if self.health <= 0 :
            self.health = 0
            self.die()


    def healthbar(self):
        """Draw the healthbar and update it in function of HP left"""

        proportion = self.health / self.health_init

        healthbar = pygame.Rect(self.pos[0] - 5,self.pos[1] - 20, 75 * proportion, 10)
        color = (0,255,0)

        if proportion < 0.80 :
            color = (127,255,0)
        if proportion < 0.60 :
            color = (255,255,0)
        if proportion < 0.45 :
            color = (255,120,9)
        if proportion < 0.2 :
            color = (255,0,0)

        pygame.draw.rect(screen,color, healthbar)


        color_border = (0, 0, 0)
        border = pygame.Rect(self.pos[0] - 5, self.pos[1] - 20, 76, 11)
        pygame.draw.rect(screen, color_border, border, 1)


    def die(self):
        """Remove an object enemy from the list and give the player the associated exp and money """
        if not self in list_enemy :
            return
        list_enemy.remove(self)
        ##rajouter les thunes et l'exp??


    def slowed(self):
        self.chrono_slowed = time()







def spawn(type):
    """Make an enemy spawn and put him in the list"""

    ### load in another file to get the same image


    bad_guy = enemy(list_load[type-1], dico_type[type][1], dico_type[type][2], dico_type[type][3])
    list_enemy.append(bad_guy)



def ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr():
    #fonction de perte de HP quand un zombie passe
    return


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


def vague(nb_pelo, type):
    # pas oublier if list_enemy = [] lancer vague suivante (ds 30 sec)
    skibidi = 4
    return skibidi












""" 
Reste à faire : 

- vague
- différents enemies
-slow

"""










