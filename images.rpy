### PATHS

### PYTHON FUNCTIONS
init python:
    import os
    import string
    from itertools import chain
    GAME_PATH = "/home/akechi/lajno/frizzzz/game"
    IMAGES_PATH = os.path.join(GAME_PATH, "images")
    ANIMATIONS_PATH = lambda character: os.path.join(IMAGES_PATH, character, "animations")
    def get_images(character, mood):
        character_path = ANIMATIONS_PATH(character)
        try:
            files = filter(lambda x: x.startswith(mood), [(os.path.splitext(f)[0]).split(' ')[1] for f in os.listdir(character_path)])
        except:
            print(character, mood)
            return
        #files = map(lambda x: x.encode("ascii", "ignore"), files)
        return filter(lambda x: x == mood or x[len(mood):].isdigit(), files)

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

