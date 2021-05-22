import time
from random import randint
from pprint import pprint
from dsa import Graph, Stack, Queue
from pygame import mixer
import sys
import pygame
import game
import config
from configparser import ConfigParser
pygame.init()
clock = pygame.time.Clock()

# Screen
WIDTH = 1080
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HU Kabootars les gooo')
# Background_start_menu
background = pygame.image.load(r"images\backgrounds\menu_bg.jpg")
# Music
pygame.mixer.music.load('sounds/kabbu.mp3')  # ('file location')
pygame.mixer.music.play(-1)  # -1 so it plays in a loop
# font
font = pygame.font.Font(r'Fonts\Fipps-Regular.otf', 20)
small_font = pygame.font.Font(r'Fonts\Fipps-Regular.otf', 10)


def start_menu():
    hellotext = font.render('Hello', True, 'white')
    running = True
    while True:  # keeps running after called
        pygame.event.get()
        screen.fill("black")  # default colour
        # screen.blit(hellotext,(5,5))    #test text
        screen.blit(background, (0, 0))  # blit the background
        # start_text = font.render("Start!", True, 'White')  # start button text
        # start_button = create_button(
        #     500, 50, start_text.get_width(), start_text.get_height(), 'Gold', 'Purple')
        # screen.blit(start_text, (500, 50))  # start button blit on screen
        # start_button_width, start_button_height = button_padding(start_text)
        start_button = button("Start",
                              (WIDTH/1.5) - 75, (HEIGHT/2) - 15, 120, 50, 'Gold', 'Purple')
        # screen.blit(start_text, (500, 50))  # start button blit on screen

        credit_text = font.render(" Credits ", True, 'White')
        credits_button = create_button(
            650, (HEIGHT/2) - 15, credit_text.get_width(), credit_text.get_height(), 'Gold', 'Purple')
        screen.blit(credit_text, (650, (HEIGHT/2) - 15))

        if credits_button:
            credit()

        if start_button:
            player_select()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        pygame.display.update()
        # clock.tick(15)
        return True

# text = what to write, x = position along x of top left corner of text, y = position along y of top left corner of text, width = width of button, height = height of button, actovecolor = color when hovering, inactivecolor = color when dormant


def create_button(x, y, width, height, activecolor, inactivecolor, text_colour="White"):
    cursor = pygame.mouse.get_pos()  # stores the position of the cursor in tuple (x,y)
    # senses when clicked return a tuple of (x,y)
    click = pygame.mouse.get_pressed(3)

    # if my mouse is on the button
    if (x + width) > cursor[0] > x and (y + height) > cursor[1] > y:
        # light up the button
        pygame.draw.rect(screen, activecolor, (x, y, width, height))
        if click[0] == 1:
            return True  # when the click is on the button move to player choosing screen
    else:
        # when not hovering keep it dormant
        pygame.draw.rect(screen, inactivecolor, (x, y, width, height))


def button(text, x, y, width, height, activecolor, inactivecolor, text_colour="White"):
    cursor = pygame.mouse.get_pos()  # stores the position of the cursor in tuple (x,y)
    # senses when clicked return a tuple of (x,y)
    click = pygame.mouse.get_pressed(3)

    # if my mouse is on the button
    if (x + width) > cursor[0] > x and (y + height) > cursor[1] > y:
        # light up the button
        pygame.draw.rect(screen, activecolor, (x, y, width, height))
        if click[0] == 1:
            return True  # when the click is on the button move to player choosing screen
    else:
        # when not hovering keep it dormant
        pygame.draw.rect(screen, inactivecolor, (x, y, width, height))

    button_text = font.render(text, True, text_colour)
    button_box = button_text.get_rect(center=((x+(width/2)), (y+(height/2))))
    screen.blit(button_text, button_box)


