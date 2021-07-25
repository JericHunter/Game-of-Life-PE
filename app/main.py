from typing import Tuple

import pygame

from app.grid import Grid

Color = Tuple[int, int, int]

WIDTH: int = 1920
HEIGHT: int = 1080
SIZE: Tuple[int, int] = (WIDTH, HEIGHT)

BACK: Color = (0, 0, 0)
WHITE: Color = (255, 255, 255)

TITLE: str = "Conway's Game Of Life - Python Edition"

SCALE: int = 10
OFFSET: int = 1
FPS: int = 60


class Game:

    def __init__(self) -> None:
        self.screen: pygame.display = pygame.display.set_mode(SIZE)
        self.clock: pygame.time.Clock = pygame.time.Clock()
        pygame.display.set_caption(TITLE)

        self.grid: Grid = Grid(WIDTH, HEIGHT, SCALE, OFFSET, WHITE)

        self.paused: bool = False
        self.is_running: bool = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.is_running: bool = False
            return

        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.grid.add_mouse_cell(*pygame.mouse.get_pos())
            self.grid.draw(surface=self.screen)

        if event.type != pygame.KEYUP:
            return

        if event.key == pygame.K_ESCAPE:
            self.is_running: bool = False

        elif event.key == pygame.K_SPACE:
            self.paused: bool = not self.paused

    def run(self):
        self.is_running: bool = True

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
