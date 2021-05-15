import sys
import pygame

pygame.init()
clock = pygame.time.Clock()

#Screen
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HU Kabootars les gooo')
        #BAckground_start_menu
background = pygame.image.load(r"images\Kabootars\kabbu.jpg")
background2 = pygame.image.load(r'images\Kabootars\memekabootar.jpg')
        #Music
pygame.mixer.music.load('sounds/kabbu.mp3') #('file location')
pygame.mixer.music.play(-1) #-1 so it plays in a loop
        #font
font = pygame.font.Font(r'Fonts\Fipps-Regular.otf',30)
small_font = pygame.font.Font(r'Fonts\Fipps-Regular.otf',10)

def start_menu():
    hellotext = font.render('Hello',True, 'white')
    running = True
    while True: #keeps running after called
        pygame.event.get()
        screen.fill("black")  #default colour
        # screen.blit(hellotext,(5,5))    #test text
        screen.blit(background,(-500,-100)) #blit the background

        button_text = font.render("Start!",True,'White') # start button text
        start_button = create_button(700,150,button_text.get_width()+ 10,button_text.get_height() + 10,'Gold','Purple')
        screen.blit(button_text,(700,150)) # start button blit on screen

        credit_text = font.render("Credits",True,'White')
        credits_button = create_button(800,300,credit_text.get_width(),credit_text.get_height(),'Gold','Purple')
        screen.blit(credit_text,(800,300))
        
        if credits_button:
            credit()


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

def credit(): # goes to credit screen (includes back button)
    running = True
    while running:
        pygame.event.get()
        screen.fill('Black')
        screen.blit(background,(-500,-100))
        
        credits_1 = font.render('Zain Ahmed Usmani',True,'White')
        credits_2 = font.render('Sudais Yasin',True,'White')
        credits_3 = font.render('Murtaza Ali Khokhar',True,'White')
        pygame.draw.rect(screen,'Gold',(300,200,credits_3.get_width(),credits_3.get_height()))
        pygame.draw.rect(screen,'Gold',(300,300,credits_3.get_width(),credits_3.get_height()))
        pygame.draw.rect(screen,'Gold',(300,400,credits_3.get_width(),credits_3.get_height()))
        screen.blit(credits_1,(300,200))
        screen.blit(credits_2,(300,300))
        screen.blit(credits_3,(300,400))

        back = font.render('BACK',True,'White')
        back_button = create_button(100,100,back.get_width(),back.get_height(),'Gold','Purple')
        screen.blit(back,(100,100))

        if back_button:
            running = False
            start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(15)

def player_select(): # second screen
    running = True
    userNameText = ''
    nameBarActive = False
    while running:
        pygame.event.get()
        screen.fill('Black')
        # screen.blit(background2,(0,0))
        single_player_text = font.render('1 player',True,'White') # single player mode text
        double_player_text = font.render('2 players',True,'White') # dual player mode text

        player_select_prompt = font.render('How many players will be playing?',True,'White') # prompt text
        constraint = font.render('(In Numbers)',True,'White')
        screen.blit(constraint,(400,300))
        screen.blit(player_select_prompt,(125,200))

        userNameSurface = font.render(userNameText,True,'White')
        userNameBorder = pygame.Rect(500, 500, userNameSurface.get_width() + 50, 50)
        screen.blit(userNameSurface, (500, 500)) # borders of the text input
        pygame.draw.rect(screen, 'White', userNameBorder, 2)

        # single_player = create_button(150,500,single_player_text.get_width(),single_player_text.get_height(),'Gold','Purple')
        # screen.blit(single_player_text,(150,500)) # single player button blit

        # if single_player: # move to single player mode
        #     running = False
        #     game()
        
        # double_player = create_button(450,500,double_player_text.get_width(),double_player_text.get_height(),'Gold',"Purple")
        # screen.blit(double_player_text,(450,500)) # double player button blit

        # if double_player: # move to double player mode
        #     game(2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if userNameBorder.collidepoint(event.pos):
                    # print('HELO')
                    nameBarActive = True # lets us know if the click was made inside the name box
                else:
                    nameBarActive = False
            if event.type == pygame.KEYDOWN:
                if nameBarActive:
                    if event.key == pygame.K_BACKSPACE:
                        userNameText = userNameText[:-1]
                    elif event.key == pygame.K_RETURN:
                        playerAmount = userNameText
                        game()
                    else:
                        userNameText += event.unicode

        pygame.display.update()
        clock.tick(100000000000000)

# runner
running = True
while running:
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(15)
