import pygame
import random
import time

# Initialize pygame
pygame.init()


# Create the screen
size_x = 800  # horizontal size; length
size_y = 600  # vertical size; height
screen = pygame.display.set_mode((size_x, size_y))

# Initial steps for creating text on buttons (colours collection)
red = (244, 0, 0)
light_green = (0, 244, 0)
cyan = (0, 255, 255)
maroon = (128, 0, 0)
teal = (0, 128, 128)
purple = (128, 0, 128)
orange = (255, 100, 0)
magenta = (255, 0, 255)
blue = (0, 120, 200)
yellow = (255, 255, 0)
colour_HU_dpurple = (94, 36, 103)
colour_HU_lpurple = (205, 168, 206)
colour_HU_vDpurple = (70, 36, 120)
colour_HU_white = (237, 231, 213)
colour_HU_brown = (211, 193, 149)
colour_help_blue = (68, 114, 196)

# screen icon and title
pygame.display.set_caption("RAISE THE BAR!")
icon = pygame.image.load(r'Media\Icons & Graphics\bar chart.png')
pygame.display.set_icon(icon)


# for adding background images
lion_lab_img = pygame.image.load(
    r'Media\Icons & Graphics\Aesthetic Elements (Focus)\LionLab - Raising Bars (smol).png')
# imagess = pygame.transform.scale(imagess, (, 155))
x_lion_lab, y_lion_lab = 200, 1

img_prompt_lose_R_S = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_lose_R_S.png')
img_prompt_lose_S_P = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_lose_S_P.png')
img_prompt_lose_P_R = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_lose_P_R.png')
img_prompt_win_R_S = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_win_R_S.png')
img_prompt_win_S_P = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_win_S_P.png')
img_prompt_win_P_R = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_win_P_R.png')
img_prompt_draw_RR = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_draw_RR.png')
img_prompt_draw_PP = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_draw_PP.png')
img_prompt_draw_SS = pygame.image.load(
    r'Media\Icons & Graphics\Win-Lose Prompts\img_prompt_draw_SS.png')
# The score indicating bar
x_bar, y_bar, w_bar, h_bar = 300, 125, 200, 250
bar_0_img = pygame.image.load(
    r'Media\Icons & Graphics\The bar\bar@0.png')
bar_0_img = pygame.transform.scale(
    bar_0_img, (w_bar, h_bar))  # for resizing the image
bar_1_img = pygame.image.load(
    r'Media\Icons & Graphics\The bar\bar@1.png')
bar_1_img = pygame.transform.scale(
    bar_1_img, (w_bar, h_bar))  # for resizing the image
bar_neg1_img = pygame.image.load(
    r'Media\Icons & Graphics\The bar\bar@-1.png')
bar_neg1_img = pygame.transform.scale(
    bar_neg1_img, (w_bar, h_bar))  # for resizing the image
bar_2_img = pygame.image.load(
    r'Media\Icons & Graphics\The bar\bar@2.png')
bar_2_img = pygame.transform.scale(
    bar_2_img, (w_bar, h_bar))  # for resizing the image
bar_neg2_img = pygame.image.load(
    r'Media\Icons & Graphics\The bar\bar@-2.png')
bar_neg2_img = pygame.transform.scale(
    bar_neg2_img, (w_bar, h_bar))  # for resizing the image
bar_img_lib = {-2: bar_neg2_img, -1: bar_neg1_img,
               0: bar_0_img, 1: bar_1_img, 2: bar_2_img}


# player control button dimensions
# RPS = Rest, Productivity, SELScore
rps_y_pos, w_RPS_button, h_RPS_button = 500, 180, 80

transform_char_pic_arg = (250, 450)
# PSYCH Character
psych_pic = pygame.image.load(
    r'Media\Characters\Psyche.png')
psych_pic = pygame.transform.scale(
    psych_pic, transform_char_pic_arg)  # for resizing the image
# button_pos
# x_murt and y_murt indicate position in value; other is dimensions
x_murt, y_murt, w_murt, h_murt = 50, 400, 180, 50

