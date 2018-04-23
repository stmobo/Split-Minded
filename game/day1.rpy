label day1_start:
    $ reset_to_default_spawns()
    $ set_screen_center(control_panel_pos)

    pause

    scene bedroom day at scene_bg
    show screen ctrl_game
    with dissolve

    "We still feel exhausted when we wake up the next day."

    "[mc.name] drags himself out of bed and starts going about his morning routine purely on autopilot..."

    "...and it takes us a minute to realize that isn't just a metaphor."

    calm "So, wait, does {i}anyone{/i} have the controls?"

    pyro "I certainly do not."

    surv "I don't have the controls."

    artist "No."

    "..."

    "We all get the idea in our heads at about the same time:"

    $ start_combat()

    "We're going to have to fight for the controls again."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)
        add_diversion_points(winner, 1)

        renpy.show_screen('ctrl_game')
        renpy.with_statement(dissolve)

        is_morning_diversion = True
        is_afternoon_diversion = False
        is_day2_diversion = False

        current_location = 'school'

        call_diversion(winner, 'day1_start')

    if winner == 'calm':  # no diversion
        jump day1_start_no_diversion
    else:
        jump day1_start_diverted

label day1_start_no_diversion:
    if current_location != 'school':
        "With that out of the way, [mc.name] starts walking to school."

        scene school day at scene_bg
        with dissolve
    else:
        "With that out of the way, [mc.name] actually starts walking to class."

    scene hallway alt day at scene_bg
    with dissolve

    "Even as tired as [mc.name] is, we still manage to arrive to class well before the bell."

    show nanami happy at center
    with dissolve

    "We bump into Nanami in the hallways again-- fortunately, without knocking her over this time."

    nanami "Oh, hiya [mc.name]! Feeling any better?"

    mc "I guess? I didn't really get much sleep last night."

    show nanami worried at center
    with dissolve

    nanami "Ehh, seriously? What, did'ja wake up in the middle of the night or something?"

    mc "Actually, yeah, that's pretty much what happened."

    show nanami normal at center
    with dissolve

    nanami "Oh, that sucks. What was it, a nightmare? Something loud outside?"

    mc "...I'm not actually sure, now that I think about it.{p}I just kind of... woke up, and sat there for a while."

    if day0_diverted:
        mc "And then everything's a blank, after that.{p}I think I might have gone outside, but I honestly can't remember."
    else:
        mc "Then I went back to sleep."

    nanami "For real? That's super strange."

    mc "I know, right? But I guess it could be worse. I could have overslept this morning, or something."

    show nanami happy at center
    with dissolve

    nanami "Heh, wouldn't be the first time for you."

    show nanami normal alt at center
    with dissolve

    nanami "Oh, I should get going; I don't want to be late to class. Seeya!"

    scene classroom day at scene_bg
    with dissolve

    jump day1_afterclass

label day1_start_diverted:
    $ voice_name = get_controlling_voice_name()

    if current_location != 'school':
        "With that out of the way, [voice_name] sits back and stops directly controlling [mc.name], who starts walking to school on his own initiative."

        scene school day at scene_bg
        with dissolve
    else:
        "With that out of the way, [voice_name] sits back and stops directly controlling [mc.name], who starts actually walking to class, now under his own initiative."

    scene school day at scene_bg
    with dissolve

    "The combination of [mc.name]'s tiredness and the diversion, however, means that we end up being seriously late to class."

    scene classroom day at scene_bg
    with dissolve

    "As it is, [mc.name] walks through the classroom doors an hour after the first bell."

    "After mumbling a few apologies to the teacher, we drag ourselves to our desk, a sleep-deprived, exhausted mess."

    show hitomi worried at center
    with dissolve

    "Hitomi comes to talk to us at lunch."

    hitomi "You really aren't feeling any better since yesterday, are you [mc.name]?"

    mc "No, not really... I'm exhausted. I didn't get much sleep last night."

    show hitomi normal at center
    with dissolve

    hitomi "Oh my. Did you have trouble falling asleep?"

    mc "No, I just suddenly woke up in the middle of the night. I'm not sure why."

    hitomi "Well, perhaps you had a nightmare?"

    mc "I guess that could've happened... but something tells me that isn't it."

    mc "I mean, I remember waking up and just sitting there, for a while."

    if day0_diverted:
        mc "I think I went outside, at some point? But I'm not really sure, though, because everything's just... gone from my memory."
    else:
        mc "And then I just went back to sleep."

    show hitomi normal alt at center
    with dissolve

    hitomi "And so you overslept this morning, I assume?"

    mc "Not really, actually. Everything's just so hazy... I remember getting up and eating breakfast, but then after that everything just goes blank."

    mc "The next thing I remember is sitting back at home, almost an hour afterwards. And that's when I started walking to school."

    show hitomi worried at center
    with dissolve

    hitomi "That is quite worrying. Perhaps you should go see a doctor?"

    mc "Ehh... I'll wait a couple of days and see if it happens again. Who knows, it might just pass quickly."

    hitomi "If you say so..."

    jump day1_afterclass

