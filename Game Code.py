#--------------------------------
#Import Libraries
#--------------------------------
import pygame

#--------------------------------
#Initialisation and setup
#--------------------------------
#Initialise python
pygame.init()

#Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#set up some variables to use later
running = True

#set up player sprite
playerImg = pygame.image.load('Assets/Graphics/Kytal-1.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 250, 250
#--------------------------------
#Game Loop
#--------------------------------
#Run until user wants to quit

while running:

    #--------------------------------
    #Input
    #--------------------------------
    #Did the user click the close button?
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerRect = (playerRect[0]+20, playerRect[1])
            if event.key == pygame.K_LEFT:
                playerRect = (playerRect[0]-20, playerRect[1])
            if event.key == pygame.K_UP:
                playerRect = (playerRect[0], playerRect[1]-20)
            if event.key == pygame.K_DOWN:
                playerRect = (playerRect[0], playerRect[1]+20)

    #--------------------------------
    #Update
    #--------------------------------
    

    #--------------------------------
    #Draw
    #--------------------------------
    #fill the background with a colour
    screen.fill((155, 155, 155))

    #Draw Everything
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)
    screen.blit(playerImg, playerRect)

    #Flip the display
    pygame.display.flip()
#--------------------------------
#End of game loop
#--------------------------------
pygame.quit()
