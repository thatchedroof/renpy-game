label d1_start:

    play sound neco_arc_sound volume .05

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

    scene m room
    with fade

    play music sunshine loop fadein 5

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

# renpy-graphviz: BREAK

label ask_mom_morning_1_night:

    m "What the heck was I doing last night? I don't even remember coming home."

    mom "You were up all night!"

    mom "With your old neco friend."

    m "Ok."

    jump ask_mom_morning_1

# renpy-graphviz: BREAK

label ask_mom_morning_1_school:

    m "Why do I have to go to NECO school anyways?"

    mom "Your father has to work, sweetie."

    m "There's nothing to do in this dunghole."

    mom "You should be making friends!"

    mom "Maybe you'll get some BITCHES for once in your life."

    m "Mmm."

    jump ask_mom_morning_1

default d1_time = 0

# renpy-graphviz: BREAK

label school_morning_1_start:

    m "Well, gotta go. Bye mom."

    scene school courtyard
    with fade

    "First day at Essa Academy."

    stop music fadeout 3

    "I'm a little nervous.."

    "All my old friends are gone."

    "Well, other than...."

    "Huh."

    "The gates make this school look like a prison."

    "Something feels wrong..."

    play music sunshine loop fadein 3

    play sound neco_arc_sound volume 2

    show arc
    with zoomin

    arc "BURRUNYAAA~~~"

    m "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    arc "HEY [nupper]!!"

    arc "YOU'RE HERE!!!"

    m "NECO-ARC!! Great to see you, bud."

    arc "Glad you're ok!"

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

label d1_school_navigate:
    if d1_time == 4:
        pa "Period 1 is beginning! All students to Period 1 classroom!"

        m "Oh, time for class."

        call d1_math_class from _call_d1_math_class

menu d1_school_navigate_menu:

    "Main Hallway":
        jump d1_main_hallway

    "Classroom":
        jump d1_classroom

    "Cafeteria":
        jump d1_cafeteria

    "Library":
        jump d1_library

    "Gym":
        jump d1_gym

    "Roof":
        jump d1_roof

    "Stairway":
        jump d1_stairway

    "{b}Dismissal{\b}" if d1_math_class_v:
        jump d1_dismissal

default d1_main_hallway_v = False

# renpy-graphviz: BREAK

label d1_main_hallway:
    scene school hallway
    with fade

    if not d1_main_hallway_v:

        stop music fadeout 3

        m "Hey, where is everybody?"

        play sound vine_boom volume 1

        show deo
        with zoomin

        deo "shit shit shit"

        hide deo
        with zoomout

        m "WH-"

        m "WHO WAS THAT??"

        m "Huh, strange..."

        m "He seemed like he was looking for something."

        m "Well, nothing else to do here."

        play music sunshine loop fadein 3

        $ d1_main_hallway_v = True

        $ d1_time += 1

    else:

        m "There's nobody here."

        m "It's kinda creepy..."

        m "I should leave."

    jump d1_school_navigate

default d1_roof_v = False

# renpy-graphviz: BREAK

label d1_roof:
    scene school roof
    with fade

    if not d1_roof_v:
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

        $ d1_roof_v = True

        $ d1_time += 1

    else:
        wd "...what does \"failed to commit transaction\" mean?..."

        m "She seems pretty absorbed in her work."

        m "I shouldn't interfere."

    jump d1_school_navigate

default d1_classroom_v = False

# renpy-graphviz: BREAK

label d1_classroom:
    show school classroom
    with fade

    if not d1_classroom_v and d1_time < 4:

        m "So this is our classroom."

        show cat 5
        with dissolve

        tea "Your Period 1 classroom, to be exact."

        tea "Hello, I'm your math teacher."

        tea "You'll be seeing me later today."

        "(Darn. I'm not very good at math...)"

        hide cat 5
        with dissolve

        $ d1_classroom_v = True

        $ d1_time += 1

    elif d1_time >= 4:
        tea "Hope you learned something new today."

        m "Kinda..."

    else:
        m "The door's locked..."

    jump d1_school_navigate

