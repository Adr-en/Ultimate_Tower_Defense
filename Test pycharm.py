import pygame
pygame.init()

running = True

pygame.display.set_caption('UTD - Ultimate Tower Defense') #Définit le nom de la fenetre
screen = pygame.display.set_mode((1540,800)) #Définit la taille et ouvre la fenetre
screen.fill('white') #Change the color of the screen

clock = pygame.time.Clock()
clock.tick(60)

test = pygame.image.load('test.png').convert() #Import une image mise dans le dossier en amount
test = pygame.transform.smoothscale(test, (50,50)) #Changing the size

tower = pygame.image.load('test_tower.png').convert()
tower = pygame.transform.smoothscale(tower, (100,100))

emp1 = pygame.Surface((50,50))
emp2= pygame.Surface((50,50))
emp1.fill('green')
emp2.fill('green')


pos_adrien = 0
y = 400
velocity = 0.2

while running : #Pour ouvrir la fenetre en continu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(test, (pos_adrien , y)) #Place l'image test
    screen.blit(tower, (1300, 600))

    screen.blit(emp1, (800, 600))
    screen.blit(emp2, (800, 200))

    pygame.display.flip() #ou .update(x,x) rafraichis l'écran pour afficher

    while pos_adrien <= 1490 :

        old_rect = pygame.Rect(pos_adrien, y, 50, 50)  #Store old position
        pos_adrien += velocity  # Move right
        new_rect = pygame.Rect(pos_adrien, y, 50, 50)  #New position

        screen.fill((255,255,255), old_rect) #Clear l'ancienne position
        screen.blit(test, (pos_adrien, y)) #Donne la nouvelle position
        pygame.display.flip()

pygame.quit()