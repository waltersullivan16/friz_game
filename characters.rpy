# FRIZ


layeredimage friz:
    group body:
        attribute main default:
            "friz_main"
        attribute otoja:
            "friz_otoja"
        attribute otojasleeping:
            "friz_otojasleeping"

    group mouth:
        attribute closed default null
        attribute open:
            "usta"

    group emotion:
        attribute normal default null
        attribute angry:
            "sweatdropp"

define Friz = Character("FRIZ", image="friz", callback=partial(char_talking, 'friz'), who_color='#000000', at_list=[START_POS_FRIZ])

# NOWCIAX

layeredimage nowciax:
    group body:
        attribute main default:
            "nowciax_main"

    group mouth:
        attribute closed default null
        attribute open:
            "usta"

    group emotion:
        attribute normal default null
        attribute angry:
            "sweatdropp"

define Nowciax = Character("NOWCIAX", image="nowciax", callback=partial(char_talking, 'nowciax'), who_color='#05232f', at_list=[START_POS_NOWCIAX])
