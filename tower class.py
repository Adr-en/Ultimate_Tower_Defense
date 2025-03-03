import pygame as p
import time as t
class Tower : 
    def __init__(self, x,y):
        screen = p.display.set_mode((1540,800))
        self.dest = (x,y)
        self.surf = p.Surface((35,60))
        self.tower = p.Rect(x,y,35,60)
        self.surf.fill((255,255,255))
        self.built = False
        self.attack_speed = 0.5
        self.activated = False
        self.ammo = # Raphael!!!!!!!!!!!
    
    def draw(self) :
        screen.blit(self.surf, self.dest)
        p.display.update()


    def archer(self):
        self.surf.fill((222,184,135))
        self.built = True
        screen.blit(self.surf,self.dest)
    
    def bomber(self) :
        self.surf.fill((128,128,128))
        self.built = True
        screen.blit(self.surf,self.dest)

    def slow(self):
        self.surf.fill((0,206,209))
        self.built = True
        screen.blit(self.surf,self.dest)
    
    def fire(self) :
        self.surf.fill((255,69,0))
        self.built = True
        screen.blit(self.surf,self.dest)
    
    def adrien(self) :
        self.surf.fill((250,235,215))
        self.built = True
        screen.blit(self.surf,self.dest)       
    
    def supr(self):
        self.surf.fill((255,255,255))
        self.built = False
        screen.blit(self.surf,self.dest)

    def fire(self):
        while self.activated :
            t.sleep(self.attack_speed)
            #fire


tower1 = Tower(100,100)
tower2 = Tower(300,100)
tower3 = Tower(500,100)
p.init()

screen = p.display.set_mode((1540,800))
run = True
font = p.font.SysFont(None, 50)
speciality = ["A = archer", "Z = bomber", "E = slow", "R = fire", "T = adrien"]
x = 40
y = 750

for n in speciality:
    text = font.render(n, True, (255,255,255))
    temp_surface = p.Surface((text.get_width(), text.get_height()))
    temp_surface.fill((50,50,50))
    temp_surface.blit(text, (0,0))
    screen.blit(temp_surface,(x,y))
    x += text.get_width() + 30

while run :
    tower1.draw()
    tower2.draw()
    tower3.draw()

    keys = p.key.get_pressed()
    mouse_pos = (p.mouse.get_pos())
    if keys[p.K_a] :
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.archer()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built :
            tower2.archer()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built :
            tower3.archer()
    if keys[p.K_z] :
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.bomber()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built :
            tower2.bomber()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built :
            tower3.bomber()
    if keys[p.K_e] :
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.slow()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built :
            tower2.slow()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built :
            tower3.slow()

    if keys[p.K_r] :
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.fire()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built :
            tower2.fire()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built :
            tower3.fire()

    if keys[p.K_t] :
        if tower1.tower.collidepoint(mouse_pos) and not tower1.built:
            tower1.adrien()
        elif tower2.tower.collidepoint(mouse_pos) and not tower2.built :
            tower2.adrien()
        elif tower3.tower.collidepoint(mouse_pos) and not tower3.built :
            tower3.adrien()

    if keys[p.K_d] :
        if tower1.tower.collidepoint(mouse_pos) and tower1.built:
            tower1.supr()
        elif tower2.tower.collidepoint(mouse_pos) and tower2.built :
            tower2.supr()
        elif tower3.tower.collidepoint(mouse_pos) and tower3.built :
            tower3.supr()

    for event in p.event.get():
            if event.type == p.QUIT:
                 run = False
            
                 
    p.display.update()
p.quit()

