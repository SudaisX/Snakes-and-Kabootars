def get_gender():
    gender = input("Select gender: M/F?")
    if gender == "Male" or gender == "Male".lower() or gender == "Male".upper or gender == "M" or gender == "m":
        pronoun = "M"
    else:  # keeps us from having too many unintended glitches on a fairly unimportant part of the program
        pronoun = "F"
    return pronoun


def get_name():
    player = input("What is your name?")
    return player


def __main__():
    pronoun = get_gender()
    batch = get_batch()
    player = get_name()

    """
    NOTE: make all events mutually-exclusive, such that the previous one
    is only linked to the next one by the user's imagination, not by code.
    On tiles 1-10:
        You get the narratives of getting into uni:
            You joined HU because your parents forced you to join HU
            You joined HU as a HU fan
            You joined HU because you got sold on the HU mission
            You joined HU because you wanted to be able to relate with liberal Shitposting Posts so joined HU
            You joined HU because
            (if any of the above twice... let's add a "You also ... ")
        6-10:
            You got a 100& scholarship at HU - ~now all you gotta do is keep that 3.5 CGPA~
            You got a scholarship at HU, but you rejected it 'cause you gotta flex daddy's money
            You didn't get a scholarship at HU, you gonna be broke, but hey at least you're now part of the Liberal Naala :)
            You you got a scholarship at HU, but you know you goin' broke over overpriced coffee (in all seriousness this isn't too bad as far as overpricing goes)

        Random:
            Graduting
            Getting a job
            Getting an internship
            Rahim bhai kay fries
            NSO
                Insert OL Name function? + text messages of you asking that OL for help all the time 🤷‍♂️
            Labs?
            Grounds
            Sunsets
            Water courtyard with the kabootars
            Staying till the light turn on
            Panicking to make that 11:59 submission at 11:58


    """


lst = [1, 2, 3, 4, ..., 100]  # corresponds with each box
# dict = {1 to 100} #no.
P1 = Player()
P1.pos(0)  # startings at 0
P1.move()


def move(pos):
    pos = prev_pos + kismat  # kismat = dice_roll
    # khabootars = [(98, 70), (20, 5), .. (khabootars_poop, restroom)]
    if pos in khabootars:
        # insert code for finding khabootar_poop in khabootars with khabootar_poop[0] == pos
        pos = correct_snake_head[1]
    # habootars = [(58, 70), (13, 40), .. (ladder_bottom, ladder_top), (habootar_and_you, habootars_nest)]
    if pos in habootars:
        # insert code for finding nest in habootars_nest with nest[0] == pos
        pos = correct_habootars_nest[1]


print(snek-head[0])
output: (5, 3)
if pos == lst[snake_1]:
    pos = new_position

dict_player_coords = {}
dict_snakes_and_habootars = {}

movement = dice_roll()
