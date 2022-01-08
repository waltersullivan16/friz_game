define config.automatic_images = ['/']
define config.automatic_images_strip = ['images']

define gui.text_font = "Ubuntu-Regular.ttf"
define gui.name_text_font = "Hey Haters.ttf"
define gui.text_size = 25
define gui.name_text_size = 45
define gui.dialogue_xpos = 400

style window:
    background Frame("gui/textbox/dq.png")
    yalign 1.0
    #left_margin 100
    ysize 300

style namebox:
#    xpos gui.name_xpos
#    ypos gui.name_ypos
#    #background Frame("gui/textbox/nb.png")#, gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
#    #padding gui.namebox_borders.padding
    xalign 0.2
    yalign 0.14


style say_label:
    properties gui.text_properties("name", accent=True)


style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 300
    yalign 0.6
    xsize gui.dialogue_width
