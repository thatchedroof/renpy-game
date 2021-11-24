label d2_start:
    pass

label school_morning_2_start:
    scene school courtyard
    with fade

    arc "Hey [n]!!"

    m "Hi Arc."

    if not stop_deo:

        arc "Did you hear about the fight out here yesterday?"

        arc "Admin says they're gonna be cracking down on us cause of it."

        m "Admin?"

        arc "School administration."

        arc "They've been awfully tyrannical this year."

        m "\"This year\" has lasted one day. How do you know what they'll do?"

        arc "I dunno."

        arc "I can feel it in the air..."

    if stop_deo:

        m "What's up?"

        arc "Not much."

        arc "We got period 1 again today."

        m "What?.."

    arc "Well, time to head off to class."

    m "Oh. See ya."

menu d2_school_navigate_menu:

    "Main Hallway":
        jump d2_main_hallway

    "Classroom":
        jump d2_classroom

    "Cafeteria":
        jump d2_cafeteria

    "Library":
        jump d2_library

    "Gym":
        jump d2_gym

    "Roof":
        jump d2_roof

    "Stairway":
        jump d2_stairway

    "{b}Dismissal{\b}" if d2_math_class_v:
        jump d2_dismissal

default d2_main_hallway_v = False

label d2_main_hallway:
    scene school hallway
    with fade

    m "..."

    m "Shouldn't there be students around?"

default d2_classroom_v = False

label d2_classroom:
    scene school classroom
    with fade



label d2_cafeteria:

label d2_library:


default d2_gym_v = False

label d2_gym:
    scene school gym
    with fade

    m "They're playing basketball in here."

    m "Oh!"

    m "There's that shed."

    m "Is it still locked?"

    qqq "Hark!"

    m "What? Who's there?"

    m "..."

    m "(Is that security camera pointed at me?)"

    qqq "Verily, verily, I say unto thee..."

    qqq "Except a man be born of water and spirit,"

    qqq "He cannot enter."

    m "That's... what..."

    m "What are you talking about?"

    m "Hello?"

    m "..."

    m "It's still locked."

    $ d2_gym_v = True

    label deotime:

        m "I wonder if the shed in here is still locked."

        deo "what"

        m "Last time I went in here I had--"

        qqq "Hark!"

        m "And there it is."

        qqq "Hosanna!..."

        qqq "Children of water and spirit!"

        deo "what the fuck"

        qqq "You three... full triumvirate... immense power..."

        deo "nope"

        qqq "It is time I wrought your dea--"

        "DeO throws a basketball at the security camera, knocking it off the wall."

        m "What??"

        m "Was that thing gonna kill us??"

        arc "I think it was planning on it..."

        deo "wait"

        deo "what did it say?"

        deo "hold on"

        "DeO kicks open the shed door."

        deo "holy fuck"

        deo "it has begun"

label d2_roof:

label d2_stairway:

label d2_dismissal:
