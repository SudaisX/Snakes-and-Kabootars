# imports
import pygame
from pygame import Rect, mixer
from dsa import Graph, Stack, Queue
from pprint import pprint
from random import randint
import time

# Display Class


class Display():
    def __init__(self):
        # screen size and background image
        # creates the screen with the arguments passed as a tuple of (Width, Height)
        self.screen = pygame.display.set_mode((1080, 720))
        # ('Location of the background image')
        self.background = pygame.image.load(
            'images/backgrounds/Completed_board.png')

    def DrawScreen(self):
        self.screen.fill((45, 48, 51))  # draw a background of color (r, g, b)
        self.screen.blit(self.background, (0, 0))  # draw background image


# Main Game Class
class Game(Display):
    def __init__(self, total_players):
        # initializes pygame
        pygame.init()
        print('GAME STARTED! ')

        Display.__init__(self)

        # icon and title
        self.__SetIconTitle()

        # Background music
        self.__BackgroundMusic()

    def __BackgroundMusic(self):
        # Background music
        mixer.music.load('sounds/kabbu.mp3')  # ('file location')
        mixer.music.play(-1)  # -1 so it plays in a loop
        mixer.music.set_volume(0.2)

    def __SetIconTitle(self):
        icon = pygame.image.load(
            'images/players/player1.png')  # ('icon location')
        pygame.display.set_caption(
            'Kabootars and Ladders')  # ('Title of the game)
        pygame.display.set_icon(icon)  # display icon


# Board Class
class Board():
    def __init__(self):
        self.board = Graph()

        # Initialise the 100 board tile nodes
        self.board.addNodes([i for i in range(101)])

        # Position of each tile
        self.position = self.__FindTilePositions()

        # Create a board with nth tile connecting to n+1th tile
        self.__CreateTileEdges()

        # Add Kabootar Edges
        self.__addKabootars()

        # Add Snake Edges
        self.__addSnakes()

        # pprint(self.board.graph)

    # A private method to create tiles
    def __CreateTileEdges(self):
        edges = []

        for n in range(100):
            edges.append((n, n+1, self.position[n+1]))
        self.board.addEdges(edges, True)

    # function to add kabootars
    def __addKabootars(self):
        kabootars = [(3, 16, self.position[16]),
                     (11, 32, self.position[32]),
                     (23, 44, self.position[44]),
                     (28, 77, self.position[77]),
                     (69, 88, self.position[88]),
                     #  (80, 99, self.position[99])
                     ]
        self.board.addEdges(kabootars, True)

    # function to add snakes
    def __addSnakes(self):
        snakes = [(29, 8, self.position[8]),
                  (42, 21, self.position[21]),
                  (58, 5, self.position[5]),
                  (74, 45, self.position[45]),
                  (95, 71, self.position[71]),
                  (97, 79, self.position[79]),
                  (99, 61, self.position[61])
                  ]
        self.board.addEdges(snakes, True)

    # A private method to find tile positions
    def __FindTilePositions(self):
        x, x_change = 370, 70  # (Initial x, change in x)
        y, y_change = 660, 70  # (Initial y, change in y)

        x_nodes = []  # Row X
        y_nodes = []  # Col Y
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
                    n += 1
                left = False
            else:
                for j in range(9, -1, -1):
                    tiles_pos[n+1] = (x_nodes[j], y_nodes[i])
                    n += 1
                left = True
        return tiles_pos


# Player class
class Player(Board):
    def __init__(self, player_num):
        Board.__init__(self)
        self.screen = pygame.display.set_mode((1080, 720))
        self.player_num = player_num
        self.images = ['images/players/player1.png',
                       'images/players/zain.png', 'images/players/player2.png', ]
        self.image = pygame.image.load(self.images[player_num-1])
        self.current_pos = 0
        self.x = self.board.graph[self.current_pos][0][1][0]
        self.y = self.board.graph[self.current_pos][0][1][1]

    def draw(self):  # draw method
        self.x = self.board.graph[self.current_pos][0][1][0]
        self.y = self.board.graph[self.current_pos][0][1][1]
        self.screen.blit(self.image, (self.x, self.y))

    def onKabootarSnake(self):
        # Check if it has more than 1 out neighbour
        if len(self.board.getNeighbours(self.current_pos+1)) > 1:
            return True
        return False

    # def isWinner(self):
    #     if self.current_pos == 100:
    #         #Change Display
    #         #Display Current Player as winner
    #         #End Game



    def moveKabootarSnake(self):
        # Check if it has more than 1 out neighbour
        KabootarSnake = self.board.getNeighbours(self.current_pos+1)[1]
        # KabootarSnakePos = self.position[KabootarSnake]

        # gradient = self.__getGradient(self.position[self.current_pos], KabootarSnakePos)
        # print(self.current_pos, self.position[self.current_pos], KabootarSnake, KabootarSnakePos, gradient)
        self.current_pos = KabootarSnake - 1

    def getKabootarSnakePos(self):
        KabootarSnake = self.board.getNeighbours(self.current_pos+1)[1]
        KabootarSnakePos = self.position[KabootarSnake]
        return KabootarSnake, KabootarSnakePos

    def __getGradient(self, node1, node2):
        x = node2[0] - node1[0]
        y = node2[1] - node1[1]
        return (y/x)


# Players Class
class Players():
    def __init__(self, total_players):
        self.players = Queue()
        for i in range(total_players):
            self.players.enQueue(Player(i+1))


