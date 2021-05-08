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

        #Initialise the 100 board tile nodes
        self.board.addNodes([i for i in range(101)])

        #Position of each tile
        self.position = self.__FindTilePositions()

        #Create a board with nth tile connecting to n+1th tile
        self.__CreateTileEdges()
        
        #Add Kabootar Edges
        self.__addKabootars()
        
        #Add Snake Edges
        self.__addSnakes()

        pprint(self.board.graph)

    # A private method to create tiles
    def __CreateTileEdges(self):
        edges = []
        
        for n in range(100):
            edges.append((n, n+1, self.position[n+1]))
        self.board.addEdges(edges, True) 

    #function to add kabootars
    def __addKabootars(self):
        kabootars = [(5, 15, self.position[15]),
                    (2, 28, self.position[28]),
                    (12, 29, self.position[29]),
                    (20, 38, self.position[38]),]
        self.board.addEdges(kabootars, True)
    
    #function to add snakes
    def __addSnakes(self):
        snakes = []
        self.board.addEdges(snakes, True)

    # A private method to find tile positions
    def __FindTilePositions(self):
        x, x_change = 370, 70 # (Initial x, change in x)
        y, y_change = 660, 70 # (Initial y, change in y)
        
        x_nodes = [] #Row X
        y_nodes = [] #Col Y
        tiles_pos = {}

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
                    tiles_pos[n+1] = (x_nodes[j], y_nodes[i])
                    n+=1
                left = False
            else:
                for j in range(9, -1, -1):
                    tiles_pos[n+1] = (x_nodes[j], y_nodes[i])
                    n+=1
                left = True
        return tiles_pos

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

    def onKabootarSnake(self):
        #Check if it has more than 1 out neighbour
        if len(self.board.getNeighbours(self.current_pos+1)) > 1:
            return True
        return False

    def moveKabootarSnake(self):
        #Check if it has more than 1 out neighbour
        KabootarSnake = self.board.getNeighbours(self.current_pos+1)[1]
        # KabootarSnakePos = self.position[KabootarSnake]

        # gradient = self.__getGradient(self.position[self.current_pos], KabootarSnakePos)

        # print(self.current_pos, self.position[self.current_pos], KabootarSnake, KabootarSnakePos, gradient)

        self.current_pos = KabootarSnake

    def __getGradient(self, node1, node2):
        x = node2[0] - node1[0]
        y = node2[1] - node1[1]
        return (y/x)
 

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

                #Move the player
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

                # Check if current position has a snake or a ladder
                if curr_player.onKabootarSnake():
                    time.sleep(0.5)
                    curr_player.moveKabootarSnake()
                    for player in game.players.q:
                        player.draw()
                        curr_player.draw()

                    pygame.display.update()
                    game.DrawScreen()

                    print('Standing on a snake/kabootar')

    for player in game.players.q:
        player.draw()

    pygame.display.update() #updates display within the loop