# MYSTIQUE Character
mystique_pic = pygame.image.load(
    r'Media\Characters\Mystique.png')
mystique_pic = pygame.transform.scale(
    mystique_pic, transform_char_pic_arg)  # for resizing the image
# x_sam and y_sam indicate position in value; other is dimensions
x_sam, y_sam, w_sam, h_sam = 300, 400, 180, 50

# INVERTO Character
inverto_pic = pygame.image.load(
    r'Media\Characters\Inverto.png')
inverto_pic = pygame.transform.scale(
    inverto_pic, transform_char_pic_arg)  # for resizing the image
# x_zain and y_zain indicate position in value; other is dimensions
x_zain, y_zain, w_zain, h_zain = 550, 400, 180, 50

# INSTRUCTOR CHARACTER
instr_pic = pygame.image.load(
    r'Media\Characters\Instructor with bg.png')
instr_pic = pygame.transform.scale(
    instr_pic, (224, 214))  # for resizing the image
x_instr, y_instr, w_instr, h_instr = x_murt+50, y_murt+200, w_murt, h_murt

# help info image
help_img = pygame.image.load(
    r'Media\Icons & Graphics\help.png')
x_help, y_help, w_help, h_help = x_bar-80, y_bar+80, 340, 90
x_help, y_help, w_help, h_help = 200, 15, 340, 90
help_img = pygame.transform.scale(
    help_img, (w_help, h_help))  # for resizing the image


def lion_lab_banner():
    screen.blit(lion_lab_img, (x_lion_lab, y_lion_lab))


