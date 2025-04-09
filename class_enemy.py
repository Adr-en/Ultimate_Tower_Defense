from random import *
import pygame
from pygame.math import Vector2
from menu import screen
import math


liste_ennemy = []
 # list of all of the ennemies alive on the board
dico_type ={                                        # dictionnary containing all different types of ennemies and their associated attributes
            1 : ["Assets/zombie1.png", (50,50), 100,1],         # number of the type : image, size, health
            2 : ["Assets/zombie2.png", (70,70), 400, 1],
           }




class Ennemy:
    """Classe Ennemy representing the ennemies trying to go trough the map, it helps with moving them, interacting with
    them manipulating each entities separatly.
    It allows to make an ennemy with some personal attributes, his representation on the map, some points by which he has to pass
    , his position, the number of the points by which he is passing, the size of the image that will be used to draw him, the speed
    movements and his health."""


    def __init__(self, image, size, health_init,speed):
        #affichage
        self.image = image
        self.size = size

        #trajectoire
        self.waypoints = waypoints              #liste of points of the trajectory
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory
        self.speed = speed
        self.variation = (randint(-20, 20),randint(-20, 20))

        #autre
        self.health = health_init
        self.health_init =health_init
        self.status = ""   #integer et on fait baisser de tps en tps quand ça arrive à 0 ils ne sont plus concernés



    def move(self):
        """Make an ennemy move in function of his own speed and trajectory
           If the ennemy go entirely through the map, the player lost a point of life
           Use of the Vector library to simplify calcul with coordinates:
           length() to get the distance
           normalize() to """

        self.healthbar()                        #not sur we need it here
        self.damaged(0.15)            #not sur we need it here

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

        if self.target_waypoint >= len(self.waypoints):                 #if the ennemy attain his last target point he disappear and make the player lose a life
            self.die()
            ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr()




    def damaged(self, damage):
        """Allow to make an ennemy take damage and make him die if necessary
        Parameter : an object of type Ennemy and the damage that he have to take of type integer
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
        """Remove an object Ennemy from the list and give the player the associated exp and money """
        liste_ennemy.remove(self)
        ##rajouter les thunes et l'exp??



def spawn(type):
    """Make an ennemy spawn and put him in the list"""

    ### load in another file to get the same image

    ennemy_py = pygame.image.load(dico_type[type][0]).convert_alpha()
    ennemy_py = pygame.transform.smoothscale(ennemy_py, dico_type[type][1])  # Resize image
    ennemy_py.set_colorkey((0, 0, 0))
    current = ennemy_py



    bad_guy = Ennemy(ennemy_py, dico_type[type][1], dico_type[type][2], dico_type[type][3])

    liste_ennemy.append(bad_guy)



def ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr():
    #fonction de perte de HP quand un zombie passe
    return




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



def is_in_range(tower):
    """Return the furthest ennemy in range of the tower
        Tower is an object of type tower
        element and ele are object of type Ennemy"""

    tower_pos = Vector2(tower.dest)
    list_range = []
    for element in liste_ennemy:
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
    # pas oublier if liste_ennemy = [] lancer vague suivante (ds 30 sec)
    skibidi = 4
    return skibidi







""" 
Reste à faire : 

- vague
- waypoints
- différents ennemies
- load les images

"""










