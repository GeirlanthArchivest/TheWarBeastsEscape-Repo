#--------------------------------
#Import Libraries
#--------------------------------
import pygame

#--------------------------------
#Initialisation and setup
#--------------------------------
#Initialise python
pygame.init()

#Set up a game clock
mainClock = pygame.time.Clock()

#Set up the drawing window
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
screen = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
pygame.display.set_caption('The War Beast Escape')

#set up some variables to use later
running = True
position = [WINDOWWIDTH /2, WINDOWHEIGHT /2]
PLAYERSIZE = 50
MOVESPEED = 200

#set up sprite
playerImg = pygame.image.load('Assets/Graphics/Kytal-1.png')
playerImg.convert()
playerRect = playerImg.get_rect()
playerRect.center = 250, 250

enemyImg = pygame.image.load('Assets/Graphics/Guard-1.png')
enemyImg.convert()
enemyRect = enemyImg.get_rect()
enemyRect.center = 250,250

foodImg = pygame.image.load('Assets/Graphics/food.png')
foodImg.convert()
foodRect = foodImg.get_rect()
foodRect.center = 300,400

syremaiImg = pygame.image.load('Assets/Graphics/Syremai.png')
syremaiImg.convert()
syremaiRect = syremaiImg.get_rect()
syremaiRect.center = 300,100

dykramaImg = pygame.image.load('Assets/Graphics/dykrama.png')
dykramaImg.convert()
dykramaRect = dykramaImg.get_rect()
dykramaRect.center = 100,200

heartImg = pygame.image.load('Assets/Graphics/heart.png')
heartImg.convert()
heartRect = heartImg.get_rect()
heartRect.center = 400,200

#Set up moveent variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
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
                moveRight = True
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_UP:
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_UP:
                moveUp = False
            if event.key == pygame.K_DOWN:
                moveDown = False

    #--------------------------------
    #Update
    #--------------------------------
    #Get the frame time
    frameMs = mainClock.tick()
    frameSec = frameMs / 1000

    if moveRight == True:
        position[0] += MOVESPEED * frameSec
    if moveLeft == True:
        position[0] -= MOVESPEED * frameSec
    if moveUp == True:
        position[1] -= MOVESPEED * frameSec
    if moveDown == True:
        position[1] += MOVESPEED * frameSec

    #Update players sprite based on position
    playerRect.left = position[0]    
    playerRect.top = position[1]
        
    #--------------------------------
    #Draw
    #--------------------------------
    #fill the background with a colour
    screen.fill((155, 155, 155))

    #Draw Everything
    pygame.draw.circle(screen, (0,0,255), (250,250), 75)
    screen.blit(playerImg, playerRect)
    screen.blit(enemyImg, enemyRect)
    screen.blit(foodImg, foodRect)
    screen.blit(syremaiImg, syremaiRect)
    screen.blit(dykramaImg, dykramaRect)
    screen.blit(heartImg, heartRect)
    
    #Flip the display
    pygame.display.flip()
#--------------------------------
#End of game loop
#--------------------------------
pygame.quit()
