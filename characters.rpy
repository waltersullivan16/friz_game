# FRIZ
init python:
    class Characterr:
        def __init__(self, name, image, mouth_pos=Position(xpos=0, ypos=0), who_color='#000000', pos=Position(xpos=0, ypos=0)):
            self.name = name
            self.image = image
            self.mouth_pos = mouth_pos
            self.who_color = who_color
            self.char = Character(name, image=image, callback=partial(char_talking, self), who_color=who_color)
            self.talking = False

        def __str__(self):
            return self.name

        @property
        def positionn(self):
            position_array = renpy.get_image_bounds(self.image)
            print(position_array)
            return [position_array[0], position_array[2]]


layeredimage friz:
    group body auto:
        attribute main default

    group reactions auto:
        xpos 170 ypos 52
        attribute normal default null
        attribute luv:
            "reaction_luv"
        attribute angry:
            "reaction_angry"

    if FrizClass.talking:
        "friz_usta" at COMPOSITION["FRIZ"]["mouth"]

# NOWCIAX
layeredimage nowciax:
    group body auto:
        attribute main default

    group reactions auto:
        attribute normal default null

    if NowciaxClass.talking:
        "nowciax_usta" at COMPOSITION["NOWCIAX"]["mouth"]
