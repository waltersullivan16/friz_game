### PATHS

image vid ekipup = Movie("ekipup.mkv", (0,0), (0,0))
image background bedroom blurr = im.Blur("background/bedroom.png", 1.5)

# ANIMATION #

init python:
    def usta_animation(character):
        usti_files = [os.path.splitext(f)[0] for f in os.listdir(CHARACTER_MOUTH_PATH(character))]
        return list(chain.from_iterable([[f, MOUTH_ANIMATION_PAUSE] for f in usti_files]))
        
image usta  = Animation(*usta_animation('friz'))
