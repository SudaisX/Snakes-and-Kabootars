import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

#Screen
WIDTH = 715
HEIGHT = 765
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HU Kabootars les gooo')
        #BAckground
background = pygame.image.load(r"images\Board.png")

def start_menu():
    hellotext = pygame.font.SysFont("Arial",30).render('Hello',True, 'white')
    while True: #keeps running after called
        screen.fill("black")  #default colour
        screen.blit(hellotext,WIDTH//2,HEIGHT//2)    #test text
        screen.blit(background,0,0) #blit the background

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                pygame.quit()
                sys.exit()
        pygame.display.update()
        clock.tick(1)
        return True


# runner
while True:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(1)


        
