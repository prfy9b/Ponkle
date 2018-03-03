import math
import random
import pygame
import sys
from pygame.locals import *
from copy import deepcopy

pygame.init()
pygame.mixer.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
player1keys = [False, False, False, False]
player2keys = [False, False, False, False]
player1pos = [[1, 30, 1]]
player2pos = [[615, 150, 3]]
ballpos = [300, 300]
ballvel = [1, 1]
for num in range(0, 6):
    player1pos.append([player1pos[num][0], player1pos[num][1] + 17, 1])
    player2pos.append([player2pos[num][0], player2pos[num][1] - 17, 3])
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
xMAX, yMAX, xMIN, yMIN = 615, 452, 1, 1
usus, dsus, lsus, rsus = False, False, False, False
acc = [0, 0]
arrows = []
badguys = [[640, 100]]

player1 = pygame.image.load("sprites/player1.png")
player2 = pygame.image.load("sprites/player2.png")
ball = pygame.image.load("sprites/ball.png")

running = 1
exitcode = 0
while running:
    screen.fill(0)
    
    for box in player1pos:
        if(box[2] == UP):
            if(box[0] > xMAX):
                box[2] = RIGHT
                box[0] = xMAX
            elif(box[0] < xMIN):
                box[2] = LEFT
                box[0] = xMIN
        if(box[2] == LEFT):
            if(box[1] > yMAX):
                box[2] = DOWN
                box[1] = yMAX
            elif(box[1] < yMIN):
                box[2] = UP
                box[1] = yMIN
        if(box[2] == DOWN):
            if(box[0] > xMAX):
                box[2] = RIGHT
                box[0] = xMAX
            elif(box[0] < xMIN):
                box[2] = LEFT
                box[0] = xMIN
        if(box[2] == RIGHT):
            if(box[1] > yMAX):
                box[2] = DOWN
                box[1] = yMAX
            elif(box[1] < yMIN):
                box[2] = UP
                box[1] = yMIN
        screen.blit(player1, [box[0], box[1]])
    for box in player2pos:
        if(box[2] == UP):
            if(box[0] > xMAX):
                box[2] = RIGHT
                box[0] = xMAX
            elif(box[0] < xMIN):
                box[2] = LEFT
                box[0] = xMIN
        if(box[2] == LEFT):
            if(box[1] > yMAX):
                box[2] = DOWN
                box[1] = yMAX
            elif(box[1] < yMIN):
                box[2] = UP
                box[1] = yMIN
        if(box[2] == DOWN):
            if(box[0] > xMAX):
                box[2] = RIGHT
                box[0] = xMAX
            elif(box[0] < xMIN):
                box[2] = LEFT
                box[0] = xMIN
        if(box[2] == RIGHT):
            if(box[1] > yMAX):
                box[2] = DOWN
                box[1] = yMAX
            elif(box[1] < yMIN):
                box[2] = UP
                box[1] = yMIN
        screen.blit(player2, [box[0], box[1]])
    screen.blit(ball, ballpos)
    ballpos[0] += ballvel[0]
    ballpos[1] += ballvel[1]
    if(ballpos[0] > xMAX - 8 or ballpos[0] < xMIN - 10):
        ballvel[0] *= -1
    if(ballpos[1] > yMAX - 5 or ballpos[1] < yMIN - 10):
        ballvel[1] *= -1
    pygame.display.flip()

    for ev in pygame.event.get():
        if ev.type == KEYDOWN:
            if ev.key == K_w:
                player1keys[0] = True
            elif ev.key == K_a:
                player1keys[1] = True
            elif ev.key == K_s:
                player1keys[2] = True
            elif ev.key == K_d:
                player1keys[3] = True
            if ev.key == K_UP:
                player2keys[0] = True
            elif ev.key == K_LEFT:
                player2keys[1] = True
            elif ev.key == K_DOWN:
                player2keys[2] = True
            elif ev.key == K_RIGHT:
                player2keys[3] = True
        if ev.type == KEYUP:
            if ev.key == K_w:
                player1keys[0] = False
            elif ev.key == K_a:
                player1keys[1] = False
            elif ev.key == K_s:
                player1keys[2] = False
            elif ev.key == K_d:
                player1keys[3] = False
            elif ev.key == K_UP:
                player2keys[0] = False
            elif ev.key == K_LEFT:
                player2keys[1] = False
            elif ev.key == K_DOWN:
                player2keys[2] = False
            elif ev.key == K_RIGHT:
                player2keys[3] = False
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    #Checks Player #1's Key inputs
    if player1keys[0]:
        if player1pos[6][2] == LEFT:
            for box in player1pos:
                if(box[2] == LEFT):
                    box[1] -= 2
                elif(box[2] == UP):
                    box[0] += 2
        elif player1pos[0][2] == RIGHT:
            for box in player1pos:
                if(box[2] == RIGHT):
                    box[1] -= 2
                elif(box[2] == UP):
                    box[0] -= 2
    elif player1keys[2]:
        if player1pos[0][2] == LEFT:
            for box in player1pos:
                if(box[2] == LEFT):
                    box[1] += 2
                elif(box[2] == DOWN):
                    box[0] += 2
        elif player1pos[6][2] == RIGHT:
            for box in player1pos:
                if(box[2] == RIGHT):
                    box[1] += 2
                elif(box[2] == DOWN):
                    box[0] -= 2
    elif player1keys[1]:
        if player1pos[0][2] == UP:
            for box in player1pos:
                if(box[2] == UP):
                    box[0] -= 2
                elif(box[2] == LEFT):
                    box[1] += 2
        elif player1pos[6][2] == DOWN:
            for box in player1pos:
                if(box[2] == DOWN):
                    box[0] -= 2
                elif(box[2] == LEFT):
                    box[1] -= 2
    elif player1keys[3]:
        if player1pos[6][2] == UP:
            for box in player1pos:
                if(box[2] == UP):
                    box[0] += 2
                elif(box[2] == RIGHT):
                    box[1] += 2
        elif player1pos[0][2] == DOWN:
            for box in player1pos:
                if(box[2] == DOWN):
                    box[0] += 2
                elif(box[2] == RIGHT):
                    box[1] -= 2

    #Checks Player #2's key inputs
    if player2keys[0]:
        if player2pos[6][2] == LEFT:
            for box in player2pos:
                if(box[2] == LEFT):
                    box[1] -= 2
                elif(box[2] == UP):
                    box[0] += 2
        elif player2pos[0][2] == RIGHT:
            for box in player2pos:
                if(box[2] == RIGHT):
                    box[1] -= 2
                elif(box[2] == UP):
                    box[0] -= 2
    elif player2keys[2]:
        if player2pos[0][2] == LEFT:
            for box in player2pos:
                if(box[2] == LEFT):
                    box[1] += 2
                elif(box[2] == DOWN):
                    box[0] += 2
        elif player2pos[6][2] == RIGHT:
            for box in player2pos:
                if(box[2] == RIGHT):
                    box[1] += 2
                elif(box[2] == DOWN):
                    box[0] -= 2
    elif player2keys[1]:
        if player2pos[0][2] == UP:
            for box in player2pos:
                if(box[2] == UP):
                    box[0] -= 2
                elif(box[2] == LEFT):
                    box[1] += 2
        elif player2pos[6][2] == DOWN:
            for box in player2pos:
                if(box[2] == DOWN):
                    box[0] -= 2
                elif(box[2] == LEFT):
                    box[1] -= 2
    elif player2keys[3]:
        if player2pos[6][2] == UP:
            for box in player2pos:
                if(box[2] == UP):
                    box[0] += 2
                elif(box[2] == RIGHT):
                    box[1] += 2
        elif player2pos[0][2] == DOWN:
            for box in player2pos:
                if(box[2] == DOWN):
                    box[0] += 2
                elif(box[2] == RIGHT):
                    box[1] -= 2
    pygame.time.delay(6)
























    
        