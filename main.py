import numpy as np
import pygame
import time
import grid
import random


width, height = 2560,1440
size = (width, height)

black = (0, 0, 0)
makeSchoolBlue = (0, 120, 150)
white = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("CONWAY'S GAME OF LIFE PYTHON EDITION")

scale = 30
offset = 1



Grid = grid.Grid(width,height, scale, offset)
Grid.random2dArray()

pause = False
go = True
while go:
    screen.fill(black)
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                go = False
            if event.key == pygame.K_SPACE:
                pause = not pause

    Grid.Conway(colorOne=white, colorTwo=makeSchoolBlue, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.mouseHandlr(mouseX, mouseY)


    pygame.display.update()

pygame.quit()
