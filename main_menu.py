import sys
import pygame
import game
# import config
pygame.init()
clock = pygame.time.Clock()

# Screen
WIDTH = 800
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

        start_button = button("Start",
                              (WIDTH/1.5) - 75, (HEIGHT/2) - 15, 120, 50, 'Gold', 'Purple')

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
                return False
                # exit()

        pygame.display.update()
        # clock.tick(15)
        return True


# text = what to write, x = position along x of top left corner of text, y = position along y of top left corner of text, width = width of button, height = height of button, actovecolor = color when hovering, inactivecolor = color when dormant


def text_object(text, font, colour):
    textSurface = font.render(text, True, colour)
    print("textSurface:", textSurface, "\nget_rect:",
          print(textSurface.get_rect()))
    return textSurface, textSurface.get_rect()


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
            # config.players = 1
            # print(config.players)
            in_menu = False
            game.main(1)

        double_player = create_button(300, 500, double_player_text.get_width(
        ) + 20, double_player_text.get_height(), 'Gold', "Purple")
        # double player button blit
        screen.blit(double_player_text, (310, 500))

        if double_player:  # move to double player mode
            # config.players = 2
            in_menu = False
            game.main(2)

        triple_player = create_button(550, 500, triple_player_text.get_width(
        ) + 20, triple_player_text.get_height(), 'Gold', "Purple")
        # double player button blit
        screen.blit(triple_player_text, (560, 500))

        if triple_player:  # move to double player mode
            # config.players = 3
            in_menu = False
            pygame.quit()
            game.main(3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        # clock.tick(15)


# runner
in_menu = True
while in_menu:
    menu_state = start_menu()
    if menu_state == False:
        in_menu = False
        pygame.quit()
        sys.exit()
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_menu = False
    pygame.display.update()
    # clock.tick(15)
