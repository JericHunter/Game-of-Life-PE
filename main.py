import pygame
from app.main import Game

pygame.init()


def main() -> None:
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
