
define logodissolve = MultipleTransition([
    False, Dissolve(0.5),
    "logo.jpg", Pause(1.0),
    "logo.jpg", dissolve,
    True])
