import pygame
import random

pygame.init()
chick_positions=[(650,50),(700,100),(650,150),(700,200)]
screen=pygame.display.set_mode((800,700))
# icon and caption
pygame.display.set_caption('poulterer')
icon=pygame.image.load('001-chicken.png')
# chick
chicks=[pygame.image.load('001-chickenimg.png')]*4
chickX=900
chickY=100
# player
playerImg=pygame.image.load('001-man.png')
playerX=370
playerY=520
playerX_change=0
# enemy
enemyImg=pygame.image.load('001-fox.png')
enemyX=random.randint(10,600)
enemyY=random.randint(50,200)
enemyX_change=0.5
enemyY_change=0.5
# ballon throwing
ballonImg=pygame.image.load('001-water-balloons.png')
ballon_state='ready'
ballonX=playerX
ballonY=playerY-16
ballonX_change=0
ballonY_change=10
pygame.display.set_icon(icon)
def player(x,y):
    screen.blit(playerImg,(x,y))
def throw_balloons(x,y):
    global ballon_state
    ballon_state='fire'
    screen.blit(ballonImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))
running=True
while running:
    screen.fill((153,255,153))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-1
            if event.key==pygame.K_RIGHT:
                playerX_change=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.k_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0
    playerX+=playerX_change
    ballonX=playerX
    enemyX+=enemyX_change
    i=0
    for chick in chicks:
        screen.blit(chick,(chick_positions[i]))
        i+=1

    throw_balloons(ballonX+78,ballonY)
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pygame.display.update()
