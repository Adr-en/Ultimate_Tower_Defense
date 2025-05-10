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

rock_img = pygame.image.load("Assets/rock.png").convert_alpha()
rock_im = pygame.transform.smoothscale(rock_img, (80, 70))

iceball_img = pygame.image.load("Assets/iceball.png").convert_alpha()
iceball_img = pygame.transform.scale(iceball_img, (50, 70))

dot1_img = pygame.image.load("Assets/placement_spell.png").convert_alpha()
dot1_img = pygame.transform.scale(dot1_img, (150, 150))
dot1_img.set_alpha(128)

dot2_img = pygame.image.load("Assets/placement_spell_effects.png").convert_alpha()
dot2_img = pygame.transform.scale(dot2_img, (150, 150))
dot2_img.set_alpha(128)


class Arrow:
    def __init__(self, start, enemy, unused, level):
        #As the tower always give 3 arguments because of the rock tower, we leave the third one empty
        #We get the starting positions, and the ending position where the enemy is located
        self.x0, self.y0 = start[0]+50, start[1]+25
        self.x1, self.y1 = enemy.pos + Vector2(enemy.size)//2
        #We also adjust it to get the coordinates of the center of the images of the ennemies as by default we get the topleft coordinates


        #We calculate the distance that our projectile will travel on the x axis
        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)


        min_t = 0.01  # As we need to see an arrow even when the enemy is very close to the tower (=short distance to travel)
                      # ,we set a minimum travel time for our projectiles so the user can see them
        max_vx = 800   # We also set a maximum travel speed as if the arrow is too fast, the user can't see it as well

        #We calculate vx depending to distance_x, which cannot exceed max_vx
        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

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

        #We calculated in self.time the total time our arrow will take to reach its target.
        #Doing so, self.t will be like a clock, used to know when we reach self.time (so when our arrow will reach its final position)
        self.t = 0

        #We get the enemy so we call its functions defined in the class Enemy to deal him damage, slow him etc
        self.enemy = enemy

        #self.active will be used to know which projectiles has complete its job : every projectile in the projectiles list is removed
        #from the list if self.active = False, so it allows us to have a smaller list (= less iterations every time).
        #Without it, there would have hundreds of elements in the projectiles list making the game eventually lag
        self.active = True
        self.damage = [30, 40, 50]
        self.level = level

    def update(self, dt):
        if not self.active:
            return None

        #We iterate self.t for each call of update(dt), and so on until it reaches self.time (<=> the projectile has reached its final position)
        self.t += dt

        #We calculate x and y using physics
        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        #If the projectile has reached its final position, we can damage the enemy and set self.active to False, waiting for the projectile to be removed from the list
        if self.t >= self.time:
            self.enemy.damaged(self.damage[self.level])
            self.active = False




    def draw(self, surface):
        if not self.active:
            return None

        # We compute the instantaneous vertical velocity to get the current direction of motion,
        # so the arrow can be rotated to follow its trajectory realistically
        vy_inst = self.vy + self.gravity_factor * self.t
        # We use the math module to compute the angle of the velocity vector to rotate the arrow image :
        # Doing so, it points in the direction of its current movement
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        # We then rotate the arrow by taking into account its angle at each step of the trajectory
        rotated = pygame.transform.rotate(arrow_img, -angle)
        # This line will allow us to center the rotated arrow image on the (x, y) position :
        # without it, the arrow would appear offset during the rotation
        rect = rotated.get_rect(center=(self.x, self.y))
        #We finally use surface.blit to draw the new rotated image on the screen
        surface.blit(rotated, rect.topleft)

#As the next classes follow the same structure, I will comment about what changes between them