default d1_stairway_v = False

# renpy-graphviz: BREAK

label d1_stairway:
    scene school stairs
    with fade

    if not d1_stairway_v:
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

        $ d1_stairway_v = True

        $ d1_time += 1

    else:
        m "Are you sure I can't come up the stairs?"

        pol "NIE."

        pol "TO BYŁ ŻART."

        m "Fine."

        "(Did he say shart?)"

    jump d1_school_navigate

default d1_cafeteria_v = False

# renpy-graphviz: BREAK

label d1_cafeteria:
    scene school cafeteria
    with fade

    m "Hi Neco!!"

    play sound neco_arc_sound

    show arc
    with dissolve

    arc "Burunyaa!!"

    arc "What's the latest?"

menu neco_cafeteria_qs_first:
    "Who was that guy in the main hallway?" if d1_main_hallway_v:
        jump deo_exposition

    "Who was that guy blocking the stairwell?" if d1_stairway_v:
        jump pol_exposition

    "Nothing much.":
        jump neco_nothing_much

menu neco_cafeteria_qs:
    "Who was that guy in the main hallway?" if d1_main_hallway_v:
        jump deo_exposition

    "Who was that guy blocking the stairwell?" if d1_stairway_v:
        jump pol_exposition

    "Well, see ya.":
        jump neco_gotta_go

label deo_exposition:
    m "Who was that brown cat that bumped into me in the hallway?"

    arc "Oh.."

    arc "That's {b}DeO{\b}."

    arc "I'd stay away if I were you."

    arc "I hope you haven't already attracted his ire..."

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

    arc "He's a hall monitor. He's not wearing his badge, however."

    m "Awesome..."

    jump neco_cafeteria_qs

label neco_nothing_much:
    m "No, just wanted to say hi."

    arc "Cool!"

    play sound neco_arc_sound

    arc "Burunyaa~"

    hide arc
    with dissolve

    jump d1_school_navigate

label neco_gotta_go:
    m "Well, see ya."

    arc "Cool!"

    play sound neco_arc_sound

    arc "Burunyaa~"

    hide arc
    with dissolve

    jump d1_school_navigate

default d1_library_v = False

# renpy-graphviz: BREAK

label d1_library:
    show school library
    with fade

    if not d1_library_v:
        dre "e"

        m "Hello!"

        dre "A"

        m "Woah."

        m "What was that?"

        $ d1_library_v = True

        $ d1_time += 1

    else:
        m "Nothing here."

    jump d1_school_navigate

default d1_gym_v = False

# renpy-graphviz: BREAK

label d1_gym:
    show school gym
    with fade

    if not d1_gym_v:
        zap "no. i thib it goes here"

        ari "what?"

        ari "what are you even talking about?"

        ari "shut up"

        zap "You closed it"

        ari "you're so bad"

        ari "you don't even know"

        "(They seem occupied...)"

        $ d1_gym_v = True

        $ d1_time += 1

    else:
        "The strange one is struggling with the door."

        "I shouldn't interfere."

    jump d1_school_navigate

default d1_math_class_v = False

# renpy-graphviz: BREAK

label d1_math_class:
    scene school classroom
    with fade

    show cat 5
    with dissolve

    tea "Hello class."

    tea "I've handed out your math packet."

    tea "Please complete as many questions as you can."

    hide cat 5
    with dissolve

label math_test:

    scene paper 1
    with fade

    $ math_test_score = 0

menu math_test_q1:
    "What is 9 times 3?"

    "35":
        call mtw from _call_mtw

    "29":
        call mtw from _call_mtw_1

    "21":
        call mtw from _call_mtw_2

    "27":
        call mtr from _call_mtr

menu math_test_q2:
    "What is 9 times 3?"

    "35":
        call mtw from _call_mtw_3

    "29":
        call mtw from _call_mtw_4

    "21":
        call mtw from _call_mtw_5

    "27":
        call mtr from _call_mtr_1

label d1_math_class_end:
    scene school classroom
    with fade

    $ d1_math_class_v = True

    return

