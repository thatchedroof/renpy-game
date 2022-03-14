label d2_start:

    scene m room
    with fade

    "..."

    "Oh man, what was I dreaming about?"

    "The thought is fading..."

    "Ants?"

label school_morning_2_start:
    scene school courtyard
    with fade

    show arc
    with zoomin

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

        arc "I can feel it in the air."

        arc "Hey, wanna stick together today?"

        arc "We got some time before period 1."

        m "Sure."

        m "Could use it."

        arc "Definitely."

    if stop_deo:

        m "What's up?"

        arc "Not much."

        arc "We got period 1 again today."

        m "What?"

        arc "Yeah, I know."

        arc "Something the school has going on."

        m "Interesting."

        m "Hey, y'know, have you ever seen anything weird around the school?"

        arc "All the time. Why?"

        m "I get the feeling we should stick together."

        arc "As a team?"

        m "Sure... a team."

        arc "Awesome."

    m "Well, where do we go first?"

    arc "Hmm..."

    arc "Let's go to the library."

    arc "Nobody ever goes there."

    m "Oh, sounds fun."

label d2_library:
    scene school library
    with fade

    show arc
    with fade

    m "..."

    arc "What?"

    m "(It's not here today.)"

    m "(Did I dream that?)"

    m "Oh um, nothing."

    arc "Ok."

    arc "Let me find a book."

    arc "..."

    arc "Hmm, these are all textbooks."

    arc "There's gotta be something.."

    "(A book falls off the shelf beside Neco-Arc.)"

    arc "Oh, let me get that."

    "(Neco-Arc flips through the pages.)"

    arc "Haha."

    m "What?"

    arc "It's a blank notebook."

    arc "The middle third of the pages have been ripped out."

    m "Let me see!"

    arc "Here."

    m "The name on the front is smudged."

    m "Woah, the back of the cover."

    arc "What does it say?"

    m "It's from last year."

    m "Grade 11 Math."

    arc "Cool. I wonder who's this is?"

    arc "We'll have to ask around."

    m "To see if anybody wants their... year old math notes back?"

    arc "Yeah, ok."

    m "The second page has polynomials."

    m "I could use this for class."

    m "And it has a doodle."

    m "..."

    m "Oh.. god."

    arc "What??"

    m "Well, that's not ok."

    arc "Let me see!!"

    arc "..."

    arc "This doesn't need to be returned."

    m "Yeah."

    m "..."

    m "Huh, this page is just scribbles."

    arc "Scribbles?"

    m "Yeah. Must have gotten bored in class."

    m "Then it.. stops."

    m "The pages were ripped out."

    m "I don't think they even used scissors."

    arc "Ok, cool."

    arc "Let's put this back in the ancient archives."

    m "No, wait."

    m "I think we should keep it."

    arc "Keep it?"

    m "Yeah. It's a piece of history."

    m "This student put a year of effort into these notes."

    m "It's come into our hands now."

    m "He may not even attend this school anymore."

    m "It could be one of the last relics of his time here."

    m "It might not mean much to him but it does mean something to me."

    m "A window into the past."

    "(Neco-Arc's stomach growls.)"

    arc "Mrrowl.."

    arc "I forgot to eat breakfast today..."

    arc "I wonder if the cafeteria has any more food left over..."

    arc "Hey, I'll be back soon, ok?"

    m "Ok."

    hide arc
    with fade

    m "..."

    m "...."

    m "When is soon?"

    m "....."

    m "Bored."

    m "I wonder if the gym has anything to do."

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

label d2_cafeteria:
    scene school cafeteria
    with fade

    m "Neco, you won't believe--"

    show arc
    with fade

    arc "Shh."

    m "What?"

    arc "Don't look."

    arc "The guy at the table next to us."

    arc "I think he's been following me."

    m "Wha--"

    arc "Shh!!"

    arc "Whisper!"

    m "Sorry."

    m "Why do you think he's been following you?"

    arc "I saw him on the way to the library."

    arc "When I got here, he was at the table at the far side of the cafeteria."

    arc "So far he's changed tables seven times!!"

    arc "Each one gets closer and closer!"

    m "Why don't you just ask him why he's here?"

    arc "Because, look."

    "(Neco-Arc pulls out a metal thermos. In the reflection, is...)"

    m "DeO!!"

    arc "Quiet!"

    arc "Ok, I have a plan."

    arc "Let's both get up and walk out."

    arc "Look in the thermos and tell me what he does."

    m "Ok..."

    "(Neco-Arc packs up three trays of lunch and gets up.)"

    "(DeO gets up at the same time.)"

label d2_main_hallway:
    scene school hallway
    with fade

    arc "Just go down the hall... don't look..."

    play sound vine_boom volume 1

    show deo
    with fade

    deo "AGH"

    deo "oh shit"

    m "(He fell!)"

    deo "hi"

    m "Hey, uh.."

    deo "i'm your friend"

    m "Ok?"

    deo "we're friends"

    m "Ok."

    deo "oh, uh, do you want to be my friend"

    m "Sure, w-"

    pa "Period 1 is beginning! All students to Period 1 classroom!"

    deo "it's period 1 now"

    m "Yeah."

    deo "gotta go"

    m "Yeah, sure."

    hide deo
    with fade

    m "..."

    arc "What the fuck."

    m "What the fuck?"

    arc "I can't... process this right now..."

    m "It's time for class anyways."

    m "We'll talk about this after."

    arc "Fine with me."

label d2_math_class:
    show school classroom
    with fade

    show cat 5
    with dissolve

    tea "Hello class."

    tea "You'll be completing math worksheet 23-B."

    tea "Please take one and pass the packets to the student on your left."

    m "(More packets...)"

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

label mtw:
    "Incorrect."
    return

label mtr:
    "Correct."
    $ math_test_score += 1
    return

label d2_math_class_end:
    scene school classroom
    with fade

    m "Um..."

    tea "There's the bell."

label d2_meeting_hallway
    scene school hallway
    with fade

    show arc
    with fade

    arc "Hey [n]!!"

    m "Hey!"

    arc "Have you... seen him around?"

    m "I was in class with you, dude."

    arc "Oh yeah."

    m "So like, what do you know about him?"

    arc "Not much..."

    arc "I've seen him and androo fight a few times."

    arc "Other than that he's a loner."

    arc "Like a lone wolf."

    arc "He keeps to himself most of the time."

    arc "I'm not in any classes with him, and I wasn't here in summer school, but from what I've heard..."

    arc "...he sits in the corner of class, playing obnoxious rhythm games."

    arc "And when the teacher asks him to stop, he-"

    deo "you know what's wild"

    show deo
    with fade

    m "Wh-"

    deo "how bad you are"

    m "Ok, wa-"

    deo "how much i hate you"

    m "Um, didn't you want to be friends?"

    deo "how dumb you are"

    deo "yeah, let's be friends"

    m "..."

    arc "..."

    arc "I mean, it's worth a shot, right?"

    m "This guy's insane..."

    deo "yeah"

    m "So.."

    m "What do you guys wanna do?"

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

    "{b}Dismissal{\b}" if d2_stairway_opened:
        jump d2_dismissal

default d2_main_hallway = False

# renpy-graphviz: BREAK

label d2_main_hallway:
    scene school hallway
    with fade

    if not d2_main_hallway_v:

        m "We... were here already."

        arc "Yeah."

        m "Just, like, a minute ago."

        deo "what"

        $ d2_main_hallway_v = True

    else:

        m "(Hello? Helloo?)"

        m "(Phone clicks.)"

    jump d2_school_navigate

default d2_classroom = False

# renpy-graphviz: BREAK

label d2_classroom:
    scene school classroom
    with fade

    if not d2_classroom_v:

        m "Ok, cmon. We can leave now."

        $ d2_classroom_v = True

    else:

        m "Really?"

    jump d2_school_navigate

default d2_cafeteria = False

# renpy-graphviz: BREAK

label d2_cafeteria:
    scene school cafeteria
    with fade

    if not d2_cafeteria_v:

        deo "thats crazy"

        deo "going back to the cafeteria where they serve gloop"

        m "Yeah."

        $ d2_cafeteria_v = True

    else:

        deo "crazy how much budget they spent exclusively on the cafeteria"

        deo "food is strange this year"

    jump d2_school_navigate

default d2_library = False

# renpy-graphviz: BREAK

