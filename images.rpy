### PATHS

### PYTHON FUNCTIONS
init python:
    import os
    import string
    from itertools import chain
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
                print("saasda", x[1],"dsadas", x[1][len(mood) - 1])
                res.append(x[1])
        #raise ValueError("character {} mood {} res {} files {}".format(character, mood, res, files_names))
        #raise ValueError(res)
        return res

    def make_animation(character, mood, repeat=30):
        template = [['{} {}'.format(character, i), 0.1] for i in get_images(character, mood)]
        print("template", template)
        flatten_template = list(chain.from_iterable(template))
        print("flatten templat", flatten_template)
        return (list(chain.from_iterable([['{} {}'.format(character, i), 0.1] for i in get_images(character, mood)])) * repeat)[:-1]


###   CHARACTERS   ###


define Friz = Character("FRIZ", image="friz")
define Nowciax = Character("NOWCIAX", image="nowciax")
image background bedroom blurr = im.Blur("background/bedroom.png", 1.5)
image nowciax main_talking = Animation(*make_animation("nowciax", "main"))
image friz main_talking = Animation(*make_animation("friz", "main"))
image friz otoja_talking = Animation(*make_animation("friz", "otoja"))
image vid ekipup = Movie("ekipup.mkv", (0,0), (0,0))

#image side friz = Transform('friz/side/side friz a2.png')#, xalign=400, yalign=-1000)
