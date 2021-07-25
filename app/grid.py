import random
from typing import Tuple, List

import pygame

Color = Tuple[int, int, int]


class Grid:

    def __init__(self, width, height, span, offset, cell_color) -> None:
        self.cell_color: Color = cell_color

        self.span: int = span

        cell_side_size: int = self.span - offset
        self.cell_size: Tuple[int, int] = (cell_side_size, cell_side_size)

        self.columns: int = height // span
        self.rows: int = width // span

        self.grid_size: Tuple[int, int] = (self.rows, self.columns)

        self.grid_array: List[List[bool]] = [
            [not random.randint(0, 1) for _y in range(self.columns)]
            for _x in range(self.rows)
        ]

    def draw(self, surface) -> None:
        for x in range(self.rows):
            for y in range(self.columns):
                if not self.grid_array[x][y]:
                    continue

                pygame.draw.rect(
                    surface,
                    self.cell_color,
                    ((x * self.span, y * self.span), self.cell_size)
                )

    def update(self) -> None:
        self.grid_array: List[List[bool]] = [
            [
                get_next_cell_state(
                    self.grid_array[x][y], self.get_neighbours(x, y)
                ) for y in range(self.columns)
            ] for x in range(self.rows)
        ]

    def conway(self, surface) -> None:
        self.update()
        self.draw(surface)

    def get_neighbours(self, x: int, y: int) -> int:
        total: int = 0
        for n in range(-1, 2):
            x_edge: int = (x + n + self.rows) % self.rows

            for m in range(-1, 2):
                y_edge: int = (y + m + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        return total - self.grid_array[x][y]

    def add_mouse_cell(self, mouse_x: int, mouse_y: int) -> None:
        self.grid_array[mouse_x // self.span][mouse_y // self.span] = True


def get_next_cell_state(state: bool, neighbours: int) -> bool:
    if neighbours == 3:
        return True

    if neighbours < 2 or neighbours > 3:
        return False

    return state
