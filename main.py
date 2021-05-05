#imports
import pygame
from pygame import mixer
from dsa import Graph, Stack, Queue
from pprint import pprint
from random import randint
import time

#initializes pygame
pygame.init()

#screen size and background image
screen = pygame.display.set_mode((1080, 720)) #creates the screen with the arguments passed as a tuple of (Width, Height)
background = background = pygame.image.load('images/backgrounds/newboard.png') #('Location of the background image')

#icon and title
icon = pygame.image.load('images/player.png') #('icon location')
pygame.display.set_caption('Kabib ke Habootars') #('Title of the game)
pygame.display.set_icon(icon) #display icon

# #Background music
mixer.music.load('sounds/kabbu.mp3') #('file location')
mixer.music.play(-1) #-1 so it plays in a loop

#Player class
class Player():
    def __init__(self):
        self.image = pygame.image.load('images/player.png')
        self.current_pos = 0
        self.x = graph.graph[self.current_pos][0][1][0]
        self.y = graph.graph[self.current_pos][0][1][1]

    def draw(self): #draw method
        self.x = graph.graph[self.current_pos][0][1][0]
        self.y = graph.graph[self.current_pos][0][1][1]
        screen.blit(self.image, (self.x, self.y))

    # def move(self, steps):
    #     for i in range(steps):
    #         self.current_pos += 1
    #         time.sleep(1)
    #move function (doesnt work)
    # def move(self):
    #     graph.graph[0][0][1] = (self.position[0], self.position[1]+50)

#Time class
class Time():
    pass

#Dice class
class Dice():
    def __init__(self):
        pass

    def roll(self):
        pass

#Setting the graph up
graph = Graph()

tiles = [i for i in range(101)] #list of all the nodes/tiles
#(node, edge, (x, y))
tile_edges = [(0, 1, (370, 660)), (1, 2, (359, 615)), (2, 3, (422, 615)), (3, 4, (485, 615)), (4, 5, (548, 615)), (5, 6, (611, 615)), (6, 7, (674, 615)), (7, 8, (737, 615)), (8, 9, (800, 615)), (9, 10, (863, 615)), (10, 11, (863, 552)), (11, 12, (800, 552)), (12, 13, (737, 552)), (13, 14, (674, 552)), (14, 15, (611, 552)), (15, 16, (548, 552)), (16, 17, (485, 552)), (17, 18, (422, 552)), (18, 19, (359, 552)), (19, 20, (296, 552)), (20, 21, (296, 489)), (21, 22, (359, 489)), (22, 23, (422, 489)), (23, 24, (485, 489)), (24, 25, (548, 489)), (25, 26, (611, 489)), (26, 27, (674, 489)), (27, 28, (737, 489)), (28, 29, (800, 489)), (29, 30, (863, 489)), (30, 31, (863, 
426)), (31, 32, (800, 426)), (32, 33, (737, 426)), (33, 34, (674, 426)), (34, 35, (611, 426)), (35, 36, (548, 426)), (36, 37, (485, 426)), (37, 38, (422, 426)), (38, 39, (359, 426)), (39, 40, (296, 426)), (40, 41, (296, 363)), (41, 42, (359, 363)), (42, 43, (422, 363)), (43, 44, (485, 363)), (44, 45, (548, 363)), (45, 46, (611, 363)), (46, 47, (674, 363)), (47, 48, (737, 363)), (48, 49, (800, 363)), (49, 50, (863, 363)), (50, 51, (863, 300)), (51, 52, (800, 300)), (52, 53, (737, 300)), (53, 54, (674, 300)), (54, 55, (611, 300)), (55, 56, (548, 300)), (56, 57, (485, 300)), (57, 58, (422, 300)), (58, 59, (359, 300)), (59, 60, (296, 300)), (60, 61, (296, 237)), (61, 62, (359, 237)), (62, 63, (422, 237)), (63, 64, (485, 237)), (64, 65, (548, 237)), (65, 66, (611, 237)), (66, 67, (674, 237)), (67, 68, (737, 237)), (68, 69, (800, 237)), (69, 70, (863, 237)), (70, 71, (863, 174)), (71, 72, (800, 174)), (72, 73, (737, 174)), (73, 74, (674, 174)), (74, 75, (611, 174)), (75, 76, (548, 174)), (76, 77, (485, 174)), (77, 78, (422, 174)), (78, 79, (359, 174)), (79, 80, (296, 174)), (80, 81, (296, 111)), (81, 82, (359, 111)), (82, 83, (422, 111)), (83, 84, (485, 111)), (84, 85, (548, 111)), (85, 86, (611, 111)), (86, 87, (674, 111)), (87, 88, (737, 111)), (88, 89, (800, 111)), (89, 90, (863, 111)), (90, 91, 
(863, 48)), (91, 92, (800, 48)), (92, 93, (737, 48)), (93, 94, (674, 48)), (94, 95, (611, 48)), (95, 96, (548, 48)), (96, 97, (485, 48)), (97, 98, (422, 48)), (98, 99, (359, 48)), (99, 100, (296, 48))]

snakes = [] #edges for all the snakes
kabootars = [(35, 10, (0, 0))] #edges for all the kabootars

graph.addNodes(tiles)
graph.addEdges(tile_edges, True) 
graph.addEdges(snakes, True)
graph.addEdges(kabootars, True)

# total_players = int(input("How many players? Enter a number between 2-4\n"))
# players = Queue()

#debugging
pprint(graph.displayGraph())

player1 = Player()
player2 = Player()

# player2.current_pos = 58

#Game loop
running = True #Initialise with True to run the gamme
while running: #checks if game is still running
    screen.fill((45, 48, 51)) #draw a background of color (r, g, b)
    screen.blit(background, (0,0)) #draw background image

    #Check keystrokes
    for event in pygame.event.get(): #iterates through all the eventss in event.get()
        if event.type == pygame.QUIT: #Checks if the X button has been pressed on the window, if yes then
            running = False #sets running to False so the game breaks

    player1.draw()
    player2.draw()

    # random test of it moving
    time.sleep(0.1)
    player2.current_pos += 1


    pygame.display.update() #updates display within the loop