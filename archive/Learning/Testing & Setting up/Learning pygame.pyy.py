import random
import pygame
import time

from pygame.key import start_text_input
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

car_width = 73  # Can be replaced by arrow height

carImg = pygame.image.load(
    r'F:\Documents\GitHub\Snakes-and-Kabootars\Playgrounds\Learning\Testing & Setting up\racecar.png')


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)


def crash():
    message_display('You Crashed')
    game_loop()


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_STARTX = random.randrange(0, display_width)
    thing_STARTY = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False
    change = +1
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         x_change = -5
            #     if event.key == pygame.K_RIGHT:
            #         x_change = 5

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_change = 0
        if change == +1:
            x_change = 5
        else:
            x_change = -5
        x += x_change

        gameDisplay.fill(white)
        things(thing_STARTX, thing_STARTY, thing_width, thing_height, black)
        thing_STARTY += thing_speed
        car(x, y)

        if x > display_width - car_width:
            change = -1
        if x < 0:
            change = +1

        if thing_STARTY == display_height:
            thing_STARTY = 0 - thing_height
            thing_STARTX = random.randrange(0, display_width)
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
