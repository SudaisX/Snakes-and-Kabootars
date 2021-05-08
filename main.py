#imports
import pygame
from pygame import mixer
from dsa import Graph, Stack, Queue
from pprint import pprint
from random import randint
import time

#Board Class
class Board():
    def __init__(self):
        self.board = Graph()
        self.tiles = [i for i in range(101)]
        self.edges = self.__create_tiles(370, 70, 660, 70)
        self.board.addNodes(self.tiles)
        self.board.addEdges(self.edges, True) 
        # pprint(self.board.graph)

    # A private method to create tiles
    def __create_tiles(self, x, x_change, y, y_change):
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

    #function to add kabootars
    def add_kabootars(self, kabootars):
        self.board.addEdges(kabootars, True)
    
    #function to add snakes
    def add_snakes(self, snakes):
        self.board.addEdges(snakes, True)

#Player class
class Player(Board):
    def __init__(self, player_num):
        Board.__init__(self)
        self.screen = pygame.display.set_mode((1080, 720))
        self.player_num = player_num
        self.images = ['images/players/player1.png', 'images/players/zain.png']
        self.image = pygame.image.load(self.images[player_num-1])
        self.current_pos = 0
        self.x = self.board.graph[self.current_pos][0][1][0]
        self.y = self.board.graph[self.current_pos][0][1][1]

    def draw(self): #draw method
        self.x = self.board.graph[self.current_pos][0][1][0]
        self.y = self.board.graph[self.current_pos][0][1][1]
        self.screen.blit(self.image, (self.x, self.y))

#Time class
class Time():
    pass #Time elepased

#Dice class
class Kismat():
    #TODO: Need to add visualisation to it
    def __init__(self):
        self.kismat = randint(1, 6)

    def roll(self):
        self.kismat = randint(1, 6)
        return self.kismat


#Main Game Class
class Game():
    def __init__(self):
        #initializes pygame
        pygame.init()
        print('GAME STARTED! ')

        #screen size and background image
        self.screen = pygame.display.set_mode((1080, 720)) #creates the screen with the arguments passed as a tuple of (Width, Height)
        self.background = pygame.image.load('images/backgrounds/newboard.png') #('Location of the background image')

        #icon and title
        self.__SetIconTitle()

        #Background music
        self.__BackgroundMusic()

        #Create Players
        self.__CreatePlayers()

        #Kismat
        self.kismat = Kismat()

    def __BackgroundMusic(self):
        #Background music
        mixer.music.load('sounds/kabbu.mp3') #('file location')
        mixer.music.play(-1) #-1 so it plays in a loop

    def __SetIconTitle(self):
        icon = pygame.image.load('images/players/player1.png') #('icon location')
        pygame.display.set_caption('Kabib ke Habootars') #('Title of the game)
        pygame.display.set_icon(icon) #display icon

    def __CreatePlayers(self):
        #Initialising Players
        total_players = int(input("How many players? Enter a number between 2-4\n"))
        self.players = Queue()
        for i in range(total_players): 
            self.players.enQueue(Player(i+1))

    def __CreateBoard(self):
        self.board = Board()
        snakes = [] #edges for all the snakes
        kabootars = [(35, 10, (0, 0))] #edges for all the kabootars

        self.board.add_kabootars(kabootars)
        self.board.add_snakes(snakes)

    def DrawScreen(self):
        self.screen.fill((45, 48, 51)) #draw a background of color (r, g, b)
        self.screen.blit(self.background, (0,0)) #draw background image



game = Game()
#Game loop
running = True #Initialise with True to run the gamme
while running: #checks if game is still running
    game.DrawScreen()

    #Check keystrokes
    for event in pygame.event.get(): #iterates through all the eventss in event.get()
        if event.type == pygame.QUIT: #Checks if the X button has been pressed on the window, if yes then
            running = False #sets running to False so the game breaks
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: #if space pressed then,
                num = game.kismat.roll()
                curr_player = game.players.deQueue()
                print(f'Player {curr_player.player_num} pressed Space and rolled {num}')
                for i in range(num):
                    time.sleep(0.5) #time delay between each player moving
                    
                    curr_player.current_pos += 1 #changing n position of time 

                    for player in game.players.q:
                        player.draw()
                        curr_player.draw()

                    pygame.display.update()
                    game.DrawScreen()
                game.players.enQueue(curr_player)

    for player in game.players.q:
        player.draw()

    pygame.display.update() #updates display within the loop