def text_objects(text, font):
    black = (0, 0, 0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# for text and colour of the font
def header_colour(text, font):
    colour = colour_HU_brown
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def def_colour_2(text, font):
    colour = (128, 0, 0)
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def def_colour_3(text, font):
    colour = (0, 0, 0)
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


# creating general button function
def button(msg, x, y, w, h, i, a):
    mouse = pygame.mouse.get_pos()
    # click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        start_button = pygame.draw.rect(
            screen, i, (x, y, w, h))
        # if click[0] == 1 and action != None:
        # action()
    else:
        start_button = pygame.draw.rect(
            screen, a, (x, y, w, h))

    ButtonText = pygame.font.Font(r"Media\Font\impact.ttf", 30)
    textSurf, textRect = text_objects(msg, ButtonText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


# can be used for YOU WIN / YOU LOSE / BAR RAISED / BAR LOWERED & HELP

def smol_button(msg, x, y, w, h, i, a):
    mouse = pygame.mouse.get_pos()
    # click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        start_button = pygame.draw.rect(
            screen, i, (x, y, w, h))
        # if click[0] == 1 and action != None:
        # action()
    else:
        start_button = pygame.draw.rect(
            screen, a, (x, y, w, h))

    ButtonText = pygame.font.Font(r"Media\Font\impact.ttf", 10)
    textSurf, textRect = text_objects(msg, ButtonText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


def display_prompt(img, coords=(140,  50)):
    running = True
    while running:
        for event in pygame.event.get():
            screen.blit(img, (coords[0], coords[1]))
            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                break


bar_pos = 0
character = "psych"
options_dict = {3: "Rest", 2: "Productivity", 1: "SEL"}


def game_over(msg):
    global bar_pos
    bar_pos = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # checking for mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # if the mouse is clicked on the
                # button the game is terminated
                if 350 <= mouse[0] <= 350+140 and 500 <= mouse[1] <= 500+40:
                    second_menu()

        # Background colour
        screen.fill(colour_HU_dpurple)
        # background image
        lion_lab_banner()

        # using button function
        start_pos_x = 350
        start_pos_y = 500
        button("Replay?", start_pos_x, start_pos_y, 120, 50, light_green, red)

        largeText = pygame.font.Font(
            r'Media\Font\Cooper Black Italic.otf', 40, bold=False,  italic=True)
        TextSurf, TextRect = header_colour(msg, largeText)
        TextRect.center = ((800/2), (600/2))
        screen.blit(TextSurf, TextRect)

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(15)

        pygame.display.update()


def round_result(img, result, userchoice, computer_choice, coords=(140,  50)):
    running = True
    while running:
        for event in pygame.event.get():
            screen.fill(colour_HU_dpurple)  # light background
            pygame.draw.rect(
                screen, (colour_HU_vDpurple), (0, 100, 800, 370))  # darker background
            pygame.draw.rect(
                screen, (colour_HU_white), (0, 100, 800, 3))  # upper line
            pygame.draw.rect(
                screen, (colour_HU_white), (0, 470, 800, 3))  # lower line

            if character == "mystique":  # character is mystique
                screen.blit(mystique_pic, (515, 50))
            elif character == "inverto":  # character is inverto
                screen.blit(inverto_pic, (515, 50))
            else:  # character is psyche
                screen.blit(psych_pic, (515, 50))

            # print result at top of screen
            largeText = pygame.font.Font(
                r'Media\Font\impact.ttf', 30, bold=False,  italic=True)
            TextSurf, TextRect = def_colour_3(
                str(result), largeText)
            TextRect.center = ((400), (40))
            screen.blit(TextSurf, TextRect)

            # blits at leftmost position
            screen.blit(instr_pic, (40, 50+100))
            # UPDATES BAR POSITION
            screen.blit(bar_img_lib[bar_pos], (x_bar, y_bar))

            # shows player choices
            button(options_dict[userchoice], x_zain, y_zain, w_zain, h_zain, yellow,
                   yellow)  # blits at right most position
            button(options_dict[computer_choice], 50, 400, 180, 50,
                   colour_HU_white, colour_HU_white)  # blits under instructors image
            # rest, productivity, SEL buttons(placed evenly in lower area)
            button("Rest", x_murt, rps_y_pos, w_RPS_button, h_RPS_button,
                   colour_HU_lpurple, colour_HU_brown)
            button("Productivity", x_sam, rps_y_pos, w_RPS_button, h_RPS_button,
                   colour_HU_lpurple, colour_HU_brown)
            button("SEL Scores", x_zain, rps_y_pos, w_RPS_button, h_RPS_button,
                   colour_HU_lpurple, colour_HU_brown)
            smol_button("?", 10, 15, 30, 30,
                        colour_HU_white, colour_help_blue)
            screen.blit(img, (coords[0], coords[1]))
            pygame.display.flip()
            pygame.display.update()
            # time.sleep(0.1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                break


def rps(userchoice):
    global bar_pos
    # 3 = Rest
    # 2 = Productivity
    # 1 = SEL Score

    computer_choice = random.randint(1, 3)
    if computer_choice == 3 and userchoice == 1:  # Instructor is resting, you have SEL
        bar_pos -= 1
        result = "lose"
        round_result(img_prompt_lose_R_S, result, userchoice,
                     computer_choice)  # insert images
    elif computer_choice == 2 and userchoice == 3:
        bar_pos -= 1
        result = "lose"
        round_result(img_prompt_lose_P_R, result, userchoice, computer_choice)
    elif computer_choice == 1 and userchoice == 3:
        bar_pos -= 1
        result = 'lose'
        round_result(img_prompt_lose_R_S, result, userchoice, computer_choice)
    elif computer_choice == 3 and userchoice == 2:
        bar_pos += 1
        result = "win"
        round_result(img_prompt_win_P_R,  result, userchoice, computer_choice)
    elif computer_choice == 2 and userchoice == 1:
        bar_pos += 1
        result = "win"
        round_result(img_prompt_win_S_P, result, userchoice, computer_choice)
    elif computer_choice == 1 and userchoice == 2:
        bar_pos += 1
        result = "win"
        round_result(img_prompt_win_S_P, result, userchoice, computer_choice)
    elif computer_choice == 1 and userchoice == 1:
        result = "draw"
        round_result(img_prompt_draw_SS, result, userchoice, computer_choice)
    elif computer_choice == 2 and userchoice == 2:
        result = "draw"
        round_result(img_prompt_draw_PP, result, userchoice, computer_choice)
    elif computer_choice == 3 and userchoice == 3:
        result = "draw"
        round_result(img_prompt_draw_RR, result, userchoice, computer_choice)

    return (result,  computer_choice)


def game_screen(char="psych"):  # 3rd window - The actual game screen; psych as default
    global bar_pos
    global character
    character = char
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():  # keeps running for everytick of the clock
            if event.type == pygame.QUIT:  # the condition for exiting the gamescreen
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # if the mouse is clicked on the
                # button the game is terminated
                print(mouse)

                click_on_help = 10 <= mouse[0] <= 10 + \
                    30 and 15 <= mouse[1] <= 15+30
                click_on_rest = x_murt <= mouse[0] <= x_murt + \
                    w_RPS_button and rps_y_pos <= mouse[1] <= rps_y_pos + \
                    h_RPS_button
                click_on_prod = x_sam <= mouse[0] <= x_sam + \
                    w_RPS_button and rps_y_pos <= mouse[1] <= rps_y_pos + \
                    h_RPS_button
                click_on_SELs = x_zain <= mouse[0] <= x_zain + \
                    w_RPS_button and rps_y_pos <= mouse[1] <= rps_y_pos + \
                    h_RPS_button

                if click_on_help:  # shows help
                    display_prompt(help_img, (x_help, y_help))
                elif click_on_rest:  # r = 3
                    # display_prompt(img_prompt_lose_R_S, (140, 50))
                    userchoice = int(3)
                    result, computer_choice = rps(userchoice)
                    game_screen(character)
                elif click_on_prod:
                    userchoice = int(2)  # in options_dict Productivity = 2
                    # print(userchoice)
                    result, computer_choice = rps(userchoice)
                    game_screen(character)
                    break
                elif click_on_SELs:  # s = 1
                    userchoice = int(1)
                    result, computer_choice = rps(userchoice)
                    game_screen(character)
                    break
            if bar_pos >= 2:
                time.sleep(1)
                running = False
                game_over("Yay! You raised the bar!")
            if bar_pos <= -2:
                time.sleep(1)
                running = False
                game_over("Bar lowered... sadly.")
        # aesthetic additions:
        screen.fill(colour_HU_dpurple)  # light background
        pygame.draw.rect(
            screen, (colour_HU_vDpurple), (0, 100, 800, 370))  # darker background
        pygame.draw.rect(
            screen, (colour_HU_white), (0, 100, 800, 3))  # upper line
        pygame.draw.rect(
            screen, (colour_HU_white), (0, 470, 800, 3))  # lower line

        if character == "mystique":  # character is mystique
            screen.blit(mystique_pic, (515, 50))
        elif character == "inverto":  # character is inverto
            screen.blit(inverto_pic, (515, 50))
        else:                         # character is psyche
            screen.blit(psych_pic, (515, 50))

        largeText = pygame.font.Font(
            r'Media\Font\impact.ttf', 30, bold=False,  italic=True)
        TextSurf, TextRect = def_colour_3(
            "Pick your option!", largeText)
        TextRect.center = ((400), (40))
        screen.blit(TextSurf, TextRect)

        # blits at leftmost position
        screen.blit(instr_pic, (40, 50+100))
        screen.blit(bar_img_lib[bar_pos], (x_bar, y_bar))

        button("You", x_zain, y_zain, w_zain, h_zain, yellow,
               yellow)  # blits at right most position
        button("Instructor", 50, 400, 180, 50,
               colour_HU_white, colour_HU_white)  # blits under instructors image
        # rest, productivity, SEL buttons (placed evenly in lower area)
        button("Rest", x_murt, rps_y_pos, w_RPS_button, h_RPS_button,
               colour_HU_lpurple, colour_HU_brown)
        button("Productivity", x_sam, rps_y_pos, w_RPS_button, h_RPS_button,
               colour_HU_lpurple, colour_HU_brown)
        button("SEL Scores", x_zain, rps_y_pos, w_RPS_button, h_RPS_button,
               colour_HU_lpurple, colour_HU_brown)
        smol_button("?", 10, 15, 30, 30,
                    colour_HU_white, colour_help_blue)  # help button

        pygame.display.flip()

        clock.tick(60)
        pygame.display.update()


def second_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # checking for mouseclicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # if the mouse is clicked on the
                # button the game is terminated
                click_on_psych = x_murt <= mouse[0] <= x_murt + \
                    w_murt and y_murt <= mouse[1] <= y_murt+h_murt
                click_on_inverto = x_zain <= mouse[0] <= x_zain + \
                    w_zain and y_zain <= mouse[1] <= y_zain+h_zain
                click_on_mystique = x_sam <= mouse[0] <= x_sam + \
                    w_sam and y_sam <= mouse[1] <= y_sam+h_sam
                if click_on_psych:
                    # run gamescreen with "psych" character
                    game_screen("psych")
                elif click_on_inverto:
                    game_screen("inverto")
                elif click_on_mystique:
                    game_screen("mystique")

        # Background colour
        bg_colour = colour_HU_dpurple
        screen.fill(bg_colour)

        # print Murtaza's image
        screen.blit(psych_pic, (15, 50))
        # print Samin's image
        screen.blit(mystique_pic, (265, 50))
        # print Zain's image
        screen.blit(inverto_pic, (515, 50))

        # murtaza's button (char 1)
        # when cursor ON, turn (magenta); otherwise stay (yellow)
        button("Psych", x_murt, y_murt, w_murt, h_murt, magenta, yellow)
        # button for revealing the power
        button(" ", 10, 460, 258, 30, magenta, maroon)
        # text/power that reveals
        largeText = pygame.font.Font(
            r'Media\Font\Cooper Black Italic.otf', 15, bold=False,  italic=True)
        TextSurf, TextRect = def_colour_2(
            "Flips opponent's choice after turn", largeText)
        TextRect.center = ((140), (480))
        screen.blit(TextSurf, TextRect)

        # samin's button (Char 2)
        button("Mystique", x_sam, y_sam, w_sam, h_sam, blue, yellow)
        # button for revealing the power
        button(" ", 280, 460, 231, 30, blue, maroon)
        # text/power that reveals
        largeText = pygame.font.Font(
            r'Media\Font\Cooper Black Italic.otf', 15, bold=False,  italic=True)
        TextSurf, TextRect = def_colour_2(
            "Has a super mystery POWER!", largeText)
        TextRect.center = ((395), (480))
        screen.blit(TextSurf, TextRect)

        button("Inverto", x_zain, y_zain, w_zain, h_zain, orange, yellow)
        # button for revealing the power
        button(" ", 525, 460, 267, 30, orange, maroon)
        # text/power that reveals
        largeText = pygame.font.Font(
            r'Media\Font\Cooper Black Italic.otf', 15, bold=False,  italic=True)
        TextSurf, TextRect = def_colour_2(
            "Flips opponent's choice before turn", largeText)
        TextRect.center = ((659), (480))
        screen.blit(TextSurf, TextRect)

        # FOR "DISCLOSE THE POWER" TEXT on TOP
        largeText = pygame.font.Font(
            r'Media\Font\impact.ttf', 30, bold=False,  italic=True)
        TextSurf, TextRect = def_colour_3(
            "Choose your identity:", largeText)
        TextRect.center = ((400), (40))
        screen.blit(TextSurf, TextRect)

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

        pygame.display.update()


# First Screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # checking for mouseclicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            # if the mouse is clicked on the
            # button the game is terminated
            if 350 <= mouse[0] <= 350+140 and 500 <= mouse[1] <= 500+40:
                second_menu()

    # Background colour
    screen.fill(colour_HU_dpurple)
    # background image
    lion_lab_banner()

    # using button function
    start_pos_x = 350
    start_pos_y = 500
    button("Start!", start_pos_x, start_pos_y, 120, 50, light_green, red)

    largeText = pygame.font.Font(
        r'Media\Font\Cooper Black Italic.otf', 70, bold=False,  italic=True)
    TextSurf, TextRect = header_colour("RAISE THE BAR!", largeText)
    TextRect.center = ((800/2), (600/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.flip()

    pygame.display.update()
