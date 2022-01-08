### PATHS

###   CHARACTERS   ###
init python:
    class CharacterBase:
        def __init__(self):
            pass

        @property
        def get_talking_sprite(character, mood):
            return "{} {}_talking".format(character.name.name, mood)



# STATIC #

define Friz = Character("FRIZ", image="frizl", callback=partial(char_talking, 'friz'), talking=False, who_color='#000000')
define Nowciax = Character("NOWCIAX", image="nowciax", callback=partial(char_talking, 'nowciax'), talking=False, who_color='#05232f')

#image friz = wh
#define e = Character("Eileen", callback=partial(char_pulse, "eileen")

define pos_friz = Position(xpos=0.3)
define pos_nowciax = Position(xpos=0.7)

# ANIMATION #

image friz main_talking = Animation(*make_animation("friz", "main"))
image nowciax main_talking = Animation(*make_animation("nowciax", "main"))
image friz otoja_talking = Animation(*make_animation("friz", "otoja"))


image vid ekipup = Movie("ekipup.mkv", (0,0), (0,0))
image background bedroom blurr = im.Blur("background/bedroom.png", 1.5)

layeredimage frizl:
    group body:
        attribute maini:
            "friz main"
        attribute otoja_talking:
            "friz otoja"

    group mouth:
        attribute open:
            "usti"

    group emotion:
        attribute angry:
            "sweatdropp"

image fr = LiveComposite(
    (600,600),
    (0,0), "friz main",
    (20,20), ConditionSwitch(
    "abla=='a'", "usti",
    "'True'", "sweatdrop"
    )
   )

transform a:
    xpos 1000
    linear 1 yanchor -400
    pause 2
    repeat


image t:
    alpha 1.0
    "usti"
    0.1
    alpha 0.0
    0.1
    repeat
image sweatdropp = At("sweatdrop", a)

image ss = VBox(
    "friz main",
    "sweatdropp")
