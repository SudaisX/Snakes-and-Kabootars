import pygame
import random

pygame.init()

WIDTH = 1080
HEIGHT = 720
COLOURS_ = ('#32a852', '#a83157', '#2e2ea3', '#a69430', '#a32f2f', '#772d9c')
COLOURS = []  # Use HU_Theme colours for final version
for colour in COLOURS_:
    COLOURS.append(pygame.Color(colour))
ARROW_IMG = pygame.image.load(
    r'F:\Documents\GitHub\Snakes-and-Kabootars\images\Graphics\arrow.png')
TAB_HEIGHT = 40
TAB_WIDTH = 100
num_font = pygame.font.Font(None, 20)
tabs = {}

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Qismat Function")
clock = pygame.time.Clock()


def assign_tabs(tabs, x, y):
    """
    Initializes the tabs_dictionary
    tabs[dice_roll] = (x_coord of blit, y_coord of blit + TAB_HEIGHT)
    """

    d_rolls = []  # this block of code can be commented out
    # and some modifications can be made to get tabs that are in fixed orders
    while (len(d_rolls) != 6):
        roll = random.randint(1, 6)
        if roll not in d_rolls:
            d_rolls.append(roll)

    for index in range(6):
        tabs[d_rolls[index]] = (x, y + TAB_HEIGHT*(index+1))
    return tabs


def render_tabs(tabs, x, y):
    """
    x, y -> (x,y) coordinates of the top left pixel of the arrow
    """
    if len(tabs) == 0:
        tabs = assign_tabs({}, x, y)
    # print(tabs)
    cum_height = 0
    x_spacing = ARROW_IMG.get_size()[0] + 5
    # print(x_spacing)
    x_tab_begin, x_tab_end = x + x_spacing, x + x_spacing + TAB_WIDTH
    for bar in tabs:

        tab = pygame.draw.rect(
            gameDisplay, COLOURS[bar-1],
            [x_tab_begin, y+cum_height, TAB_WIDTH, TAB_HEIGHT])
        roll = num_font.render(str(bar), True, "White")
        roll_rect = roll.get_rect(center=tab.center)
        gameDisplay.blit(roll, roll_rect)
        cum_height += TAB_HEIGHT
    return tabs


def arrow(arrow_img, start_x, start_y):
    gameDisplay.blit(arrow_img, (start_x, start_y))


def qismat_function(x, y):
    # tabs = assign_tabs({}, 0, 0)
    # x, y = 0, 0
    global tabs
    tabs = render_tabs(tabs, x, y)
    attempted = False
    attempted_ = False
    motion = +1
    y_pos = y
    while not attempted:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:  # You click when you leave the button
                if event.key == pygame.K_SPACE:
                    attempted_ = True
        gameDisplay.fill("Black")
        render_tabs(tabs, x, y)
        arrow(ARROW_IMG, x, y_pos - 16)
        if motion == +1:
            height_change = 5
        elif motion == -1:
            height_change = -5
        y_pos += height_change

        if y_pos > y+TAB_HEIGHT*6:
            motion = -1
        elif y_pos < y:
            motion = +1

        if attempted_:
            return y_pos
            attempted = True
        pygame.display.update()
        clock.tick(120)


# print(qismat_function(0, 0))

def qismat_calc(stopping_height):  # The main basically
    tabs[0] = (0, 0)
    print("stoppingHeight:", stopping_height)
    print(tabs)
    for roll in tabs:
        if tabs[roll][1] >= stopping_height and stopping_height > tabs[roll-1][1]:
            print("Roll:", roll)
            print("Range:", tabs[roll][1], tabs[roll-1][1])
            return roll


print(qismat_calc(qismat_function(0, 300)))
