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

        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.grid.add_mouse_cell(*pygame.mouse.get_pos())
            self.grid.draw(surface=self.screen)

        if event.type != pygame.KEYUP:
            return

        if event.key == pygame.K_ESCAPE:
            self.is_running = False

        elif event.key == pygame.K_SPACE:
            self.paused = not self.paused

    def run(self):
        self.is_running = True

        while self.is_running:
            for event in pygame.event.get():
                self.handle_event(event)

            if not self.paused:
                self.screen.fill(BACK)
                self.grid.conway(surface=self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.display.quit()
        pygame.quit()
