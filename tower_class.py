import pygame as p
import math
import class_enemy as en
import class_projectile as pro

class Tower:
    def __init__(self, x, y):  # definition of the class
        self.screen = p.display.set_mode((1540, 775))
        self.dest = (x, y)
        self.surf = p.image.load("Assets/available_tower.png")  # surface of the tower
        self.tower = p.Rect(x, y, 90, 180)  # the tower itself
        self.built = False  # to know if the tower is built
        self.list_ammo = [pro.Arrow,pro.Rock,pro.Iceball,pro.FireBall,None] # list of possible ammo
        self.ammo = None
        self.range = 0

    def trigger(self,last_enemy):
        """Return the furthest enemy in range of the tower
            Tower is an object of type tower
            element and ele are object of type Enemy"""
        tower_pos = p.math.Vector2(self.dest)
        list_range = [] # list of enemies in range
        for element in en.liste_ennemy: # allows us to know if there is enemies in range
            dist = tower_pos - element.pos
            dist = dist.length()
            if dist <= self.range:
                list_range.append(element)
            # this checks which enemy is the furthest
            furthest_ele = list_range[0]
            for elem in list_range:
                if furthest_ele.pos[0] < elem.pos[0]:
                    furthest_ele = elem
            self.ammo(furthest_ele.pos,self.pos,last_enemy)

    """in the main program, add a list (maybe called active_tower) and add every active tower. then in the main loop, make sure to to run through this list and trigger"""




    def draw(self):
        self.screen.blit(self.surf, self.dest)


    """definition of every type of tower"""
    def archer(self):
        self.surf = p.image.load("Assets/archer_tower.png")  # where we'll have the skin of the mob
        self.built = True # states that the tower is active
        self.ammo = self.list_ammo[0]
        self.screen.blit(self.surf, self.dest) #prints the tower
        self.range = 120

    """same patern everywhere"""
    def bomber(self):
        self.surf = p.image.load("Assets/rock_tower.png")
        self.built = True
        self.ammo = self.list_ammo[1]
        self.screen.blit(self.surf, self.dest)
        self.range = 250

    def slow(self):
        self.surf = p.image.load("Assets/ice_tower.png")
        self.built = True
        self.ammo = self.list_ammo[2]
        self.screen.blit(self.surf, self.dest)
        self.range = 120
        #self.active()

    def fire(self):
        self.surf = p.image.load("Assets/fire_tower.png")
        self.built = True
        self.ammo = self.list_ammo[3]
        self.screen.blit(self.surf, self.dest)
        self.range = 250
        #self.active()

    def adrien(self):
        self.surf = p.image.load("Assets/adrien_tower.png")
        self.built = True
        self.ammo = self.list_ammo[4]
        self.screen.blit(self.surf, self.dest)
        #self.active()
    """method to delete a tower"""
    def supr(self):
        self.surf = p.image.load("Assets/available_tower.png")
        self.built = False # states that there the emplacement is
        self.ammo = None
        self.screen.blit(self.surf, self.dest)


p.init()

tower1 = Tower(80, 260)
tower2 = Tower(410, 120)
tower3 = Tower(820, 165)
tower4 = Tower(1175,356)
tower5 = Tower(1320,150)
screen = p.display.set_mode((1520,775))
size = screen.get_size()
background = p.image.load("Assets/Level1.jpg")
background = p.transform.smoothscale(background, size)
run = True

x = 40
y = 750

def lastEnemy(tower):
    tower_pos = p.math.Vector2(tower.dest)
    list_range = []  # list of enemies in range
    for element in en.liste_ennemy:  # allows us to know if there is enemies in range
        dist = tower_pos - element.pos
        dist = dist.length()
        if dist <= tower.range:
            list_range.append(element)
        # this checks which enemy is the furthest
        furthest_ele = list_range[0]
        for elem in list_range:
            if furthest_ele.pos[0] < elem.pos[0]:
                furthest_ele = elem
    return furthest_ele

def upgrade(self):
    self.range += 20


while run:
    screen.blit(background, (0, 0))
    tower3.draw()
    tower1.draw()
    tower2.draw()
    tower4.draw()
    tower5.draw()
    p.draw.rect(screen, (0, 0, 0),p.Rect(0,20,300,40))
    keys = p.key.get_pressed()
    mouse_pos = (p.mouse.get_pos())
    if keys[p.K_a]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.archer()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.archer()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.archer()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.archer()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.archer()
    if keys[p.K_z]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.bomber()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.bomber()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.bomber()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.bomber()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.bomber()
    if keys[p.K_e]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.slow()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.slow()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.slow()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.slow()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.slow()

    if keys[p.K_r]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.fire()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.fire()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.fire()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.fire()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.fire()

    if keys[p.K_t]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.adrien()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.adrien()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.adrien()
        elif tower4.tower.collidepoint(mouse_pos) and not tower4.built:
            tower4.adrien()
        elif tower5.tower.collidepoint(mouse_pos) and not tower5.built:
            tower5.adrien()

    if keys[p.K_d]:
        if tower1.tower.collidepoint(mouse_pos) and tower1.built:
            tower1.supr()
        elif tower2.tower.collidepoint(mouse_pos) and tower2.built:
            tower2.supr()
        elif tower3.tower.collidepoint(mouse_pos) and tower3.built:
            tower3.supr()
        elif tower4.tower.collidepoint(mouse_pos) and tower4.built:
            tower4.supr()
        elif tower5.tower.collidepoint(mouse_pos) and tower5.built:
            tower5.supr()
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()
p.quit()