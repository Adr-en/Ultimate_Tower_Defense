"""Tower class"""
import pygame as p

class Tower:
    def __init__(self, x, y):
        self.width =35
        self.height = 60
        self.dest = (x,y)
        self.surf = p.Surface((self.width, self.height))
        self.tower = p.Rect(x, y, self.width, self.height)
        self.surf.fill((0,150,75))

    def create_tower(self):
        screen.blit(self.surf, self.dest)





p.init()
screen = p.display.set_mode((1540,800))
run = True
to = Tower(50,50)

while run :
    keys = p.key.get_pressed()
    if keys[p.K_a] :
        to.create_tower()
    for event in p.event.get():
        if event.type == p.QUIT:
            run =False
    p.display.update()
p.quit()
