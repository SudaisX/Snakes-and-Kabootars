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
        self.x = board.board.graph[self.current_pos][0][1][0]
        self.y = board.board.graph[self.current_pos][0][1][1]

    def draw(self): #draw method
        self.x = board.board.graph[self.current_pos][0][1][0]
        self.y = board.board.graph[self.current_pos][0][1][1]
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

class Board():
    def __init__(self):
        self.board = Graph()
        self.tiles = [i for i in range(101)]
        self.edges = self.create_tiles(370, 70, 660, 70)
        self.board.addNodes(self.tiles)
        self.board.addEdges(self.edges, True) 

    def create_tiles(self, x, x_change, y, y_change):
        x_nodes = []
        y_nodes = []
        tiles = []

        for i in range(10):
            x_nodes.append(x)
            x += x_change

        for i in range(10):
            y_nodes.append(y)
            y -= y_change

        n = 0
        left = True
        for i in range(10):
            if left:
                for j in range(10):
                    tiles.append((n, n+1, (x_nodes[j], y_nodes[i])))
                    n+=1
                left = False
            else:
                for j in range(9, -1, -1):
                    tiles.append((n, n+1, (x_nodes[j], y_nodes[i])))
                    n+=1
                left = True
        return tiles

    def add_kabootars(self, kabootars):
        self.board.addEdges(kabootars, True)

#Setting the graph up
# graph = Graph()

# tiles = [i for i in range(101)] #list of all the nodes/tiles
# #(node, edge, (x, y))
# tile_edges = [(0, 1, (370, 660)), (1, 2, (440, 660)), (2, 3, (510, 660)), (3, 4, (580, 660)), (4, 5, (650, 660)), (5, 6, (720, 660)), (6, 7, (790, 660)), (7, 8, (860, 660)), (8, 9, (930, 660)), (9, 10, (1000, 660)), (10, 11, (1000, 
# 590)), (11, 12, (930, 590)), (12, 13, (860, 590)), (13, 14, (790, 590)), (14, 15, (720, 590)), (15, 16, (650, 590)), (16, 17, (580, 590)), (17, 18, (510, 590)), (18, 19, (440, 590)), (19, 20, (370, 590)), (20, 21, (370, 520)), (21, 22, (440, 520)), (22, 23, (510, 520)), (23, 24, (580, 520)), (24, 25, (650, 520)), (25, 26, (720, 520)), (26, 27, (790, 520)), (27, 28, (860, 520)), (28, 29, (930, 520)), (29, 30, (1000, 520)), (30, 31, (1000, 450)), (31, 32, (930, 450)), (32, 33, (860, 450)), (33, 34, (790, 450)), (34, 35, (720, 450)), (35, 36, (650, 450)), (36, 37, (580, 450)), (37, 38, (510, 450)), (38, 39, (440, 450)), (39, 40, (370, 450)), (40, 41, (370, 380)), (41, 42, (440, 380)), (42, 43, (510, 380)), (43, 44, (580, 380)), (44, 45, (650, 380)), (45, 46, (720, 380)), (46, 47, (790, 380)), (47, 48, (860, 380)), (48, 49, (930, 380)), (49, 50, (1000, 380)), (50, 51, (1000, 310)), (51, 52, (930, 310)), (52, 53, (860, 310)), (53, 54, (790, 310)), (54, 55, (720, 310)), (55, 56, (650, 310)), (56, 57, (580, 310)), (57, 58, (510, 310)), (58, 59, (440, 310)), (59, 60, (370, 310)), (60, 61, (370, 240)), (61, 62, (440, 240)), (62, 63, (510, 240)), (63, 64, (580, 240)), (64, 65, (650, 240)), (65, 66, (720, 240)), (66, 67, (790, 240)), (67, 68, (860, 240)), (68, 69, (930, 240)), (69, 70, (1000, 240)), (70, 71, (1000, 170)), (71, 72, (930, 170)), (72, 73, (860, 170)), (73, 74, (790, 170)), (74, 75, (720, 170)), (75, 76, (650, 170)), (76, 77, (580, 170)), (77, 78, (510, 170)), (78, 79, (440, 170)), (79, 80, (370, 170)), (80, 81, (370, 100)), (81, 82, (440, 100)), (82, 83, (510, 100)), (83, 84, (580, 100)), (84, 85, (650, 100)), (85, 86, (720, 100)), (86, 87, (790, 100)), (87, 88, (860, 100)), (88, 89, (930, 100)), (89, 90, (1000, 100)), 
# (90, 91, (1000, 30)), (91, 92, (930, 30)), (92, 93, (860, 30)), (93, 94, (790, 30)), (94, 95, (720, 30)), (95, 96, (650, 30)), (96, 97, (580, 30)), (97, 98, (510, 30)), (98, 99, (440, 30)), (99, 100, (370, 30))]

board = Board()
snakes = [] #edges for all the snakes
kabootars = [(35, 10, (0, 0))] #edges for all the kabootars

board.add_kabootars(kabootars)
# graph.addEdges(kabootars, True)

# total_players = int(input("How many players? Enter a number between 2-4\n"))
# players = Queue()

#debugging
pprint(board.board.displayGraph())

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