class FireBall:
    def __init__(self, start, enemy, unused, level):
        self.x0, self.y0 = start[0]+50, start[1]+25
        self.x1, self.y1 = enemy.pos + Vector2(enemy.size)//2

        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)

        # We adapt these variables to get a smoother trajectory depending of the type of the projectile
        min_t = 0.8
        max_vx = 200

        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        #We wanted for the fireball to have a really curved trajectory, contrary to the arrow that flies straight,
        #so we augmented the gravity for this class
        self.gravity_factor = GRAVITY*100

        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.active = True
        self.damage = [10, 15, 20]
        self.level = level

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            self.active = False
        #Contrairy to the other projectiles, the fireball doesn't deal damage itself but will instead burn the ground
        #(Dot class) to deal damage over time : it will create a Dot at its ending position
            projectiles.append(Dot((self.x-75, self.y-75), self.damage[self.level]))

    def draw(self, surface):
        if not self.active:
            return

        vy_inst = self.vy + self.gravity_factor * self.t
        angle = math.degrees(math.atan2(vy_inst, self.vx))+180

        rotated = pygame.transform.rotate(fireball_img, -angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect.topleft)

class Rock:
    def __init__(self, start, enemy, last_enemy, level):
        self.x0, self.y0 = start[0]+50, start[1]+25
        self.x1, self.y1 = enemy.pos + Vector2(enemy.size)//2

        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)

        min_t = 0.8
        max_vx = 800

        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        #We want the rock to have a really curved trajectory, more than the others projectiles
        self.gravity_factor = GRAVITY*200

        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.enemy = enemy
        self.active = True
        self.damage = [5, 10, 15]
        self.level = level

        #We use last_enemy for this class only : we wanted our rock to deal more damage each time it hits
        #the same enemy, so we needed to know who was the last enemy targeted by the tower
        self.last_enemy = last_enemy
        #We define a counter to know how many times our tower targeted this particular enemy in a row
        self.compteur = last_enemy[1]

        #To represent it better, we chose to augment the size of our rock at each hit : it is originally at (80,70),
        #and will grow by 5 at each hit
        new_size = (80 + self.compteur*5, 70 + self.compteur*5)
        #We change the size of our rock_img at each iteration
        self.rock_img = pygame.transform.smoothscale(rock_img, new_size)

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            #The damages increase at each hit, but if a new enemy is targeted, self.compteur will return to 0
            #And the damages will return to their value defined in self.damage
            self.enemy.damaged(self.damage[self.level] + self.compteur)
            print(self.damage+self.compteur)
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
    def __init__(self, start, enemy, unused, level):
        self.x0, self.y0 = start[0]+50, start[1]+25
        self.x1, self.y1 = enemy.pos + Vector2(enemy.size)//2

        self.dx = self.x1 - self.x0
        self.dy = self.y1 - self.y0

        distance_x = abs(self.dx)

        min_t = 0.1
        max_vx = 800

        raw_vx = distance_x / min_t if min_t > 0 else max_vx
        self.vx = min(raw_vx, max_vx) * (1 if self.dx >= 0 else -1)

        self.time = abs(self.dx) / abs(self.vx) if self.vx != 0 else 1

        self.gravity_factor = GRAVITY

        self.vy = (self.dy - 0.5 * self.gravity_factor * self.time ** 2) / self.time

        self.x = self.x0
        self.y = self.y0
        self.t = 0
        self.enemy = enemy
        self.damage = [5, 10, 15]
        self.level = level
        self.active = True

    def update(self, dt):
        if not self.active:
            return None

        self.t += dt

        self.x = self.x0 + self.vx * self.t
        self.y = self.y0 + self.vy * self.t + 0.5 * self.gravity_factor * self.t ** 2

        if self.t >= self.time:
            self.enemy.damaged(self.damage[self.level])
            #We will call the slow function defined in the Enemy class to slow the enemy for two seconds
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
    def __init__(self, coor, damage):
        self.coord = coor
        #We define a chronometer using the time module as we want our Dot to appear exactly 4 seconds
        self.chrono = time()
        self.active = True
        self.damage = damage
        #During the time our dot is active, it will deal damage 8 times every 0.5 seconds,
        #so we use self.ticks to know how much time we deal damage
        self.ticks = 0
        #We define a second instance related to the ticks, to deal the damages every 0.5 seconds
        self.next_tick_time = 0
        self.t = 0
        #We save the current asset that we will be displayed on the screen, so we can change it later to make an animation
        self.current_dot = dot1_img

    def update(self, dt):
        self.t += dt
        #If it's been 0.5 seconds since the last tick and it is not the eight tick
        if self.t >= self.next_tick_time and self.ticks < 8:

            self.ticks += 1
            self.next_tick_time += 0.5
            #We change the asset to have an animation
            if self.current_dot == dot2_img :
                self.current_dot = dot1_img
            else :
                self.current_dot = dot2_img
            #We go through the enemy list and get the coordinates of all of them
            for el in list_enemy:
                dis_enemy = math.sqrt(((el.pos[1]-el.size[1]/2) - self.coord[1])**2 + ((el.pos[0]-el.size[0]/2) - self.coord[0])**2)
                #If they are in range, we damage them
                if dis_enemy <= 75:
                    el.damaged(self.damage)
                    el.burned()

        #We deactivate the dot after 4 seconds
        if time() - self.chrono >= 4:
            self.active = False


    def draw(self, surface):
        if self.active:
            surface.blit(self.current_dot, self.coord)

