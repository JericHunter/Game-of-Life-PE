import pygame

from grid import Grid

WIDTH, HEIGHT = 1920, 1080
SIZE = (WIDTH, HEIGHT)

BACK = (0, 0, 0)
BLUE = (0, 120, 150)
WHITE = (255, 255, 255)

TITLE = "CONWAY'S GAME OF LIFE PYTHON EDITION"

SCALE = 5
OFFSET = 1
FPS = 60

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)

grid = Grid(WIDTH, HEIGHT, SCALE, OFFSET)
grid.random_2d_array()

paused = False
is_running = True

while is_running:
    screen.fill(BACK)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type != pygame.KEYUP:
            continue

        if event.key == pygame.K_ESCAPE:
            is_running = False

        if event.key == pygame.K_SPACE:
            paused = not paused

    grid.conway(color_one=WHITE, color_two=BLUE, surface=screen, pause=paused)

    if pygame.mouse.get_pressed(num_buttons=3)[0]:
        grid.mouse_handler(*pygame.mouse.get_pos())

    pygame.display.update()

pygame.display.quit()
pygame.quit()
