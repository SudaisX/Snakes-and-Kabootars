import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

#Screen
WIDTH = 800
HEIGHT = 650
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HU Kabootars les gooo')
        #BAckground_start_menu
background = pygame.image.load(r"images\Kabootars\kabbu.jpg")
        #font
font = pygame.font.Font(r'Fonts\Fipps-Regular.otf',20)

def start_menu():
    hellotext = font.render('Hello',True, 'white')
    running = True
    while True: #keeps running after called
        pygame.event.get()
        screen.fill("black")  #default colour
        # screen.blit(hellotext,(5,5))    #test text
        screen.blit(background,(-500,-100)) #blit the background

        button_text = font.render("Start!",True,'White') # start button text
        start_button = create_button(500,50,button_text.get_width(),button_text.get_height(),'Gold','Purple')
        screen.blit(button_text,(500,50))

        if start_button:
            player_select()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        pygame.display.update()
        clock.tick(15)
        return True

def create_button(x, y, width, height, activecolor, inactivecolor): # text = what to write, x = position along x of top left corner of text, y = position along y of top left corner of text, width = width of button, height = height of button, actovecolor = color when hovering, inactivecolor = color when dormant
    cursor = pygame.mouse.get_pos()     #stores the position of the cursor in tuple (x,y)
    click = pygame.mouse.get_pressed(3) #senses when clicked return a tuple of (x,y)

    if (x + width) > cursor[0] > x and (y + height) > cursor[1] > y:    #if my mouse is on the button
        pygame.draw.rect(screen,activecolor,(x,y,width,height))         #light up the button
        if click[0] == 1:
            return True                                         #when the click is on the button move to player choosing screen
    else:
        pygame.draw.rect(screen, inactivecolor,(x,y,width,height)) #when not hovering keep it dormant


def player_select(): # second screen
    running = True
    while running:
        pygame.event.get()
        screen.fill('Black')  
        screen.blit(background,(-500,-100))  
        single_player_text = font.render('1 player',True,'White')
        double_player_text = font.render('2 players',True,'White')
        player_select_prompt = font.render('How many players will be playing?',True,'White')
        screen.blit(player_select_prompt,(125,300))
        single_player = create_button(150,500,single_player_text.get_width(),single_player_text.get_height(),'Gold','Purple')
        screen.blit(single_player_text,(150,500))
        double_player = create_button(450,500,double_player_text.get_width(),double_player_text.get_height(),'Gold',"Purple")
        screen.blit(double_player_text,(450,500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
        pygame.display.update()
        clock.tick(15)

# runner
running = True
while running:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(15)
