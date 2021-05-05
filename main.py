#imports
import pygame
from pygame import mixer
from dsa import Graph, Stack, Queue
from pprint import pprint
from random import randint

#initializes pygame
pygame.init()

#screen size and background image
screen = pygame.display.set_mode((926, 640)) #creates the screen with the arguments passed as a tuple of (Width, Height)
background = background = pygame.image.load('images/backgrounds/kabbu.jpg') #('Location of the background image')

#icon and title
icon = pygame.image.load('images/icons/icon.png') #('icon location')
pygame.display.set_caption('Kabib ke Habootars') #('Title of the game)
pygame.display.set_icon(icon) #display icon

# #Background music
mixer.music.load('sounds/kabbu.mp3') #('file location')
mixer.music.play(-1) #-1 so it plays in a loop

#Player class
class Player():
    def __init__(self, player_number):
        self.player_number = player_number
        self.position = graph.graph[0][3]

    def draw(self):
        pass

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

tiles = [i for i in range(1, 101)] #list of all the nodes/tiles
#(node, edge, (x, y))
tile_edges = [(1, 2, (0, 0)), (2, 3, (0, 0)), (3, 4, (0, 0)), (4, 5, (0, 0)), (5, 6, (0, 0)), (6, 7, (0, 0)), (7, 8, (0, 0)), (8, 9, (0, 0)), (9, 10, (0, 0)), 
(10, 11, (0, 0)), (11, 12, (0, 0)), (12, 13, (0, 0)), (13, 14, (0, 0)), (14, 15, (0, 0)), (15, 16, (0, 0)), (16, 17, (0, 0)), (17, 18, (0, 0)), (18, 19, (0, 0)), (19, 20, (0, 0)), 
(20, 21, (0, 0)), (21, 22, (0, 0)), (22, 23, (0, 0)), (23, 24, (0, 0)), (24, 25, (0, 0)), (25, 26, (0, 0)), (26, 27, (0, 0)), (27, 28, (0, 0)), (28, 29, (0, 0)), (29, 30, (0, 0)), 
(30, 31, (0, 0)), (31, 32, (0, 0)), (32, 33, (0, 0)), (33, 34, (0, 0)), (34, 35, (0, 0)), (35, 36, (0, 0)), (36, 37, (0, 0)), (37, 38, (0, 0)), (38, 39, (0, 0)), (39, 40, (0, 0)), 
(40, 41, (0, 0)), (41, 42, (0, 0)), (42, 43, (0, 0)), (43, 44, (0, 0)), (44, 45, (0, 0)), (45, 46, (0, 0)), (46, 47, (0, 0)), (47, 48, (0, 0)), (48, 49, (0, 0)), (49, 50, (0, 0)), 
(50, 51, (0, 0)), (51, 52, (0, 0)), (52, 53, (0, 0)), (53, 54, (0, 0)), (54, 55, (0, 0)), (55, 56, (0, 0)), (56, 57, (0, 0)), (57, 58, (0, 0)), (58, 59, (0, 0)), (59, 60, (0, 0)), 
(60, 61, (0, 0)), (61, 62, (0, 0)), (62, 63, (0, 0)), (63, 64, (0, 0)), (64, 65, (0, 0)), (65, 66, (0, 0)), (66, 67, (0, 0)), (67, 68, (0, 0)), (68, 69, (0, 0)), (69, 70, (0, 0)), 
(70, 71, (0, 0)), (71, 72, (0, 0)), (72, 73, (0, 0)), (73, 74, (0, 0)), (74, 75, (0, 0)), (75, 76, (0, 0)), (76, 77, (0, 0)), (77, 78, (0, 0)), (78, 79, (0, 0)), (79, 80, (0, 0)), 
(80, 81, (0, 0)), (81, 82, (0, 0)), (82, 83, (0, 0)), (83, 84, (0, 0)), (84, 85, (0, 0)), (85, 86, (0, 0)), (86, 87, (0, 0)), (87, 88, (0, 0)), (88, 89, (0, 0)), (89, 90, (0, 0)), 
(90, 91, (0, 0)), (91, 92, (0, 0)), (92, 93, (0, 0)), (93, 94, (0, 0)), (94, 95, (0, 0)), (95, 96, (0, 0)), (96, 97, (0, 0)), (97, 98, (0, 0)), (98, 99, (0, 0)), (99, 100, (0, 0))]

snakes = [] #edges for all the snakes
kabootars = [(35, 10, (0, 0))] #edges for all the kabootars

graph.addNodes(tiles)
graph.addEdges(tile_edges, True) 
graph.addEdges(snakes, True)
graph.addEdges(kabootars, True)

# total_players = int(input("How many players? Enter a number between 2-4\n"))
# players = Queue()

#debugging
# pprint(graph.displayGraph())

#Game loop
running = True #Initialise with True to run the gamme
while running: #checks if game is still running
    screen.fill((45, 48, 51)) #draw a background of color (r, g, b)
    screen.blit(background, (0,0)) #draw background image

    #Check keystrokes
    for event in pygame.event.get(): #iterates through all the eventss in event.get()
        if event.type == pygame.QUIT: #Checks if the X button has been pressed on the window, if yes then
            running = False #sets running to False so the game breaks

    pygame.display.update() #updates display within the loop