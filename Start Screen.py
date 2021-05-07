import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

#Screen
WIDTH = 800
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HU Kabootars les gooo')
        #BAckground
background = pygame.image.load(r"images\Kabootars\kabbu.jpg")

def start_menu():
    hellotext = pygame.font.SysFont("Arial",30).render('Hello',True, 'white')
    while True: #keeps running after called
        screen.fill("black")  #default colour
        screen.blit(hellotext,(5,5))    #test text
        screen.blit(background,(-500,-100)) #blit the background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(1)
        return True


# runner
while True:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(1)


        
def chooseMode