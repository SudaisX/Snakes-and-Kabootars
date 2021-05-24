import pygame
from pprint import *
WIDTH = HEIGHT = 600
DIMENSION = 10
BLOCK_SIZE = WIDTH // DIMENSION
IMAGES = {}
FPS = 60

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

def image_load():
    IMAGES['--'] = pygame.image.load(r"C:\Users\Student\Documents\GitHub\DSA-Projecto\images\box_4.png")

    
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('black'))
    game = GameEngine()
    image_load()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        drawGame(screen, game)
        clock.tick(FPS)
        pygame.display.flip()
        
def drawGame(screen, game):
    drawBoard(screen)


def drawBoard(screen):
    image = pygame.image.load(r'C:\Users\Student\Documents\GitHub\DSA-Projecto\images\box_4.png')
    image = pygame.transform.scale(image, (WIDTH//4,HEIGHT//4))
    image.convert()
    rect = image.get_rect()
    rect.center = DIMENSION//4,DIMENSION//4
    color_list = [pygame.Color('blue'),pygame.Color('orange')]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = color_list[(row+column) %2]
            screen.blit(image,rect)
            pygame.draw.rect(screen, 'white', rect,1)
main()