label day1_afterclass:
    "Classes come and go as quickly as usual."

    if winner == 'calm':
        "As we walk out of the classroom at the end of the day, I can feel the other voices finish reconstituting."
    else:
        "As we walk out of the classroom at the end of the day, the other voices and I can feel our bodies finish reconstituting."

    $ start_combat()

    "And we're back to fighting for the controls..."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)

    pause

    scene hallway day at scene_bg
    show screen ctrl_game
    with dissolve

    "And when the dust settles, we're left with a choice."

    mc "Something tells me I shouldn't leave just yet."

    mc "But what should I do?"

    $ route_choice = renpy.random.choice(['hitomi', 'nanami'])

    if winner != 'calm':
        $ voice_name = get_controlling_voice_name()
        "[voice_name] gives [mc.name] a slight nudge..."

        if route_choice == 'hitomi':
            if winner == 'pyro':
                pyro "Hitomi seems like a charming girl. Let's go visit her in the library, shall we?"
            elif winner == 'artist':
                artist "The library is quiet, right?{p}I want to go there."
            elif winner == 'surv':
                surv "I need to do some deeper recon. Let's go to the library."
        elif route_choice == 'nanami':
            if winner == 'pyro':
                pyro "That Nanami girl-- she said they were preparing for a play performance, yes? Let's go visit her."
            elif winner == 'artist':
                artist "I need inspiration.{p}I wonder if I'll find it in the auditorium?"
            elif winner == 'surv':
                surv "I need to do deeper recon. We should go scope out the auditorium.."

    menu:
        "Go visit the library." if route_choice == 'hitomi' or winner == 'calm':
            $ route_choice = 'hitomi'
        "Go visit the auditorium." if route_choice == 'nanami' or winner == 'calm':
            $ route_choice = 'nanami'

    if route_choice == 'hitomi':
        if winner == 'calm':
            calm "Why don't we go see what's happening in the library? We might find Hitomi there."

        mc "...maybe I'll go visit the library."

        jump day1_hitomi_start
    elif route_choice == 'nanami':
        if winner == 'calm':
            calm "Why don't we go see what's happening in the auditorium? Nanami might need our help with her performance."

        mc "...maybe I'll go visit the auditorium."

        jump day1_nanami_start


label day1_leaving_school:
    scene hallway alt day at scene_bg
    with dissolve

    scene school day at scene_bg
    with dissolve

    "We leave the school, and start our afternoon walk back home."

    if winner == 'calm':
        "Before we can even take five steps, however, I feel a wave of energy.{p}The other voices must have come back."
    else:
        "Before we can even take five steps, however, we all feel a wave of energy, and manifest once more."

    $ start_combat()

    "Naturally, we begin fighting for the controls again."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)
        add_diversion_points(winner, 1)

    pause

    scene school day at scene_bg
    with dissolve

    python:
        is_morning_diversion = True
        is_afternoon_diversion = False
        is_day2_diversion = False
        current_location = 'school'
        call_diversion(winner, 'day1_leaving_school')

    if current_location != 'home':
        "With that diversion out of the way, we continue heading home."

        scene walk_to_school day at scene_bg
        with dissolve

        scene home day at scene_bg
        with dissolve

    "Unfortunately, as soon as we get home, our exhaustion catches back up to us."

    scene bedroom day at scene_bg
    with dissolve

    "Even though there's definitely still not even evening yet, we opt to simply head to our bed, where we almost instantly fall into a deep sleep..."

    jump day2_start
