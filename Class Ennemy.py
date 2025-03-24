from random import *
import pygame
from pygame.math import Vector2
import math


liste_ennemy = []                    # list of all of the ennemies alive on the board
dico_type ={                                        # dictionnary containing all different types of ennemies and their associated attributes
            1 : ["test.png", (50,50), 100],         # number of the type : image, size, health
            2 : ["test.png", (70,70), 200],
           }




class Ennemy:
    """Classe Ennemy representing the ennemies trying to go trough the map, it helps with moving them, interacting with
    them manipulating each entities separatly.
    It allows to make an ennemy with some personal attributes, his representation on the map, some points by which he has to pass
    , his position, the number of the points by which he is passing, the size of the image that will be used to draw him, the speed
    movements and his health."""


    def __init__(self, waypoints, image, size, health_init):
        self.image = image
        self.waypoints = waypoints              #liste of points of the trajectory
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory
        self.size = size
        self.speed = 5 + randint(-1,1)
        self.health = health_init
        self.health_init =health_init



    def move(self):
        """Make an ennemy move in function of his own speed and trajectory
           If the ennemy go entirely through the map, the player lost a point of life
           Use of the Vector library to simplify calcul with coordinates:
           length() to get the distance
           normalize() to """

        self.healthbar()                        #not sur we need it here
        self.health_management(0.15)            #not sur we need it here

        target = Vector2(self.waypoints[self.target_waypoint])  #represent the point of the trajectory that we target in teh form of a vector
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




    def health_management(self, damage):
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

    ennemy_py = pygame.image.load(dico_type[type][0]).convert()
    ennemy_py = pygame.transform.smoothscale(ennemy_py, dico_type[type][1])  # Resize image
    ennemy_py.set_colorkey((0, 0, 0))

    bad_guy = Ennemy(waypoints, ennemy_py, dico_type[type][1], dico_type[type][2])

    liste_ennemy.append(bad_guy)



def ahtasperdueunpointdeviegroslosersameretupulamerdemdrrrrrrrr():
    #fonction de perte de HP quand un zombie passe
    return

def projectile(self):
    """Vérifier les attribues de la classe projectile"""


    for element in liste_ennemy:
        distance = math.sqrt((projectile.pos[0] - element.pos[0])**2 + (projectile.pos[1] - element.pos[1])**2)

        if distance < projectile.zone :
            element.health_management(projectile.damage)
            if projectile.target == 1 :
                return


waypoints = [(000,400),
             (300,400),
             (300,250),
             (700,250),
             (700,500),
             (1050,500),
             (1050, 400),
             (1540, 400)
             ]




""" 
Reste à faire : 

- vague
- waypoints
- différents ennemies
- 

"""










