import pygame as p
import class_enemy as en
import class_projectile as pro
from class_projectile import*
from Definitions.definitions_tower import*


active_towers = []
time_counting = 0


class Tower:
    def __init__(self, x, y):
        self.screen = p.display.set_mode((1540, 775)) # screen
        self.dest = (x - 5, y - 15) # position of the top left corner of the tower
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

        # division clock by the attack speed. if the reminder is = 0, the tower lunch an attack
        if time_counting % self.attspd[self.level - 1] == 0 :
            if self.last_enemy == furthest_ele:
                self.compteur += 5
            else:
                self.compteur = 0
            # append a projectile to the list of projectiles to be lunched
            projectiles.append(self.ammo(self.dest,furthest_ele, (self.last_enemy, self.compteur), self.level))
            # saves the last ennemy to be hit by the tower
            self.last_enemy = furthest_ele
            # update the time counter
        time_counting += 1

    def draw(self): # method that draws the tower
        self.screen.blit(self.surf, self.dest)

    def archer(self): # type archer
        self.level = 1
        self.surf = get_sprite_from_sheet(elandor[self.level - 1],0, 0,90,180)
        self.surf = p.transform.smoothscale(self.surf, (80, 130))

        self.built = True
        # ammo is of type arrow (<- only comment to adapt according to different ammo)
        self.ammo = self.list_ammo[0]
        self.screen.blit(self.surf, self.dest)
        self.range = 160
        self.attspd = [80, 70, 60]

        global currency
        currency.value = currency.get_value() - 100


    def bomber(self): # type bomber

        self.level = 1
        self.surf = get_sprite_from_sheet(rokhan[self.level - 1], 0, 0, 90, 180)
        self.surf = p.transform.smoothscale(self.surf, (80, 130))
        self.built = True
        global currency
        currency.value = currency.get_value() - 100
        self.ammo = self.list_ammo[1]
        self.screen.blit(self.surf, self.dest)
        self.range = 290
        self.attspd = [80, 70, 60]

    def slow(self): # type slow
        self.level = 1
        self.surf = get_sprite_from_sheet(syra[self.level - 1], 0, 0, 90, 180)
        self.surf = p.transform.smoothscale(self.surf, (80, 130))
        self.built = True
        global currency
        currency.value = currency.get_value() - 100
        self.ammo = self.list_ammo[2]
        self.screen.blit(self.surf, self.dest)
        self.range = 160
        self.attspd = [20, 18, 16]

    def fire(self): # type fire
        self.level = 1
        self.surf = get_sprite_from_sheet(maelor[self.level - 1], 0, 0, 90, 180)
        self.surf = p.transform.smoothscale(self.surf, (80, 130))
        self.built = True
        global currency
        currency.value = currency.get_value() - 100
        self.ammo = self.list_ammo[3]
        self.screen.blit(self.surf, self.dest)
        self.range = 290
        self.attspd = [100, 90, 80]

    def adrien(self):  # type adrien
        self.level = 1
        self.surf = p.image.load("Assets/hut2.png")
        self.surf = p.transform.smoothscale(self.surf, (70, 110))
        self.built = True
        global currency
        currency.value = currency.get_value() - 100
        # À gérer selon ton architecture :
        # towers_list.append(self)
        self.ammo = self.list_ammo[4]
        self.screen.blit(self.surf, self.dest)
        self.attspd = [100, 40, 30]

    def supr(self): # method that delete the tower
        self.level = 0
        global currency
        currency.value = currency.get_value() + self.value * 0.5
        self.value = 100
        if self.ammo == self.list_ammo[4]:
            # put the basic skin of the hut when not built
            self.surf = p.image.load("Assets/hut1.png.png").convert_alpha()
        else:
            self.surf = p.image.load("Assets/available_tower.png")
        self.built = False
        self.ammo = None
        # blit the new image
        self.screen.blit(self.surf, self.dest)

    def upgrade(self):
        # checks if we can update the tower
        if self.level < 3:
            # increase the level by one
            self.level += 1
            # increase the value by 20%
            self.value *= 1.2
            global currency
            # deduce the value from currency
            currency.value = currency.get_value() - 100
            # increase the range by 20
            self.range += 20

            # Détecter le type de la tour selon l'ammo
            if self.ammo == self.list_ammo[0]:  # Archer
                sprite_list = elandor
            elif self.ammo == self.list_ammo[1]:  # Bomber
                sprite_list = rokhan
            elif self.ammo == self.list_ammo[2]:  # Slow
                sprite_list = syra
            elif self.ammo == self.list_ammo[3]:  # Fire
                sprite_list = maelor
            else:
                return  # hut ou type inconnu : pas de sprite à changer

            self.surf = get_sprite_from_sheet(sprite_list[self.level - 1], 0, 0, 90, 180)
            self.surf = p.transform.smoothscale(self.surf, (80, 130))

    def spawn_bomber(self, tempura):
        # sets the attackspeed with the clock
        if tempura%self.attspd[self.level-1] == 0 :
            # append a bomber after the list of bombers
            bombers.append(Bombers(self.level))
        return

# Création de tours
tower1 = Tower(105, 360)
tower2 = Tower(490, 225)
tower3 = Tower(840, 270)
tower4 = Tower(1205, 450)
tower5 = Tower(1330, 215)
hut = Tower(280,500)

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

