import pygame

from app.grid import Grid

WIDTH, HEIGHT = 1920, 1080
SIZE = (WIDTH, HEIGHT)

BACK = (0, 0, 0)
WHITE = (255, 255, 255)

TITLE = "CONWAY'S GAME OF LIFE PYTHON EDITION"

SCALE = 10
OFFSET = 1
FPS = -1


class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

        self.grid = Grid(WIDTH, HEIGHT, SCALE, OFFSET, WHITE)

        self.paused = False
        self.is_running = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running = False
            return

        if event.type != pygame.KEYUP:
            return

        if event.key == pygame.K_ESCAPE:
            self.is_running = False

        elif event.key == pygame.K_SPACE:
            self.paused = not self.paused

    def run(self):
        self.is_running = True

        while self.is_running:
            pygame.display.set_caption(f'{self.clock.get_fps():,.0f} FPS')

            self.screen.fill(BACK)
            self.clock.tick(FPS)

            for event in pygame.event.get():
                self.handle_event(event)

            self.grid.conway(surface=self.screen, pause=self.paused)

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.grid.mouse_handler(*pygame.mouse.get_pos())

            pygame.display.update()

        pygame.display.quit()
        pygame.quit()
