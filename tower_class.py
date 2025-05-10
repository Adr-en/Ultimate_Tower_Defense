import pygame as p
import class_enemy as en
import class_projectile as pro
from class_projectile import*

active_towers = []
time_counting = 0


class Tower:
    def __init__(self, x, y):
        self.screen = p.display.set_mode((1540, 775)) # screen
        self.dest = (x, y) # position of the top left corner of the tower
        self.surf = p.image.load("Assets/available_tower.png") # image of the tower when available
        self.tower = p.Rect(x, y, 75, 125) # surface itself
        self.built = False # checks if the tower is built
        self.level = 0 # level of the tower
        self.value = 100 # value in gold
        self.list_ammo = [pro.Arrow, pro.Rock, pro.Iceball, pro.FireBall, None] # list of type of tower
        self.ammo = None # the ammo selected
        self.range = 0 # range of the tower
        self.attspd = []
        self.last_enemy = None


    def trigger(self): # method that makes the tower shoot
        tower_pos = p.math.Vector2(self.dest)
        list_range = []
        for element in en.list_enemy: # define which enemies are in range of the tower
            dist = tower_pos - element.pos
            if dist.length() <= self.range:
                list_range.append(element)

        if not list_range: # if there's no enemies in range
            return

        furthest_ele = list_range[0]
        for elem in list_range: # define which enemy is the furthest from the tower
            if elem.pos[0] > furthest_ele.pos[0]:
                furthest_ele = elem

        global time_counting

        if time_counting % self.attspd[self.level] == 0 :
            if self.last_enemy == furthest_ele:
                self.compteur += 5
            else:
                self.compteur = 0
            projectiles.append(self.ammo(self.dest,furthest_ele, (self.last_enemy, self.compteur), self.level))

            self.last_enemy = furthest_ele
        time_counting += 1

    def draw(self): # method that draws the tower
        self.screen.blit(self.surf, self.dest)

    def archer(self): # type archer
        self.level = 1
        self.surf = p.image.load("Assets/archer_tower.png").convert_alpha()
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        global currency
        currency -= self.value
        self.ammo = self.list_ammo[0]
        self.screen.blit(self.surf, self.dest)
        self.range = 120
        self.attspd = [30, 25, 20]

    def bomber(self): # type bomber

        self.level = 1
        self.surf = p.image.load("Assets/rock_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        global currency
        currency -= self.value
        self.ammo = self.list_ammo[1]
        self.screen.blit(self.surf, self.dest)
        self.range = 250
        self.attspd = [20, 30, 40]

    def slow(self): # type slow
        self.level = 1
        self.surf = p.image.load("Assets/ice_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        global currency
        currency -= self.value
        self.ammo = self.list_ammo[2]
        self.screen.blit(self.surf, self.dest)
        self.range = 120
        self.attspd = [7.5, 7.25, 7]

    def fire(self): # type fire
        self.level = 1
        self.surf = p.image.load("Assets/fire_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        global currency
        currency -= self.value
        self.ammo = self.list_ammo[3]
        self.screen.blit(self.surf, self.dest)
        self.range = 250
        self.attspd = [25, 20, 15]

    def adrien(self):  # type adrien
        self.level = 1
        self.surf = p.image.load("Assets/adrien_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        global currency
        currency -= self.value
        # À gérer selon ton architecture :
        # towers_list.append(self)
        self.ammo = self.list_ammo[4]
        self.screen.blit(self.surf, self.dest)
        self.attspd = [4, 4, 3]

    def supr(self): # method that delete the tower
        self.level = 0
        global currency
        currency += self.value * 0.5
        self.value = 100
        self.surf = p.image.load("Assets/available_tower.png")
        self.built = False
        self.ammo = None
        self.screen.blit(self.surf, self.dest)

    def upgrade(self): # method that upgrades the tower
        if self.level < 3:
            self.level += 1
            self.value *= 1.2
            global currency
            currency -= self.value
            self.range += 20


# Création de tours
tower1 = Tower(105, 360)
tower2 = Tower(490, 225)
tower3 = Tower(840, 270)
tower4 = Tower(1205, 450)
tower5 = Tower(1330, 215)

def lastEnemy(tower): # function that determines the last enemy
    tower_pos = p.math.Vector2(tower.dest)
    list_range = []
    for element in en.list_enemy:
        dist = tower_pos - element.pos
        if dist.length() <= tower.range:
            list_range.append(element)

    if not list_range:
        return None

    furthest_ele = list_range[0]
    for elem in list_range:
        if elem.pos[0] > furthest_ele.pos[0]:
            furthest_ele = elem
    return furthest_ele




