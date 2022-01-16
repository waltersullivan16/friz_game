### PATHS

image vid ekipup = Movie("ekipup.mkv", (0,0), (0,0))
image background bedroom blurr = im.Blur("background/bedroom.png", 1.5)
image gold = Image("background/gold.png")


image sweatdropp = At("reactions/sweatdrop.png", sweatdrop_transform)
image gacie = "friz/ubranka/spodenki.png"

image friz_usta = Animation(*usta_animation('friz'))

image nowciax_usta  = Animation(*usta_animation('nowciax'))

init python:
    FrizClass = Characterr("FRIZ", image="frizz", who_color='#000000', pos=START_POS_FRIZ)
    Friz = FrizClass.char

    NowciaxClass = Characterr("NOWCIAX", image="nowciaxx", who_color='#000000', pos=START_POS_NOWCIAX)
    Nowciax = NowciaxClass.char
