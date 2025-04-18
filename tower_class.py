import pygame as p
import math
import class_enemy as en
import class_projectile as pro
from class_projectile import*

active_towers = []
global time_counting
time_counting = 0

class Tower:
    def __init__(self, x, y):
        self.screen = p.display.set_mode((1540, 775))
        self.dest = (x, y)
        self.surf = p.image.load("Assets/available_tower.png")
        self.tower = p.Rect(x, y, 75, 125)
        self.built = False
        self.list_ammo = [pro.Arrow, pro.Rock, pro.Iceball, pro.FireBall, None]
        self.ammo = None
        self.range = 0
        self.attackspeed = 20
        self.last_enemy = None
        self.compteur = 0

    def trigger(self):
        global time_counting
        time_counting += 1 / len(active_towers)
        tower_pos = p.math.Vector2(self.dest)
        list_range = []
        for element in en.list_enemy:
            dist = tower_pos - element.pos
            if dist.length() <= self.range:
                list_range.append(element)

        if not list_range:
            return

        furthest_ele = list_range[0]
        for elem in list_range:
            if elem.pos[0] > furthest_ele.pos[0]:
                furthest_ele = elem

        if time_counting % self.attackspeed < 1 :
            if self.last_enemy == furthest_ele:
                self.compteur += 5
            else:
                self.compteur = 0
            projectiles.append(self.ammo(self.dest,furthest_ele, (self.last_enemy, self.compteur)))

            self.last_enemy = furthest_ele

    def draw(self):
        self.screen.blit(self.surf, self.dest)

    def archer(self):
        self.surf = p.image.load("Assets/archer_tower.png").convert_alpha()
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        self.ammo = self.list_ammo[0]
        self.screen.blit(self.surf, self.dest)
        self.range = 200
        self.attackspeed = 60

    def bomber(self):
        self.surf = p.image.load("Assets/rock_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        self.ammo = self.list_ammo[1]
        self.screen.blit(self.surf, self.dest)
        self.range = 250

    def slow(self):
        self.surf = p.image.load("Assets/ice_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        self.ammo = self.list_ammo[2]
        self.screen.blit(self.surf, self.dest)
        self.range = 250

    def fire(self):
        self.surf = p.image.load("Assets/fire_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        self.ammo = self.list_ammo[3]
        self.screen.blit(self.surf, self.dest)
        self.range = 250
        self.attackspeed = 120

    def adrien(self):
        self.surf = p.image.load("Assets/adrien_tower.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        # À gérer selon ton architecture :
        # towers_list.append(self)
        self.ammo = self.list_ammo[4]
        self.screen.blit(self.surf, self.dest)

    def supr(self):
        self.surf = p.image.load("Assets/available_tower.png")
        self.built = False
        self.ammo = None
        self.screen.blit(self.surf, self.dest)

    def upgrade(self):
        self.range += 20

# Création de tours
tower1 = Tower(105, 360)
tower2 = Tower(490, 225)
tower3 = Tower(840, 270)
tower4 = Tower(1205, 450)
tower5 = Tower(1330, 215)

def lastEnemy(tower):
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

