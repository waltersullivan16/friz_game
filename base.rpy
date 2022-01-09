init python:
    from functools import partial
    import os
    import logging
    from itertools import chain

    ## PATHS
    GAME_PATH = "/home/akechi/lajno/frizzzz/game"
    IMAGES_PATH = os.path.join(GAME_PATH, "images")
    CHARACTER_MOUTH_PATH = lambda c: os.path.join(IMAGES_PATH, c, "mouth")

    ## CONST
    START_POS_FRIZ = Position(xpos=0.3)
    START_POS_NOWCIAX = Position(xpos=0.7)

    MOUTH_ANIMATION_PAUSE = 0.2

    ## FUNCTIONS
    def char_talking(character, event, **kwargs):
        print("dadadsadsadada", character)
        if event == ("end" or "slow_down"):
            renpy.show("{} closed".format(character))
        elif event=="show":
            renpy.show("{} open".format(character))

    ## TRANSITIONS
    define.move_transitions("ease", 0.6)

    alpha_transform = lambda x: Transform(alpha=x)
