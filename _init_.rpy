init python:
    import os
    from functools import partial
    import logging
    from itertools import chain

    ####### PATHS #####

    GAME_PATH = "/home/akechi/lajno/frizzzz/game"
    IMAGES_PATH = os.path.join(GAME_PATH, "images")

    CHARACTER_PATH = lambda c, prefix='': os.path.join(IMAGES_PATH, c, prefix)
    CHARACTER_MOUTH_PATH = lambda c: CHARACTER_PATH(c, "mouth")


    ##### CHARACTERS CONSTS ######

    START_POS_FRIZ = Position(xpos=0.3)
    START_POS_NOWCIAX = Position(xpos=0.7)
    MOUTH_ANIMATION_PAUSE = 0.2


    ###### FUNCTIONS ######

    def char_talking(character, event, **kwargs):
        if event == ("end" or "slow_down"):
            renpy.show("{} closed".format(character))
        elif event=="show":
            renpy.show("{} open".format(character))

    def usta_animation(character):
        usti_files = [os.path.splitext(f)[0] for f in os.listdir(CHARACTER_MOUTH_PATH(character))]
        return list(chain.from_iterable([[f, MOUTH_ANIMATION_PAUSE] for f in usti_files]))


    ###### TRANSITIONS AND TRANFORMATIONS ######

    define.move_transitions("ease", 0.6)
    alpha_transform = lambda x: Transform(alpha=x)


###### CONFIG ######

define config.automatic_images = ['/']
define config.automatic_images_strip = ['images']


## GUI

define gui.text_font = os.path.join("gui", "Ubuntu-Regular.ttf")
define gui.name_text_font = os.path.join("gui", "Hey Haters.ttf")
define gui.text_size = 25
define gui.name_text_size = 45
define gui.dialogue_xpos = 400


## STYLE

style window:
    background Frame(os.path.join("gui", "textbox", "dq.png"))
    yalign 1.0
    ysize 300

style namebox:
    xalign 0.2
    yalign 0.14

style say_label:
    properties gui.text_properties("name", accent=True)

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 300
    yalign 0.6
    xsize gui.dialogue_width
