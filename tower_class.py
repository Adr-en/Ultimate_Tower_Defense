import pygame as p
import time as t


class Tower:
    def __init__(self, x, y):  # definition of the class
        self.screen = p.display.set_mode((1540, 800))
        self.dest = (x, y)
        self.surf = p.image.load("Assets/default_tower.png")  # surface of the tower
        self.tower = p.Rect(x, y, 90, 180)  # the tower itself
        self.built = False  # to know if the tower is built
        self.attack_speed = 0.5  # attack speed of the tower
        #self.ammo =  # Raphael!!!!!!!!!!!

    def draw(self):
        self.screen.blit(self.surf, self.dest)
        #p.display.update()

    def archer(self):
        try:
            self.surf = p.image.load("Assets/archer_tower.png")  # where we'll have the skin of the mob
            self.built = True
            self.screen.blit(self.surf, self.dest)
        except p.error as e:
            print(e)

    def bomber(self):
        self.surf = p.image.load("Assets/rock_tower.png")
        self.built = True
        self.screen.blit(self.surf, self.dest)

    def slow(self):
        self.surf = p.image.load("Assets/ice_tower.png")
        self.built = True
        self.screen.blit(self.surf, self.dest)

    def fire(self):
        self.surf = p.image.load("Assets/fire_tower.png")
        self.built = True
        self.screen.blit(self.surf, self.dest)

    def adrien(self):
        self.surf = p.image.load("Assets/adrien_tower.png")
        self.built = True
        self.screen.blit(self.surf, self.dest)

    def supr(self):
        self.surf = p.image.load("Assets/default_tower.png")
        self.built = False
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
y = 750 # ta grand mère


while run:
    screen.blit(background, (0, 0))
    tower3.draw()
    tower1.draw()
    tower2.draw()
    tower4.draw()
    tower5.draw()

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