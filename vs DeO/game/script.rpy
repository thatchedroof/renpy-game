define m = Character("[n]")

define mom = Character("Mom", color='#ff0080')

define arc = Character("Neco-Arc", color='#a80076')

define deo = Character("DeO", color='#7c6352')

define roo = Character("Androo", color='#a2a3a5')

define wdr = Character("W. D.", color='#7df9ff')

define pol = Character("Polish Guy", color='#dc143c')

define dre = Character("Dream Dog", color='#ffffff')

define sus = Character("Neco-Arc", color='#a80057')

label start:

    "BURRUNYAA~~"

    "IT'S MY FIRST DAY AT ESSA ACADEMY!!!"

    "Oh god, my head.."

    define m = Character("[n]")

    python:
        n = renpy.input("Jeez, what was my name again?")
        n = n.strip().capitalize()

        if not n:
            n = "Andrew"

        nupper = n.upper()

    m "Yeah, [n]."

    scene m room
    with fade

    m "Urrgh.. I had too much catnip..."

    mom "It doesn't do anything, honey. You're human."

default ask_mom_morning_1_night = False
default ask_mom_morning_1_school = False

menu ask_mom_morning_1:

    "What happened last night?" if not ask_mom_morning_1_night:
        $ ask_mom_morning_1_night = True
        jump ask_mom_morning_1_night

    "What's the deal with my school?" if not ask_mom_morning_1_school:
        $ ask_mom_morning_1_school = True
        jump ask_mom_morning_1_school

    "I have to go to school now.":
        jump school_morning_1_start

label ask_mom_morning_1_night:

    m "What the heck was I doing last night? I don't even remember coming home."

    mom "DIALOGUE SOON"

    m "Oh, yeah."

    jump ask_mom_morning_1

label ask_mom_morning_1_school:

    m "Why do I have to go to NECO school anyways?"

    mom "Your father has to work, sweetie."

    m "There's nothing to do in this dunghole."

    mom "You should be making friends!"

    mom "Maybe you'll get some BITCHES for once in your life."

    m "Mmm."

    jump ask_mom_morning_1

label school_morning_1_start:

    m "Well, gotta go. Bye mom."

    scene school courtyard
    with fade

    "First day at Essa Academy."

    "I'm a little nervous.."

    "All my old friends are gone."

    "I'm restarting from scratch!"

    "Well, other than...."

    "Huh."

    "The gates make this school look like a prison."

    "Something feels wrong..."

    play sound neco_arc_sound volume 5

    show arc
    with zoomin

    arc "BURRUNYAAA~~~"

    m "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    arc "HEY [nupper]!!"

    arc "YOU'RE HERE!!!"

    m "NECO-ARC!! Great to see you, bud."

    arc "Fun doing catnip with you, my dude."

    arc "You look wasted."

    arc "How much sleep did you get last night?"

    m "Yeah, it was great to catch up."

    "(I've known Neco-Arc since primary school. I'm glad they're still the same Arc from all those years ago.)"

    arc "We got a while until first period."

    arc "I'll meet you in the Cafeteria."

    play sound neco_arc_sound

    arc "Burunyaa~"

    hide arc
    with moveoutleft

    "Man, this school is massive."

    "Maybe I should have asked Neco-Arc for a tour..."

    "Where do I head first?"

menu day_1_school_navigate:

    "Main Hallway":
        pass

    "Classroom":
        jump day_1_classroom

    "Cafeteria":
        pass

    "Gym":
        pass

    "Roof":
        pass

    "Stairway":
        pass

label day_1_classroom:
    scene school classroom
    with fade

    show cat 1

    arc "Burrunyaa"

    show cat 2

    arc "Burrunyaa"

    show cat 3

    arc "Burrunyaa"

    show cat 4

    arc "Burrunyaa"

    show cat 5

    arc "Burrunyaa"

    show cat 6

    arc "Burrunyaa"

return
