define m = Character("[n]")

define mom = Character("Mom", color='#ff0080')

define arc = Character("Neco-Arc", color='#a80076')

define deo = Character("DeO", color='#7c6352')

define roo = Character("Androo", color='#a2a3a5')

define wd = Character("W. D.", color='#7df9ff')

define pol = Character("Polish Guy", color='#dc143c')

define dre = Character("Dream Dog", color='#ffffff')

define sus = Character("Neco-Arc", color='#a80057')

define zap = Character("Zap Rat", color='#808080')

define ari = Character("Strange One", color='#ff0080')

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

    play sound neco_arc_sound volume 2

    show arc
    with zoomin

    arc "BURRUNYAAA~~~"

    m "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    arc "HEY [nupper]!!"

    arc "YOU'RE HERE!!!"

    m "NECO-ARC!! Great to see you, bud."

    arc "Was fun doing catnip!"

    arc "You look wasted."

    arc "How much sleep did you get last night?"

    m "Yeah, it was great to catch up."

    "(I've known Neco-Arc since primary school. I'm glad they're still the same Arc from all those years ago.)"

    arc "We got a while until first period."

    arc "Meet me in the Cafeteria once you're done exploring."

    play sound neco_arc_sound

    arc "Burunyaa~"

    hide arc
    with moveoutleft

    "Man, this school is massive."

    "Maybe I should have asked Neco-Arc for a tour..."

    "Where do I head first?"

menu day_1_school_navigate:

    "Main Hallway":
        jump day_1_main_hallway

    "Classroom":
        jump day_1_classroom

    "Cafeteria":
        jump day_1_cafeteria

    "Library":
        jump day_1_library

    "Gym":
        jump day_1_gym

    "Roof":
        jump day_1_roof

    "Stairway":
        jump day_1_stairway

default day_1_main_hallway_visited = False

label day_1_main_hallway:
    scene school hallway
    with fade

    if not day_1_main_hallway_visited:
        m "Hey, where is everybody?"

        play sound vine_boom volume 1

        show deo
        with zoomin

        deo "shit shit shit"

        hide deo
        with zoomout

        m "WH-"

        m "WHO WAS THAT?"

        m "HE ALMOST BUMPED INTO ME!!"

        m "Huh, strange..."

        m "He seemed like he was looking for something."

        m "The classroom perhaps?"

        m "Maybe I should be doing the same."

        m "Well, nothing else to do here."

        $ day_1_main_hallway_visited = True

    else:

        m "There's nobody here."

        m "It's kinda creepy..."

        m "I should leave."

    jump day_1_school_navigate

default day_1_roof_visited = False

label day_1_roof:
    scene school roof
    with fade

    if not day_1_roof_visited:
        wd "Look at that hook echo!"

        wd "...shit, that's a lot of debris..."

        wd "WEDGE!!"

        m "Hello?"

        wd "GAH"

        m "What are you doing up here?"

        wd "What does it look like I'm doing??"

        m "Wha-"

        wd "FOLLOWING THE CURRENTLY UNFOLDING TORNADO OUTBREAK..."

        wd "...and waiting on my Arch install."

        m "Why do you have to be on the roof-"

        wd "THE ADMIN."

        wd "THE ADMIN PRESIDES OVER THE SCHOOL WIFI."

        wd "NO TRAFFIC ESCAPES HIS WATCHFUL EYE."

        wd "So I'm using my phone hotspot."

        wd "Install at 95\%.."

        wd "ERROR?!"

        """{font=courier_new.ttf} :: Mounting '/dev/disk/by-label/ARCH_201212' to 'run/archiso/bootmnt'
        Waiting 30 seconds for device /dev/disk/by-label/ARCH_201212 ...
        ERROR: '/dev/disk/by-label/ARCH_201212' device did not show up after 30 seconds...{\font}"""

        """{font=courier_new.ttf} Falling back to interactive prompt\n
        sh: can't access tty; job control turned off\n\n
        :] -Admin{\font}"""

        wd "What."

        wd "ADMIN"

        wd "HOW."

        wd "HOW DO YOU GET ONTO MY MOBILE HOTSPOT"

        wd "HES USING BLACK MAGIC"

        wd "GAAHH"

        wd "..."

        wd "If you wouldn't mind, I'd prefer to be left alone right now."

        wd "I must focus."

        $ day_1_roof_visited = True

    else:
        wd "...what does \"failed to commit transaction\" mean?..."

        m "She seems pretty absorbed in her work."

        m "I shouldn't interfere."

    jump day_1_school_navigate

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

    jump day_1_school_navigate