#The bomber class follow the same logic than the enemy class about the movement and animation
class Bombers:
    def __init__(self, level):
        #affichage
        self.image = pygame.image.load("Assets/adriboom.png")
        self.image.set_colorkey((113, 107, 104))

        #trajectoire
        self.waypoints = waypoints[::-1]           #list of points of the trajectory
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1                # position of the actual point of the trajectory in the waypoint list
        self.speed = 2

        #animation
        self.chrono_animation = time()
        self.animation_col = 0
        self.animation_row = 1
        self.active = True
        self.damage = [30, 40, 50]
        self.level = level

    def move(self):

        target = Vector2(self.waypoints[self.target_waypoint])  # represent the point of the trajectory that we target in teh form of a vector
        movement = target - self.pos  # represent the distance between the target and the position (it's a vector)
        dist = movement.length()  # represent the distance in the form of an integer not a vector

        #We change the row of the asset to match the direction of the movement
        if movement[1] > 40:
            self.animation_row = 0
        elif movement[1] < -40:
            self.animation_row = 2
        else:
            self.animation_row = 1



        self.animation()
        image = get_sprite_from_sheet(self.image, self.animation_row, self.animation_col, 200, 200)
        image = pygame.transform.smoothscale(image, (110, 100))
        screen.blit(image, self.pos)

        # Management of speed in function of the chrono

        if dist >= self.speed:
            self.pos += movement.normalize() * self.speed

        else:
            if dist != 0:
                self.pos += movement.normalize() * dist
            else:
                self.target_waypoint += 1

        if self.target_waypoint >= len(
                self.waypoints):  # if the enemy attain his last target point he disappear and make the player lose a life
            self.active = False


    def update(self, dt):
        self.move()
        print(self.animation_row)
        print(self.animation_col)

        #We get the coordinates of each enemy in list_enemy and check its coordinates : if the distance between
        #one of them and the bomber is short enough, the bomber explodes. We get through the list a second time,
        #to deal damage to every enemy in a certain range
        for el in list_enemy:
            dis_enemy = math.sqrt(
                ((el.pos[1] - el.size[1] / 2) - self.pos[1]) ** 2 +
                ((el.pos[0] - el.size[0] / 2) - self.pos[0]) ** 2
            )
            if dis_enemy <= 70:
                for target in list_enemy:
                    dis = math.sqrt(
                        ((target.pos[1] - target.size[1] / 2) - self.pos[1]) ** 2 +
                        ((target.pos[0] - target.size[0] / 2) - self.pos[0]) ** 2
                    )
                    if dis <= 150:
                        target.damaged(self.damage[self.level])
                self.active = False
                return
    def animation(self):

        if time() - self.chrono_animation > 0.7:

            self.chrono_animation = time()
            self.animation_col += 1

            if self.animation_col > 3:
                self.animation_col = 0