label mtw:
    "Incorrect."
    return

label mtr:
    "Correct."
    $ math_test_score += 1
    return

# renpy-graphviz: BREAK

label d1_dismissal:
    scene school courtyard
    with fade

    m "Well, time to head home."

    m "Today was pretty uneventful."

    stop music fadeout 2

    m "Is every day gonna be like this?"

    play sound vine_boom

    show deo
    with zoomin
    play sound vine_boom
    with vpunch
    deo "your mad your mad"

    show deo at left
    with ease

    show cat 2 at right
    with moveinbottom

    roo "HOLY SHIT"

    play sound vine_boom
    with vpunch
    deo "your mad your mad"

    roo "SHUT THE FUCK UP"

    play sound vine_boom
    with vpunch
    deo "your mad your mad"

    roo "YOU'VE BEEN AT THIS THE ENTIRE DAY"

    play sound vine_boom
    with vpunch
    deo "your mad your mad"

    roo "YOU HAVE NO LIFE"

    play sound vine_boom
    with vpunch
    deo "your mad your mad"

    roo "ACTUALLY OBESE"

    play sound vine_boom
    with vpunch
    deo "your mad your mad"

    roo "SHUT UP!!!!"

    show cat 2 at left
    with ease
    show cat 2 at right
    with ease

    deo "..."

    deo "what are you doing androo"

    roo "GETTING YOU THE FUCK AWAY FROM ME"

    roo "YOU CRAZY PARASITE"

    deo "you remember what you owe me"

    deo "dont you androo"

    roo "WHAT THE FUCK ARE YOU TALKING ABOUT"

    "(DeO pulls out a phone.)"

    roo "..."

    roo "Put the phone away DeO."

    "(Androo raises his fists.)"

    deo "what's wrong"

    deo "scared"

    deo "mad"

    deo "what's wrong with hurting people"

    roo "..."

    deo "do you"

    deo "really"

    deo "want to give up"

    "(Androo's arms fall.)"

    deo "that's right"

    deo "you train"

    deo "but you can't bring yourself to land a single blow"

    deo "you're powerless"

    "(Androo falls to the floor.)"

    deo "you're nothing"

default stop_deo = False

menu d1_deo_choice:
    "Stop DeO.":
        $ stop_deo = True
        jump d1_stop_deo

    "Do nothing.":
        jump d1_deo_do_nothing

label d1_stop_deo:
    deo "fight back andr-"

    deo "oh"

    deo "i guess someone saw us"

    deo "androo"

    deo "you're lucky"

    hide deo
    with dissolve

    "(Androo gets back up.)"

    show cat 2 at center
    with ease

    roo "..."

    roo "Thanks, I guess."

    hide cat 2
    with dissolve

    jump d1_go_home

label d1_deo_do_nothing:
    deo "fight back androo"

    "(Androo punches the ground.)"

    "(...is that a crack?)"

    deo "your mad."

    deo "..your mad."

    roo "Your mad!!! Your mad!!!!"

    "(...Oh god...)"

    "(...I gotta go...)"

    hide cat 2
    with dissolve

    hide deo
    with dissolve

    jump d1_go_home

label d1_go_home:

    play music sunshine loop fadein 5

    pa "DING! All classes dismissed."

    scene m room
    with fade

    mom "Hello!"

    mom "How was school today?"

    m "Um."

    m "Pretty uneventful."

    mom "Well that's good to hear."

    mom "Do you have any homework?"

    m "No."

    scene black
    with fade

    stop music fadeout 3

    "Well."

    "Today was fun."

    "Uh.. most of it."

    "Did I just watch a guy get mentally farmed?"

    "Jesus Christ..."

    if d1_stairway_v:
        "Oh, there was that guy blocking the stairwell."

    if d1_library_v:
        "And there was that strange being in the library."

    if d1_gym_v:
        "And what was that door they were trying to open in the gym?"

    "Hmm.."

    "What am I gonna have for breakfast tomorrow?..."

    "END OF DAY 1"

label d1_end:
    jump d2_start
