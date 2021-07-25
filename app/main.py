import pygame

from app.grid import Grid

WIDTH, HEIGHT = 1920, 1080
SIZE = (WIDTH, HEIGHT)

BACK = (0, 0, 0)
BLUE = (0, 120, 150)
WHITE = (255, 255, 255)

TITLE = "CONWAY'S GAME OF LIFE PYTHON EDITION"

SCALE = 30
OFFSET = 1
FPS = -1


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

        self.grid = Grid(WIDTH, HEIGHT, SCALE, OFFSET)
        self.grid.random_2d_array()

        self.paused = False
        self.is_running = False

    def run(self):
        self.is_running = True

        while self.is_running:
            self.screen.fill(BACK)
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type != pygame.KEYUP:
                    continue

                if event.key == pygame.K_ESCAPE:
                    self.is_running = False

                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

            self.grid.conway(
                color_one=WHITE,
                color_two=BLUE,
                surface=self.screen,
                pause=self.paused
            )

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.grid.mouse_handler(*pygame.mouse.get_pos())

            pygame.display.update()

        pygame.display.quit()
        pygame.quit()