label d2_library:
    scene school library
    with fade

    if not d2_library_v:

        deo "uncanny... i feel a presence"

        m "Oh, yeah. Yesterday I did too."

        deo "shut up"

        # INSERT BOOK COLLECTING DIALOGUE

        $ d2_library_v = True

    else:

        arc "Thanks..."

    jump d2_school_navigate

default d2_roof = False

# renpy-graphviz: BREAK

label d2_roof:
    scene school roof
    with fade

    if not d2_roof_v:

        m "It's chilly today."

        deo "it's not that cold"

        m "You're covered in fur!"

        # INSERT ARCH DIALOGUE

        $ d2_roof_v = True

    else:



    jump d2_school_navigate

default d2_stairway = False

# renpy-graphviz: BREAK

label d2_stairway:
    scene school stairway
    with fade

    if not nametag_get:

        pol "Kurwa bez kox jablek jestes bity."

        pol "Kurwa mac."

    elif not d2_stairway_v:

        pol "Nowy regulamin! #zasady"

        m ""

        $ d2_stairway_v = True

    else:



    jump d2_school_navigate

default d2_gym = False

# renpy-graphviz: BREAK

label d2_gym:
    scene school gym
    with fade

    if not d2_gym_v:

        scene school gym
        with fade

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

        qqq "It is time I wrought your demis--"

        "DeO throws a basketball at the security camera, knocking it off the wall."

        m "What??"

        m "Was that thing gonna kill us??"

        arc "I think it was planning on it..."

        deo "wait"

        deo "what did it say?"

        deo "hold on"

        "DeO kicks open the shed door."

        deo "holy fuck"

        "Look at your shadow. What do you see?"

        m "A face!"

        "Not just any face."

        m "Oh, I understand."

        m "..."

        m "I don't understand."

        "What can you remember?"

        m "Nothing much."

        "Where are we?"

        m "Underwater."

        "Wrong. Where are we really?"

        m "This isn't real."

        "I will show you something. But you must hand over some control."

        m "Control over what?"

        "You won't mind, will you?"

        "Just try not to think for a bit."

        m "How much control?"

        "You're lax. That's all you've ever been. You're lazy."

        m "What?"

        "All you have to do is be a bit lazier."

        m "..."

        m "Fine."

        arc "Hey [n]."

        deo "hi [n]."

        arc "Can you help us figure out how to use these?"

        m "What? This is just some gym equipment..."

        m "I can't, there's nothing to do with these..."

        tea "I need you to use these for me."

        m "What??"

        m "Ok, I'll try..."

        m "..."

        m "I can't put them together..."

        arc "Hey! What's taking so long?"

        deo "you need to destroy this"

        m "Is that the school garden?"

        deo "figure out how to destroy this"

        m "But these are just random... this is random..."

        deo "the ants here"

        deo "they're not in our design"

        deo "they walked away from us"

        m "You've hid them back here?"

        deo "yes."

        deo "but they're causing problems again"

        deo "you need to destroy every weed."

        m "Hey, did you say ants, or weeds..."

        arc "It doesn't matter."

        deo "they'll start crawling on you if you don't start."

        m "I have a feeling these aren't either."

        deo "doesn't matter. use your tools and fix it."

        m "Hey! How do I use these??"

        m "Help!"

        m "..."

        m "Fix it.. I can't..."

        m "Oh!"

        m "I can!"

        m "Oh, this is going to take so long..."

        m "I'll never be able to finish in time..."

        m "I..."

        arc "Dude, dude, is [n] gonna wake up?"

        deo "i don't know"

        arc "Jesus christ... the fuck happened??"

        m "oh... shit"

        arc "[nupper]!!!"

        m "I... oh my god, what's in the shed..."

        arc "It was just some gym stuff dude, calm down..."

        m "Wait... shit... did anybody take it??"

        deo "here. i brought it."

        m "Can I see it?"

        deo "you're... already holding it."

        m "Wait, when did I get this?"

        deo "..."

        arc "Hey, I think it's time to head home."

        m "What?"

        m "Wait, how long have I been sleeping?"

        arc "Ok, let's put these back..."

        m "..."

        arc "Jeez, you don't have to be so loud..."

        m "What? But I didn't say anything!"

        arc "The teachers won't like us taking the gym equipment home."

        deo "i know where to put them"

        deo "they'll be safe"

        m "Ok..."

        $ d2_gym_v = True

    else:



    jump d2_school_navigate
