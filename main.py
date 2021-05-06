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
    time.sleep(0.5)
    player2.current_pos += 1


    pygame.display.update() #updates display within the loop