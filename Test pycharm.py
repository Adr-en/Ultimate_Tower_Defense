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

x = 0
y = 400
velocity = 0.2

while running : #Pour ouvrir la fenetre en continu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(test, (x , y)) #Place l'image
    pygame.display.flip() #ou .update(x,x) rafraichis l'écran pour afficher

    while x <= 1490 :

        old_rect = pygame.Rect(x, y, 50, 50)  #Store old position
        x += velocity  # Move right
        new_rect = pygame.Rect(x, y, 50, 50)  #New position

        screen.fill('white', old_rect) #Clear l'ancienne position
        screen.blit(test, (x, y)) #Donne la nouvelle position
        pygame.display.flip()

pygame.quit()