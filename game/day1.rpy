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
        call_diversion(winner, 'day1_start')

    if winner == 'calm':  # no diversion
        jump day1_start_no_diversion
    else:
        jump day1_start_diverted

label day1_start_no_diversion:
    "With that out of the way, [mc.name] starts walking to school."

    scene school day at scene_bg
    with dissolve

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
    "With that out of the way, [voice_name] sits back and stops directly controlling [mc.name], who starts walking to school on his own initiative."

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
