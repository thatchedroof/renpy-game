define charfunc = lambda name, clr: Character(
    name,
    #kind=nvl,
    #what_prefix="{}\n    ".format(name),
    #what_suffix="",
    color=clr,
    #what_color=clr
    )

define m = charfunc("[n]", '#ffffff')

define mom = charfunc("Mom", '#ff0080')

define arc = charfunc("Neco-Arc", '#a80076')

define deo = charfunc("DeO", '#7c6352')

define roo = charfunc("Androo", '#a2a3a5')

define wd = charfunc("W. D.", '#7df9ff')

define pol = charfunc("Polish Guy", '#dc143c')

define dre = charfunc("Dream Dog", '#ffffff')

define sus = charfunc("Neco-Arc", '#a80057')

define zap = charfunc("Zap Rat", '#808080')

define ari = charfunc("Strange One", '#ff0080')

define pa = charfunc("PA system", '#ffffff')

define tea = charfunc("Teacher", '#ffffff')

define qqq = charfunc("???", '#ffffff')

label start:

    play sound neco_arc_sound volume .2

    "Oh god, my head.."

    define m = Character("[n]")

    python:
        n = renpy.input("Jeez, what was my name again?")
        n = n.strip().capitalize()

        if not n:
            n = "MC"

        nupper = n.upper()

    m "Yeah, [n]."

    stop music fadeout 5

    jump d1_start
