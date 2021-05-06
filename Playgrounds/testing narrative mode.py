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
            Water courtyard with the habootars*
                *habootars go 'hwoo hwoo', khabootars go 'pop, poop, pttt'
            Staying till the lights turn on
            Panicking to make that 11:59 submission at 11:58
            Enrolment
            [Being tolerant]
            Ranting in the townhalls
            Appreciating wholesomeness 
            [a couple of things to do with the forums?]
            Hanging out at the Student Centre (ask a sophomore or above)
            Event at the central street
            Some design workshop at the playground
            * A PANDEMIC STARTED?*
                You missed an online class
                Your schedule's a mess
                Discord/Zoom call
                SEL Scores
                Playing 
    """