def credit():  # goes to credit screen (includes back button)
    running = True
    while running:
        pygame.event.get()
        screen.fill('Black')
        screen.blit(background, (0, 0))

        credits_1 = font.render(' Zain Ahmed Usmani', True, 'White')
        credits_2 = font.render(' Sudais Yasin', True, 'White')
        credits_3 = font.render(' Murtaza Ali Khokhar ', True, 'White')
        pygame.draw.rect(
            screen, 'Black', (300, 200, credits_3.get_width(), credits_3.get_height()))
        pygame.draw.rect(
            screen, 'Black', (300, 300, credits_3.get_width(), credits_3.get_height()))
        pygame.draw.rect(
            screen, 'Black', (300, 400, credits_3.get_width(), credits_3.get_height()))
        screen.blit(credits_1, (300, 200))
        screen.blit(credits_2, (300, 300))
        screen.blit(credits_3, (300, 400))

        back = font.render(' back ', True, 'White')
        back_button = create_button(
            100, 100, back.get_width(), back.get_height(), 'Gold', 'Purple')
        screen.blit(back, (100, 100))

        if back_button:
            running = False
            start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        # clock.tick(15)


def player_select():  # second screen
    global players
    running = True
    while running:
        pygame.event.get()
        screen.fill('Black')
        screen.blit(background, (0, 0))
        single_player_text = font.render(
            '1 player', True, 'White')  # single player mode text
        double_player_text = font.render(
            '2 players', True, 'White')  # dual player mode text
        triple_player_text = font.render(
            '3 players', True, 'White')  # triple player mode text

        player_select_prompt = font.render(
            'How many players will be playing?', True, 'White')  # prompt text
        screen.blit(player_select_prompt, (125, 300))

        single_player = create_button(50, 500, single_player_text.get_width(
        ) + 20, single_player_text.get_height(), 'Gold', 'Purple')
        # single player button blit
        screen.blit(single_player_text, (60, 500))

        if single_player:  # move to single player mode
            # game(1)
            players = 1
            config.players = 1
            print(config.players)
            running = False
            game.main()

        double_player = create_button(300, 500, double_player_text.get_width(
        ) + 20, double_player_text.get_height(), 'Gold', "Purple")
        # double player button blit
        screen.blit(double_player_text, (310, 500))

        if double_player:  # move to double player mode
            config.players = 2
            game.main()

        triple_player = create_button(550, 500, triple_player_text.get_width(
        ) + 20, triple_player_text.get_height(), 'Gold', "Purple")
        # double player button blit
        screen.blit(triple_player_text, (560, 500))

        if triple_player:  # move to double player mode
            config.players = 3
            game.main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        # clock.tick(15)


def main():
    # runner
    running = True
    while running:
        start_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(15)


main()
# imports

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

        pprint(self.board.graph)

    # A private method to create tiles
    def __CreateTileEdges(self):
        edges = []

        for n in range(100):
            edges.append((n, n+1, self.position[n+1]))
        self.board.addEdges(edges, True)

    # function to add kabootars
    def __addKabootars(self):
        kabootars = [(3, 25, self.position[25]),
                     (28, 77, self.position[77]),
                     (69, 88, self.position[59]),
                     (80, 99, self.position[99]), ]
        self.board.addEdges(kabootars, True)

    # function to add snakes
    def __addSnakes(self):
        snakes = [(29, 8, self.position[8]),
                  (42, 21, self.position[21]),
                  (58, 5, self.position[5]),
                  (74, 45, self.position[45]),
                  (95, 71, self.position[71]),
                  (97, 79, self.position[79])]
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
                       'images/players/player2.png', 'images/players/zain.png']
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

    def moveKabootarSnake(self):
        # Check if it has more than 1 out neighbour
        KabootarSnake = self.board.getNeighbours(self.current_pos+1)[1]
        #KabootarSnakePos = self.position[KabootarSnake]

        # gradient = self.__getGradient(self.position[self.current_pos], KabootarSnakePos)
        # print(self.current_pos, self.position[self.current_pos], KabootarSnake, KabootarSnakePos, gradient)
        self.current_pos = KabootarSnake

    def getKabootarSnakePos(self):
        KabootarSnake = self.board.getNeighbours(self.current_pos+1)[1]
        KabootarSnakePos = self.position[KabootarSnake]
        return KabootarSnake, KabootarSnakePos

    def __getGradient(self, node1, node2):
        x = node2[0] - node1[0]
        y = node2[1] - node1[1]
        return (y/x)


