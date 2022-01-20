### PATHS

image vid ekipup = Movie("ekipup.mkv", (0,0), (0,0))
image background bedroom blurr = im.Blur("background/bedroom.png", 1.5)

image reaction_sweatdrop = At("reactions/sweatdrop.png", dropping)
image reaction_luv = At("reactions/luv.png", beating)
image reaction_angry = At("reactions/angry.png", beating)
image reaction_angry2 = At("reactions/angry2.png", beating)

image friz_usta = Animation(*mouth_animation('friz'))
image friz love = Animation(*animation('friz', CHARACTER_ANIMATION_PATH, 'love'))

image nowciax_usta  = Animation(*mouth_animation('nowciax'))

define FrizClass = Characterr("FRIZ", image="friz", mouth_pos=FRIZ_MOUTH_POSITION, who_color='#000000', pos=START_POS_FRIZ)

define NowciaxClass = Characterr("NOWCIAX", image="nowciaxx", who_color='#000000', pos=START_POS_NOWCIAX)
define Nowciax = NowciaxClass.char
define Friz = FrizClass.char
init python:
    def show_emotion(character, emotion):
        arr = list(map(lambda x: int(x), renpy.get_image_bounds(character)))
        renpy.show(emotion, atl=Position(arr[0], arr[2]))
