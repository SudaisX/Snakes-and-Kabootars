import pygame

WIDTH = HEIGHT = 512
DIMENSION = 10
BLOCK_SIZE = WIDTH // DIMENSION

class GameEngine():
    def __init__(self):
        self.board = [
            ['end','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--','--','--'],
            ['start','--','--','--','--','--','--','--','--','--']
        ]


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    game = GameEngine()
    print(game.board())

main()