# Time class
class Time():
    pass  # Time elepased

# Dice class


class Kismat():
    def __init__(self, screen):
        self.tabs = {}

        # Display Screen
        self.screen = screen

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

        while not(attempted):
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        _attempted = True

            game.DrawScreen()
            self.__renderTabs(x, y)
            self.__drawArrow(x, yPos - 16)

            if motion == 1:
                heightChange = 5
            elif motion == -1:
                heightChange = -5

            yPos += heightChange

            if yPos > y + self.tabHeight*6:
                motion = -1
            elif yPos < y:
                motion = 1

            if _attempted:
                return yPos
                #attempted = True

            for player in game.players.q:
                player.draw()

            pygame.display.update()
            # clock.tick(120)

    def QismatCalc(self, stoppingHeight):
        self.tabs[0] = (0, 0)
        print("stoppingHeight:", stoppingHeight)

        for roll in self.tabs:
            if (self.tabs[roll][1] >= stoppingHeight) and stoppingHeight > self.tabs[roll-1][1]:
                return roll

    def roll(self):
        self.kismat = randint(1, 6)
        return self.kismat


# Main Game Class
class Game():
    def __init__(self):
        # initializes pygame
        pygame.init()
        print('GAME STARTED! ')

        # screen size and background image
        # creates the screen with the arguments passed as a tuple of (Width, Height)
        self.screen = pygame.display.set_mode((1080, 720))
        # ('Location of the background image')
        self.background = pygame.image.load('images/backgrounds/newboard.png')

        #icon and title
        self.__SetIconTitle()

        # Background music
        self.__BackgroundMusic()

        # Create Players
        self.__CreatePlayers()

        # Kismat
        self.kismat = Kismat(self.screen)

    def __BackgroundMusic(self):
        # Background music
        mixer.music.load('sounds/kabbu.mp3')  # ('file location')
        mixer.music.play(-1)  # -1 so it plays in a loop

    def __SetIconTitle(self):
        icon = pygame.image.load(
            'images/players/player1.png')  # ('icon location')
        pygame.display.set_caption(
            'Kabib ke Habootars')  # ('Title of the game)
        pygame.display.set_icon(icon)  # display icon

    def __CreatePlayers(self):
        # Initialising Players
        # total_players = int(input("How many players? Enter a number between 2-4\n"))
        global players
        total_players = players
        print(players)
        self.players = Queue()
        for i in range(total_players):
            self.players.enQueue(Player(i+1))

    def DrawScreen(self):
        self.screen.fill((45, 48, 51))  # draw a background of color (r, g, b)
        self.screen.blit(self.background, (0, 0))  # draw background image


game = Game()
kismat = Kismat(game.screen)

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
                # num = game.kismat.roll()
                num = game.kismat.QismatCalc(game.kismat.Qismat(0, 300))

                curr_player = game.players.deQueue()
                game.players.enQueue(curr_player)
                print(
                    f'Player {curr_player.player_num} pressed Space and rolled {num}')
                for i in range(num):
                    # time delay between each player moving
                    time.sleep(0.5)

                    curr_player.current_pos += 1  # changing n position of time

                    for player in game.players.q:
                        player.draw()
                        # curr_player.draw()

                    pygame.display.update()
                    game.DrawScreen()

                # Check if current position has a snake or a ladder
                if curr_player.onKabootarSnake():
                    print('Standing on a snake/kabootar')
                    curr_player.moveKabootarSnake()

                    time.sleep(0.1)

                    for player in game.players.q:
                        player.draw()
                        curr_player.draw()

                    pygame.display.update()
                    game.DrawScreen()

    for player in game.players.q:
        player.draw()

    pygame.display.update()  # updates display within the loop
