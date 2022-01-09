###   CHARACTERS   ###

# STATIC #

image fr = LiveComposite(
    (600,600),
    (0,0), "friz main",
    (20,20), ConditionSwitch(
    "abla=='a'", "friz_talking",
    "'True'", "usti"
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
init python:
    GAME_PATH = "/home/akechi/lajno/frizzzz/game"
    IMAGES_PATH = os.path.join(GAME_PATH, "images")
    MAIN_IMAGES = lambda character: os.path.join(IMAGES_PATH, character, "main")
    #ANIMATIONS_PATH = lambda character: os.path.join(IMAGES_PATH, character, "animations")
    def get_images(character, mood):
        character_path = MAIN_IMAGES(character)
        try:
            files_names = [os.path.splitext(f)[0] for f in os.listdir(character_path) if f.endswith('png')]
        except e:
            raise Exception("[{}] file with incorrect format in images".format(character))
        res = []

        for file in files_names:
            x = file.split(' ')
            assert(len(x) == 2 and x[0] == character)
            if x[1].startswith(mood) and (x[1] == mood or all([a.isdigit() for a in x[1][len(mood)]])):
                #logging.info("saasda", x[1],"dsadas", x[1][len(mood) - 1])
                res.append(x[1])
                #res.extend(['{} {}'.format(character, x[1]), 0.1])
        #raise ValueError("character {} mood {} res {} files {}".format(character, mood, res, files_names))
        #raise ValueError(res)
        return res# * 20

    def make_animation(character, mood):#, repeat=20):
        #return get_images(character, mood)[:-1]
        template = [['{} {}'.format(character, i), 0.1] for i in get_images(character, mood)]
        #logging.info("template", template)
        flatten_template = list(chain.from_iterable(template))
        #logging.info("flatten templat", flatten_template)
        return list(chain.from_iterable([['{} {}'.format(character, i), 0.1] for i in get_images(character, mood)]))# * repeat)[:-1]

    def talk_anim(character, state):
        template = ["{} {}".format(character, state), 0.1, "{} {}_talking".format(character, state), 0.1]
        return Animation(*template)
    from collections import defaultdict
    class Characterr:
        def __init__(self, name, image, color='#000000', pos=Position(xpos=0.5)):
            self.name = name
            self.image = image
            self.color = color
            self.pos = pos
            self.char = Character(name, image=image, callback=partial(char_talking, self), who_color=color)
            self.tags = {"body": "main", "mouth": "closed", "reaction": "normal"}

        def __str__(self):
            return "{} {}".format(self.image, " ".join(self.tags.values()))

        def show(self, mood, *kwargs):
            for (k, i) in mood.items():
                self.tags[k] = i
            renpy.show(str(self), at_list=[self.pos])
        def talk(self):
            self.show({"mouth": "open"})

        def stop_talking(self):
            self.show({"mouth": "closed"})
    #Frizz = Characterr("FRIZ", image="friz", color='#000000')
    #Nowciaxx = Characterr("NOWCIAX", image="nowciax", color='#05232f', pos=pos_nowciax)
