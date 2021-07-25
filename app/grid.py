import pygame
import numpy as np
import random


class Grid:

    def __init__(self, width, height, span, offset):
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

    def draw(self, color_one, color_two, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                pygame.draw.rect(
                    surface,
                    color_two if self.grid_array[x][y] == 1 else color_one,
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
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)
                next_grid[x][y] = get_next_cell_state(state, neighbours)

        self.grid_array = next_grid

    def conway(self, color_one, color_two, surface, pause):
        self.draw(color_one, color_two, surface)

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
    if state == 0 and neighbours == 3:
        return True

    if state == 1 and (neighbours < 2 or neighbours > 3):
        return False

    return state
