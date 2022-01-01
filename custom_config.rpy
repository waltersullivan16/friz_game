define config.automatic_images = ['/', '-', '_']
define config.automatic_images_strip = ['images', 'animations']

define gui.text_font = "Ubuntu-Regular.ttf"
define gui.name_text_font = "Hey Haters.ttf"
define gui.text_size = 25
define gui.name_text_size = 45
define gui.dialogue_xpos = 400

style window:
    xalign 1.0
    yalign 1.0
    ysize 350
    background Image("gui/textbox/textbox.png", xalign=1.0, yalign=1.8)

style namebox:
    xsize 450
    ysize 160
    xalign 0.275
    yalign 0.3
    background Frame("gui/textbox/namebox.png")

style say_label:
    xalign 0.6
    yalign 0.3

style say_dialogue:
    xpos 400
    yalign 0.6
