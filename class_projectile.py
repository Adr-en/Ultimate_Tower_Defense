import pygame
import math
import time

# Initialisation de Pygame
pygame.init()
WIDTH, HEIGHT = 1500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SRCALPHA)
clock = pygame.time.Clock()

# Constante gravité (pixels/s²)
GRAVITY = 1

# Chargement de l'image de la flèche
arrow_img = pygame.image.load("Assets/arrow.png").convert_alpha()
arrow_img = pygame.transform.scale(arrow_img, (50, 70))

fireball_img = pygame.image.load("Assets/fireball.png").convert_alpha()
fireball_img = pygame.transform.scale(fireball_img, (80, 70))

rock_img = pygame.image.load("Assets/rock.png").convert_alpha()
rock_img = pygame.transform.scale(rock_img, (80, 70))

iceball_img = pygame.image.load("Assets/arrow.png").convert_alpha()
iceball_img = pygame.transform.scale(iceball_img, (50, 70))

dot_img = pygame.image.load("Assets/ice_tower.png").convert_alpha()
dot_img = pygame.transform.scale(dot_img, (50, 50))


class Arrow:
    def __init__(self, start, enemy):
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

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * GRAVITY * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.active = True

        #others:
        self.damage = 30

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * GRAVITY * self.t ** 2

        if self.t >= self.time:
            self.active = False




    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + GRAVITY * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(arrow_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class FireBall:
    def __init__(self, start, end):
        self.x0, self.y0 = start
        self.x1, self.y1 = end

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

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * GRAVITY * 1000 * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.active = True

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * GRAVITY * 1000 * self.t ** 2

        if self.t >= self.time:
            self.active = False
            projectiles.append(Dot((self.x-50, self.y)))

    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + GRAVITY * 1000 * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(fireball_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Rock:
    def __init__(self, start, end):
        self.x0, self.y0 = start
        self.x1, self.y1 = end

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

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * GRAVITY * 2000 * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.active = True

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * GRAVITY * 2000 * self.t ** 2

        if self.t >= self.time:
            self.active = False

    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + GRAVITY * 2000 * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(rock_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Iceball:
    def __init__(self, start, end):
        self.x0, self.y0 = start
        self.x1, self.y1 = end

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

        # Calcul de vy selon la physique
        self.vy = (self.dy - 0.5 * GRAVITY * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.active = True

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * GRAVITY * self.t ** 2

        if self.t >= self.time:
            self.active = False

    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + GRAVITY * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(iceball_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Dot:
    def __init__(self, coor):
        self.coord = coor
        self.chrono = time.time()
        self.active = True
        self.damage = 10
        self.ticks = 0
        self.next_tick_time = 1
        self.t = 0

    def update(self, dt):
        self.t += dt
        if self.t >= self.next_tick_time and self.ticks < 8:

            self.ticks += 1
            self.next_tick_time += 0.5
            print(f"Tick {self.ticks}: Dot inflige {self.damage} dégâts à {self.coord}")

        if time.time() - self.chrono >= 4:
            self.active = False

        #for enemy in enemies:
          #  if self.coor

    def draw(self, surface):
        if self.active:
            surface.blit(dot_img, self.coord)




projectiles = []
#projectiles.append(Arrow((200, 500), (600, 480)))
#projectiles.append(Rock((200, 500), (200, 400)))
projectiles.append(FireBall((200, 500), (1000, 300)))
#projectiles.append(Iceball((200, 500), (600, 480)))


running = True
while running:
    dt = clock.tick(60) / 1000  # Delta time en secondes
    screen.fill((255, 255, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for element in projectiles:
        element.update(dt)
        if not element.active:
            projectiles.remove(element)
        element.draw(screen)

    # Points de repère
    #for arrow in projectiles:
      #  pygame.draw.circle(screen, (255, 0, 0), (int(arrow.x0), int(arrow.y0)), 5)
       # pygame.draw.circle(screen, (0, 128, 0), (int(arrow.x1), int(arrow.y1)), 5)

    pygame.display.flip()

pygame.quit()
