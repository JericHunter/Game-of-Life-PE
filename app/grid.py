import random

import numpy as np
import pygame


class Grid:

    def __init__(self, width, height, span, offset, cell_color):
        self.cell_color = cell_color

        self.span = span

        self.columns = height // span
        self.rows = width // span

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size)
        self.offset = offset

    def random_2d_array(self):
        self.grid_array = [
            [not random.randint(0, 1) for _y in range(self.columns)]
            for _x in range(self.rows)
        ]

    def draw(self, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                if not self.grid_array[x][y]:
                    continue

                pygame.draw.rect(
                    surface,
                    self.cell_color,
                    [
                        x * self.span,
                        y * self.span,
                        self.span - self.offset,
                        self.span - self.offset
                    ]
                )

    def update(self):
        next_grid = np.ndarray(shape=self.size)

        for x in range(self.rows):
            for y in range(self.columns):
                next_grid[x][y] = get_next_cell_state(
                    self.grid_array[x][y], self.get_neighbours(x, y)
                )

        self.grid_array = next_grid

    def conway(self, surface, pause):
        self.draw(surface)

        if not pause:
            self.update()

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            x_edge = (x + n + self.rows) % self.rows

            for m in range(-1, 2):
                y_edge = (y + m + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        return total - self.grid_array[x][y]

    def mouse_handler(self, mouse_x, mouse_y):
        self.grid_array[mouse_x // self.span][mouse_y // self.span] = True


def get_next_cell_state(state, neighbours):
    if neighbours == 3:
        return True

    if neighbours < 2 or neighbours > 3:
        return False

    return state