# Time class
class Time():
    pass  # Time elepased


# Kismat class (Dice)
class Kismat(Display):
    def __init__(self, players):
        self.tabs = {}

        # Players
        self.players = players

        # Display Screen
        Display.__init__(self)

        # Tab Colors
        self._colors = ('#32a852', '#a83157', '#2e2ea3',
                        '#a69430', '#a32f2f', '#772d9c')
        self.colors = list(self._colors)

        # Tab Height and Width
        self.tabHeight = 40
        self.tabWidth = 100

        # Arrow image
        self.arrowImg = pygame.image.load(r'images\arrow.png')

        # Tab number font
        self.numFont = pygame.font.Font(None, 20)

        self.kismat = randint(1, 6)

    def __assignTabs(self, x, y):
        """
        Initializes the tabs_dictionary
        tabs[dice_roll] = (x_coord of blit, y_coord of blit + TAB_HEIGHT)
        """
        d_rolls = []  # this block of code can be commented out
        # and some modifications can be made to get tabs that are in fixed orders
        while (len(d_rolls) != 6):
            roll = randint(1, 6)
            if roll not in d_rolls:
                d_rolls.append(roll)

        for index in range(6):
            self.tabs[d_rolls[index]] = (x, y + self.tabHeight*(index+1))

    def __renderTabs(self, x, y):
        # x, y -> (x,y) coordinates of the top left pixel of the arrow

        if len(self.tabs) == 0:
            self.__assignTabs(x, y)

        cum_height = 0
        x_spacing = self.arrowImg.get_size()[0] + 5

        x_tab_begin = x + x_spacing

        for bar in self.tabs:
            if bar != 0:
                tab = pygame.draw.rect(
                    self.screen, self.colors[bar-1], [x_tab_begin, y+cum_height, self.tabWidth, self.tabHeight])

                roll = self.numFont.render(str(bar), True, "White")
                roll_rect = roll.get_rect(center=tab.center)
                self.screen.blit(roll, roll_rect)
                cum_height += self.tabHeight
        # return tabs

    def __drawArrow(self, startX, startY):
        self.screen.blit(self.arrowImg, (startX, startY))

    def Qismat(self, x, y):
        self.__renderTabs(x, y)

        attempted = False
        _attempted = False
        motion = 1
        yPos = y
        clock = pygame.time.Clock()

        while not(attempted):
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        _attempted = True

            self.DrawScreen()
            self.__renderTabs(x, y)
            self.__drawArrow(x, yPos - 16)

            if motion == 1:
                heightChange = 15
            elif motion == -1:
                heightChange = -15

            yPos += heightChange

            if yPos > y + self.tabHeight*6:
                motion = -1
            elif yPos < y:
                motion = 1

            if _attempted:
                return yPos
                # attempted = True

            for player in self.players.q:
                player.draw()

            pygame.display.update()
            clock.tick(60)

    def QismatCalc(self, stoppingHeight):
        self.tabs[0] = (0, 0)
        print("stoppingHeight:", stoppingHeight)

        for roll in self.tabs:
            if (self.tabs[roll][1] >= stoppingHeight) and stoppingHeight > self.tabs[roll-1][1]:
                return roll

    def roll(self):
        self.kismat = randint(1, 6)
        return self.kismat

# Prompt ~Class~ function


# def display_prompt(message):
#     running = True
#     button_text = font.render(message, True, "White")
#     button_box = button_text.get_rect(center=((x+(width/2)), (y+(height/2))))
#     pygame.draw.rect(screen, "Black", ((WIDTH/2)-button_box.get_rect), y, width, height))
#     screen.blit(button_text, button_box)
#     # center graphic on screen?
    #
    # #
    # while running:
    #     for event in pygame.event.get():
    #         screen.blit(img, (coords[0], coords[1]))
    #         pygame.display.flip()

    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             running=False
    #             break



def main(total_players):
    # total_players = 3
    game = Game(total_players)
    players = Players(total_players)
    kismat = Kismat(players.players)

    # Game loop
    running = True  # Initialise with True to run the gamme
    while running:  # checks if game is still running
        game.DrawScreen()

        # Check keystrokes
        for event in pygame.event.get():  # iterates through all the eventss in event.get()
            if event.type == pygame.QUIT:  # Checks if the X button has been pressed on the window, if yes then
                running = False  # sets running to False so the game breaks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:  # if space pressed then,

                    # Move the player
                    # num = kismat.kismat.roll()
                    num = kismat.QismatCalc(kismat.Qismat(0, 300))

                    curr_player = players.players.deQueue()
                    players.players.enQueue(curr_player)

                    print(
                        f'Player {curr_player.player_num} pressed Space and rolled {num}')
                    for i in range(num):
                        # time delay between each player moving
                        time.sleep(0.5)

                        curr_player.current_pos += 1  # changing n position of time

                        for player in players.players.q:
                            player.draw()
                            # curr_player.draw()

                        pygame.display.update()
                        game.DrawScreen()
                    # if curr_player.hasWon():
                    #     pass
                    # Check if current position has a snake or a ladder
                    if curr_player.onKabootarSnake():
                        print('Standing on a snake/kabootar')
                        curr_player.moveKabootarSnake()

                        time.sleep(0.1)

                        for player in players.players.q:
                            player.draw()
                            curr_player.draw()

                        pygame.display.update()
                        game.DrawScreen()

        for player in players.players.q:
            player.draw()

        pygame.display.update()  # updates display within the loop
