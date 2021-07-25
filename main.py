import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920,1080
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE PE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()



black = (0, 0, 0)
blue = (0, 121, 150)
teal = (0, 255, 255)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
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

    Grid.Conway(off_color=white, on_color=blue, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)


    pygame.display.update()

pygame.quit()
