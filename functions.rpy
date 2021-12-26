init python:
    define.move_transitions("ease", 1.6)

define farleft = Position(xpos=0.2)

define logodissolve = MultipleTransition([
    False, Dissolve(0.5),
    "logo.jpg", Pause(1.0),
    "logo.jpg", dissolve,
    True])

