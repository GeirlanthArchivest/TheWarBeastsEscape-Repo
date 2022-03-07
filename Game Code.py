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
playerimg = pygame.image.load('Assets/Graphics')

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
    #--------------------------------

    #--------------------------------
    #Update
    #--------------------------------


    #--------------------------------
    #Draw
    #--------------------------------
    #fill the background with a colour
    screen.fill((155, 155, 155))

    #Draw a solid blue circle
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)

    #Flip the display
    pygame.display.flip()
#--------------------------------
#End of game loop
#--------------------------------
pygame.quit()
