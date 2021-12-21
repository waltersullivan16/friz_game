###   CHARACTERS   ###
init python:
    import os
    import sys
    media_dir = os.path.join(os.curdir, "media")

    def load_img(character):
        path = os.path.join(media_dir, character, "images")
        for state_img in os.listdir(path):
            state = state_img.split('.')[0]
            renpy.image('{} {}'.format(character, state), os.path.join(path, state_img))
    
    load_img('friz')
    load_img('nowciax')

    def get_image(character, activity):
        return os.path.join(media_dir, character, "images", "{}.png".format(activity))

    def load_gif(character, activity):
        path = os.path.join(media_dir, character, "gifs")
        anim = (os.path.join(path, f) for f in os.listdir(path) if f.startswith(activity))
        return list(anim)
    
    friz_main = load_gif("friz", "main")
    friz_otoja = load_gif("friz", "otoja")

# FRIZ


# gifs
image side friz = get_image("friz", "side")
image side nowciax = get_image("friz", "side")

image friz main_talking:
  friz_main[0]
  0.1
  friz_main[1]
  0.1
  repeat

image friz otoja_talking:
  friz_otoja[0]
  0.1
  friz_otoja[1]
  0.1
  repeat

### NOWCIAX


image nowciax main_talking:
    get_image("nowciax", "main")
    0.1
    get_image("nowciax", "maino")
    0.1
    repeat

###   BACKGROUND   ###
image background bedroom = get_image("background", "bedroom") 