default day_1_stairway_visited = False

label day_1_stairway:
    scene school stairs
    with fade

    if not day_1_stairway_visited:
        m "Uhh.. Hey?"

        pol "Za pozno?"

        m "What?"

        pol "Potrzebujemy jezusa w naszym życiu..."

        m "..."

        pol "Już jak ja wrócę to będziecie mieli wykład o bogu."

        m "Can you uhh.. move out of the way?"

        m "I gotta get up the stairs."

        pol "NIE."

        m "Excuse me?"

        pol "NIE ZGADZAJCIE SIE."

        m "Jesus, ok.."

        pol "Czas minął."

        $ day_1_stairway_visited = True

    else:
        m "Are you sure I can't come up the stairs?"

        pol "NIE."

        pol "TO BYŁ ŻART."

        m "Fine."

        "(Did he say shart?)"

    jump day_1_school_navigate

default day_1_cafeteria_visited = False

label day_1_cafeteria:
    scene school cafeteria
    with fade

    m "Hi Neco!!"

    play sound neco_arc_sound

    show arc
    with fade

    arc "Burunyaa!!"

    arc "What's the latest?"

menu neco_cafeteria_qs_first:
    "Who was that guy in the main hallway?" if day_1_main_hallway_visited:
        jump deo_exposition

    "Who was that guy blocking the stairwell?" if day_1_stairway_visited:
        jump pol_exposition

    "Nothing much.":
        jump neco_nothing_much

menu neco_cafeteria_qs:
    "Who was that guy in the main hallway?" if day_1_main_hallway_visited:
        jump deo_exposition

    "Who was that guy blocking the stairwell?" if day_1_stairway_visited:
        jump pol_exposition

    "Well, see ya.":
        jump neco_gotta_go

label deo_exposition:
    m "Who was that brown cat that bumped into me in the hallway?"

    arc "Oh.."

    arc "That's {b}DeO{\b}."

    arc "I'd stay away if I were you."

    arc "I hope you haven't already attracted his ire..."

    arc "You don't wanna get on his bad side."

    arc "He's \"Fucked Up\"."

    m "Huh."

    m "I thought he was kinda soft..."

    play sound vine_boom

    arc "Shut up."

    m "Ok.."

    jump neco_cafeteria_qs

label pol_exposition:
    m "Who's the guy in the stairwell?"

    m "I can't understand a single thing he says."

    arc "Oh, the Polish Guy?"

    arc "He's a transfer student."

    arc "I don't think anyone knows his name."

    arc "They say he comes from Upstairs."

    m "Upstairs?"

    m "Up the stairwell?"

    arc "Pretty much."

    arc "He's a hall monitor, but I don't know where his badge is."

    arc "He should be wearing it."

    m "Awesome..."

    jump neco_cafeteria_qs

label neco_nothing_much:
    m "No, just wanted to say hi."

    arc "Cool!"

    play sound neco_arc_sound

    arc "Burunyaa~"

    hide arc
    with fade

    jump day_1_school_navigate

label neco_gotta_go:
    m "Well, see ya."

    arc "Cool!"

    play sound neco_arc_sound

    arc "Burunyaa~"

    hide arc
    with fade

    jump day_1_school_navigate

default day_1_library_visited = False

label day_1_library:
    show school library
    with fade

    if not day_1_library_visited:
        dre "e"

        m "Hello!"

        dre "A"

        m "Woah."

        m "What was that?"

        $ day_1_library_visited = True

    else:
        m "Nothing here."

    jump day_1_school_navigate

default day_1_gym_visited = False

label day_1_gym:
    show school gym
    with fade

    if not day_1_gym_visited:
        zap "no. i thib it goes here"

        ari "what?"

        ari "what are you even talking about?"

        ari "shut up"

        zap "You closed it"

        ari "you're so bad"

        ari "you don't even know"

        $ day_1_gym_visited = True

    else:
        m "Nothing here."

    jump day_1_school_navigate

return
