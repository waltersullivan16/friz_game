# FRIZ
init python:
    class Characterr:
        def __init__(self, name, who_color='#000000'):
            self.capital_name = name.upper()
            self.name = name.lower()
            self.mouth_pos = COMPOSITION[name]["mouth"]
            self.pos = COMPOSITION[name]["start"]
            self.who_color = who_color

            self.char = Character(name=self.capital_name, callback=partial(char_talking, self), who_color=who_color)

            self.talking = False
            self.layeredimage = None

        def __str__(self):
            return self.name

        @property
        def coordinates(self):
            position_array = renpy.get_image_bounds(self.image)
            print(position_array)
            return [position_array[0], position_array[2]]

        @property
        def mouth(self):
            return Animation(*mouth_animation(self.name))
        x = LayeredImage([Attribute("test", "main", "reaction_sweatdrop")])

##### FRIZ #####

define FrizClass = Characterr("FRIZ")
define Friz = FrizClass.char

layeredimage friz:
    group body auto:
        attribute main default

    group reaction:
        attribute normal default null
        attribute luv:
            "reaction_luv"
        attribute angry:
            "reaction_angry"

    if FrizClass.talking:
        FrizClass.mouth at FrizClass.mouth_pos


### NOWCIAX ###

define NowciaxClass = Characterr("NOWCIAX")
define Nowciax = NowciaxClass.char

layeredimage nowciax:
    group body auto:
        attribute main default

    group reaction:
        attribute normal default null
        attribute luv:
            "reaction_luv"
        attribute angry:
            "reaction_angry"

    if NowciaxClass.talking:
        NowciaxClass.mouth at NowciaxClass.mouth_pos
