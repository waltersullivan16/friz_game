### PYTHON FUNCTIONS
init python:
    import os
    import logging
    import string
    from itertools import chain
    from functools import partial
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

    def talking_sprite(character, state):
        return "{} {}_talking".format(character, state)

    def char_talking(character, event, **kwargs):
        attr = renpy.get_attributes(character)
        if attr is None:
            logging.info("character {}".format(character))
            return
        logging.info("EVEEEENT {} kwargs {} attr {} {}".format(event, kwargs, attr, character))
        talking_sprite = "{} {}_talking".format(character, attr[0])
        if event == "end":
            renpy.hide(talking_sprite)
        elif event=="show":
            renpy.show(talking_sprite)


    define.move_transitions("ease", 1.6)
    friz_dict = { "main": 'friz main_talking', "otoja": 'friz otoja_talking'}
