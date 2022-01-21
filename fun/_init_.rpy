init python:
    import os
    from functools import partial
    import logging
    from itertools import chain

    ####### PATHS #####

    GAME_PATH = "/home/akechi/lajno/frizzzz/game"
    IMAGES_PATH = os.path.join(GAME_PATH, "images")

    FONTS_PATH = os.path.join("gui", "fonts")
    TEXTBOX_PATH = os.path.join("gui", "textbox")

    CHARACTER_PATH = lambda c, prefix='': os.path.join(IMAGES_PATH, c, prefix)
    CHARACTER_MOUTH_PATH = lambda c: CHARACTER_PATH(c, "mouth")
    CHARACTER_ANIMATION_PATH = lambda c: CHARACTER_PATH(c, "animation")


    ##### CHARACTERS CONSTS ######

    START_POS_FRIZ = Position(xpos=0.3)
    START_POS_NOWCIAX = Position(xpos=0.7)
    MOUTH_ANIMATION_PAUSE = 0.2

    FRIZ_MOUTH_POSITION = Position(xpos=452,ypos=213)
    NOWCIAX_MOUTH_POSITION = Position(xpos=465,ypos=203)

    ###### FUNCTIONS ######

    def char_talking(character, event, **kwargs):
        print("[start] chatacer {} event {}".format(renpy.get_attributes(character.name), event))
        if event == "show":
            character.talking = True
            renpy.music.play("music/blip.mp3", channel="sound", loop="True")
        elif event in ["end", "slow_done"]:
            character.talking = False
            renpy.music.stop(channel="sound")
        print("[stop] chatacer {} event {}".format(renpy.get_attributes(character.name), event))

    def animation(character, animation_path, animation_name):
        files = [os.path.splitext(f)[0].split(" ") for f in os.listdir(animation_path(character))]
        print(files)
        files = list(filter(lambda f: f[0] == character and f[1] == animation_name, files))
        print(files)
        return list(chain.from_iterable([[' '.join(f), MOUTH_ANIMATION_PAUSE] for f in files]))

    mouth_animation = lambda c: animation(c, CHARACTER_MOUTH_PATH, "usti")


    ###### TRANSITIONS AND TRANFORMATIONS ######
#
#    alpha_transform = lambda x: Transform(alpha=x)
#    define.move_transitions("ease", 1.6)
#
#define spritechange = MultipleTransition([
#    False, Dissolve(1.0), True])
#
transform dropping:
    linear 1.5 yanchor -100
    pause 3.0

transform beating:
    zoom 1.2
    pause 0.2
    zoom 1.0
    pause 0.2
    repeat


###### CONFIG ######

define config.automatic_images = ['/']
define config.automatic_images_strip = ['images']

###### GUI ######
define FONT_CHERI = os.path.join(FONTS_PATH, "CHERI___.TTF")
define gui.text_font = os.path.join(FONTS_PATH, "Ubuntu-Regular.ttf")
define gui.name_text_font = os.path.join(FONTS_PATH, "Bubblegum.ttf")
define gui.text_size = 25
define gui.name_text_size = 55

#define _preferences.show_empty_window = True

####### STYLE ######

style window:
    background Frame(os.path.join(TEXTBOX_PATH, "db.png"))
    yalign 1.05
    ysize 300

style namebox:
    xalign 0.05
    yalign 0.16

style say_label:
    properties gui.text_properties("name", accent=True)

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 100
    yalign 0.6
    xsize gui.dialogue_width

style bum:
    font FONT_CHERI
    size 50
    xanchor 0.5 yanchor 0.5
image top_text = ParameterizedText(style="bum")

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define punch_flash = MultipleTransition([
        False, hpunch,
        False, Pause(0.2),
        False, hpunch,
        False, Pause(0.3),
        False, flash,
        False, Pause(0.3),
        False, hpunch,
        False, Pause(0.2),
        False, flash,
        True])
define BUBBLE = "bubble.png"
init python:
    def comic_text(text, bubble=BUBBLE):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), Text(text, style="bum"))#"top_text \"{}\"".format(text))

image tt = comic_text("dsadasd")
