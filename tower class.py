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

tower1 = Tower(110, 500)
tower2 = Tower(530, 280)
tower3 = Tower(1050, 350)
screen = p.display.set_mode((0,0),p.FULLSCREEN)
size = screen.get_size()
background = p.image.load("Assets/Level1.jpg")
background = p.transform.smoothscale(background, size)
run = True
font = p.font.SysFont(None, 50)
speciality = ["A = archer", "Z = bomber", "E = slow", "R = fire", "T = adrien"]
x = 40
y = 750 # ta grand mère

for n in speciality:
    text = font.render(n, True, (255, 255, 255))
    temp_surface = p.Surface((text.get_width(), text.get_height()))
    temp_surface.fill((50, 50, 50))
    temp_surface.blit(text, (0, 0))
    screen.blit(temp_surface, (x, y))
    x += text.get_width() + 30

while run:
    screen.blit(background, (0, 0))
    tower3.draw()
    tower1.draw()
    tower2.draw()


    keys = p.key.get_pressed()
    mouse_pos = (p.mouse.get_pos())
    if keys[p.K_a]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.archer()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.archer()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.archer()
    if keys[p.K_z]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.bomber()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.bomber()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.bomber()
    if keys[p.K_e]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.slow()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.slow()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.slow()

    if keys[p.K_r]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.fire()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.fire()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.fire()

    if keys[p.K_t]:
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.adrien()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built:
            tower2.adrien()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built:
            tower3.adrien()

    if keys[p.K_d]:
        if tower1.tower.collidepoint(mouse_pos) and tower1.built:
            tower1.supr()
        elif tower2.tower.collidepoint(mouse_pos) and tower2.built:
            tower2.supr()
        elif tower3.tower.collidepoint(mouse_pos) and tower3.built:
            tower3.supr()

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()
p.quit()