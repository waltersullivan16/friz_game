init -10 python:
    import os
    from functools import partial
    import logging
    from itertools import chain

    ####### CONSTS #####


    ## PATHS ##

    GAME_PATH = "/home/akechi/lajno/frizzzz/game"
    IMAGES_PATH = os.path.join(GAME_PATH, "images")
    TEXTBOX_PATH = os.path.join("gui", "textbox")

    ## CHARACTERS ##

    get_character_path = lambda c, prefix='': os.path.join(IMAGES_PATH, c, prefix)
    get_character_animation_path = lambda c: os.path.join(IMAGES_PATH, c, "animations")

    ANIMATION_PAUSE = 0.2

    COMPOSITION = {}
    COMPOSITION["FRIZ"] = {
        "start": Position(xpos=0.3),
        "mouth": Position(xpos=452, ypos=213),
    }

    COMPOSITION["NOWCIAX"] = {
        "start": Position(xpos=0.6),
        "mouth": Position(xpos=465, ypos=203)
    }

    ## FONTS ##

    FONTS_PATH = os.path.join("gui", "fonts")
    get_font = lambda font: os.path.join(FONTS_PATH, font)

    FONT_CHERI = get_font("CHERI___.TTF")
    FONT_UBUNTU = get_font("Ubuntu-Regular.ttf")
    FONT_BUBBLEGUM = get_font("Bubblegum.ttf")

    FONT_SIZE = 25
    FONT_SIZE_NAME = 55

    FONT_TEXT = FONT_UBUNTU
    FONT_NAME = FONT_BUBBLEGUM

    AUTOMATIC_IMAGES = ["/"]
    AUTOMATIC_IMAGES_STRIP = ["images"]

    ###### FUNCTIONS ######

    BUBBLE = "bubble.png"

    def char_talking(character, event, **kwargs):
        #print("[start] chatacer {} event {}".format(renpy.get_attributes(character.name), event))
        if event == "show":
            character.talking = True
            renpy.music.play("music/blip.mp3", channel="sound", loop="True")
        elif event in ["end", "slow_done"]:
            character.talking = False
            renpy.music.stop(channel="sound")
        #print("[stop] chatacer {} event {}".format(renpy.get_attributes(character.name), event))


    def animation_maker(character, animation_name, animation_pause=ANIMATION_PAUSE):
        files = [os.path.splitext(f)[0].split(" ") for f in os.listdir(get_character_animation_path(character))]
        files = list(filter(lambda f: f[0] == character and f[1] == animation_name, files))
        return list(chain.from_iterable([[' '.join(f), animation_pause] for f in files]))

    def emotion_maker(character, emotion):
        arr = list(map(lambda x: int(x), renpy.get_image_bounds(character)))
        renpy.show(emotion, atl=Position(arr[0], arr[2]))

    def comic_text_maker(text, bubble=BUBBLE):
        return LiveComposite(
            renpy.image_size(bubble),
            (0, 0), bubble,
            (0.0, 0.0), Text(text, style="bum"))#"top_text \"{}\"".format(text))

    mouth_animation = lambda c: animation_maker(c, "mouth")

    ###### TRANSITIONS AND TRANFORMATIONS ######
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

image tt = comic_text_maker("dsadasd")
