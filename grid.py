import pygame
import numpy as np
import random


class Grid:
    def __init__(self, width, height, span, offset):
        self.span = span

        self.columns = int(height / span)
        self.rows = int(width / span)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size)
        self.offset = offset

    def random_2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)

    def conway(self, color_one, color_two, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_position = y * self.span
                x_position = x * self.span
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(
                        surface, color_two, [
                            x_position, y_position,
                            self.span - self.offset,
                            self.span - self.offset
                        ]
                    )

                else:
                    pygame.draw.rect(
                        surface, color_one, [
                            x_position, y_position,
                            self.span - self.offset,
                            self.span - self.offset
                        ]
                    )

        _next = np.ndarray(shape=self.size)

        if not pause:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours(x, y)
                    if state == 0 and neighbours == 3:
                        _next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        _next[x][y] = 0
                    else:
                        _next[x][y] = state
            self.grid_array = _next

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            x_edge = (x + n + self.rows) % self.rows

            for m in range(-1, 2):
                y_edge = (y + m + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

    def mouse_handler(self, x, y):
        _x = x // self.span
        _y = y // self.span

        if self.grid_array[_x][_y] is not None:
            self.grid_array[_x][_y] = 1
