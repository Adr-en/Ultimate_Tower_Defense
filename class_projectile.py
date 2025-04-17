import pygame
import math

from class_enemy import*

projectiles = []

# Initialization
pygame.init()
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
clock = pygame.time.Clock()

# Gravity constant
GRAVITY = 9.81

# We load all our images, set the size and the transparency if necessary
arrow_img = pygame.image.load("Assets/arrow.png").convert_alpha()
arrow_img = pygame.transform.scale(arrow_img, (50, 70))

fireball_img = pygame.image.load("Assets/fireball.png").convert_alpha()
fireball_img = pygame.transform.scale(fireball_img, (80, 70))

global rock_img
rock_img = pygame.image.load("Assets/rock.png").convert_alpha()
rock_img = pygame.transform.smoothscale(rock_img, (80, 70))

iceball_img = pygame.image.load("Assets/iceball.png").convert_alpha()
iceball_img = pygame.transform.scale(iceball_img, (50, 70))

dot1_img = pygame.image.load("Assets/placement_spell.png").convert_alpha()
dot1_img = pygame.transform.scale(dot1_img, (150, 150))
dot1_img.set_alpha(128)

dot2_img = pygame.image.load("Assets/placement_spell_effects.png").convert_alpha()
dot2_img = pygame.transform.scale(dot2_img, (150, 150))
dot2_img.set_alpha(128)


class Arrow:
    def __init__(self, start, enemy, unused):
        #We get the starting positions, and the ending position where the enemy is located
        self.x0, self.y0 = start
        self.x1, self.y1 = enemy.pos + Vector2(enemy.size)//2 #(enemy.pos[0] + enemy.size[0] //2 ,enemy.pos[1]+ enemy)


        #We calculate the distance that our projectile will travel
        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)


        min_t = 0.01  # As we need to see an arrow even when the enemy is very close to the tower (=short distance to travel), we set a minimum travel time for our projectiles so the user can see them
        max_vx = 800   # We also set a maximum travel speed as if the arrow is too fast, the user can't see it as well

        #We calculate vx depending to distance_x, which cannot exceed max_vx
        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        # Recalcul du temps de vol avec vx ajusté
        # We calculate the time our projectile will take to reach it ending position considering only the horizontal axis
        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        #We adapt the gravity factor to get a smoother trajectory
        self.gravity_factor = GRAVITY*10

        # Calcul de vy selon la physique
        # We calculate then the projectile speed on the y axis, using physics
        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        # We define the coordinates that we will change for our projectile along its path
        self.x = self.x0
        self.y = self.y0

        #
        self.t = 0

        self.enemy = enemy
        self.active = True
        self.damage = 30

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            self.enemy.damaged(self.damage)
            self.active = False




    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + self.gravity_factor * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180


        rotated = pygame.transform.rotate(arrow_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class FireBall:
    def __init__(self, start, enemy, unused):
        self.x0, self.y0 = start
        self.x1, self.y1 = enemy.pos

        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)

        # Vitesse horizontale "idéale"
        min_t = 0.8  # temps minimum de vol en secondes
        max_vx = 200       # vitesse maximale autorisée

        # Calcul de vx selon la distance, mais limité par max_vx
        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        # Recalcul du temps de vol avec vx ajusté
        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        self.gravity_factor = GRAVITY

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0

        self.active = True

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            self.active = False
            projectiles.append(Dot((self.x-50, self.y)))

    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + self.gravity_factor * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(fireball_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Rock:
    def __init__(self, start, enemy, last_enemy):
        self.x0, self.y0 = start
        self.x1, self.y1 = enemy.pos

        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)

        # Vitesse horizontale "idéale"
        min_t = 0.8  # temps minimum de vol en secondes
        max_vx = 800        # vitesse maximale autorisée

        # Calcul de vx selon la distance, mais limité par max_vx
        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        # Recalcul du temps de vol avec vx ajusté
        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        self.gravity_factor = GRAVITY*100

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.enemy = enemy
        self.last_enemy = last_enemy
        self.active = True
        self.compteur = 0
        self.damage = 10
        self.rock_img = rock_img

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            if self.last_enemy != None:
                if self.enemy == self.last_enemy:
                    self.compteur += 10
                    self.rock_img = pygame.transform.smoothscale(self.rock_img, (80+self.compteur, 70+self.compteur))
                else:
                    self.compteur = 0
                    self.rock_img = pygame.transform.smoothscale(self.rock_img, (80, 70))
            self.enemy.damaged(self.damage + self.compteur)
            self.active = False


    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + self.gravity_factor * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(self.rock_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Iceball:
    def __init__(self, start, enemy, unused):
        self.x0, self.y0 = start
        self.x1, self.y1 = enemy.pos

        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)

        # Vitesse horizontale "idéale"
        min_t = 0.1  # temps minimum de vol en secondes
        max_vx = 800        # vitesse maximale autorisée

        # Calcul de vx selon la distance, mais limité par max_vx
        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        # Recalcul du temps de vol avec vx ajusté
        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        self.gravity_factor = GRAVITY

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.enemy = enemy
        self.damage = 5
        self.active = True

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            self.enemy.damaged(self.damage)

            self.enemy.slowed()
            self.active = False



    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + self.gravity_factor * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(iceball_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Dot:
    def __init__(self, coor):
        self.coord = coor
        self.chrono = time()
        self.active = True
        self.damage = 10
        self.ticks = 0
        self.next_tick_time = 1
        self.t = 0
        self.current_dot = dot1_img

    def update(self, dt):
        self.t += dt
        if self.t >= self.next_tick_time and self.ticks < 8:

            self.ticks += 1
            self.next_tick_time += 0.5
            print(f"Tick {self.ticks}: Dot inflige {self.damage} dégâts à {self.coord}")
            if self.current_dot == dot2_img :
                self.current_dot = dot1_img
            else :
                self.current_dot = dot2_img
            for el in list_enemy:
                dis_enemy = math.sqrt((el.pos[1] - self.coord[1])**2 + (el.pos[0] - self.coord[0])**2)
                if dis_enemy <= 100:
                    el.damaged(self.damage)


        if time() - self.chrono >= 4:
            self.active = False





    def draw(self, surface):
        if self.active:
            surface.blit(self.current_dot, self.coord)



