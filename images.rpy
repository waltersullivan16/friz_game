###   CHARACTERS   ###
init:
    $ Friz = Character("FRIZ", image="friz")
    define Nowciax = Character("NOWCIAX", image="nowciax")

image friz main_talking:
  "friz main"
  0.1
  "friz mainz"
  0.1
  repeat

image friz otoja_talking:
  "friz otoja"
  0.1
  "friz otojaz"
  0.1
  repeat

### NOWCIAX


#style.window.background = Frame("PinkBox.png", 25, 25)
image nowciax main_talking:
    "nowciax main"
    0.1
    "nowciax maino"
    0.1
    repeat

image vid ekipup = Movie("ekipup.mkv", (0,0), (0,0))
style window:
    background Frame("gui/db.png")
    left_margin 150

define gui.text_font = "Ubuntu-Regular.ttf"
define gui.text_size = 25
define gui.textbox_height = 300
#define gui.text_color = u'#696f96'
define gui.dialogue_ypos = gui.textbox_height // 2
define gui.dialogue_xpos = 170

define gui.name_text_font = "Hey Haters.ttf"
define gui.name_text_size = 40
define gui.name_xpos = 200
define gui.name_ypos = 60
define gui.name_text_color = '#000000'
define config.automatic_images = ['/', '-', '_']
define config.automatic_images_strip = ['images']
