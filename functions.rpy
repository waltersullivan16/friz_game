init python:
    define.move_transitions("ease", 1.6)

define farleft = Position(xpos=0.2)
define farright = Position(xpos=0.8)

define logodissolve = MultipleTransition([
    False, Dissolve(0.5),
    "logo.jpg", Pause(1.0),
    "logo.jpg", dissolve,
    True])

transform alphatransform:
    alpha .0
    linear 1.0 alpha 1.0

init python:

    def active_friz(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "begin":
            current_speaker = 'friz'

