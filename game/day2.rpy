label day2_start:
    $ reset_to_default_spawns()
    $ set_screen_center(control_panel_pos)

    pause

    scene bedroom day at scene_bg
    show screen ctrl_game
    with dissolve

    "The day before the festival, we wake up feeling no more rested than before."

    "And, once again, when we wake up, the controls are vacant..."

    $ start_combat()

    "Which, in the end, means yet another fight for control."

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

        current_location = 'home'

        call_diversion(winner, 'day2_start')

    if winner == 'calm':
        "With that brief interruption out of the way, [mc.name] starts walking to school."

        scene school day at scene_bg
        with dissolve
    else:
        $ voice_name = get_controlling_voice_name()

        if current_location != 'school':
            "After that diversion, [voice_name] sits back and lets [mc.name] express himself a bit, and finally he starts actually making his way to school."

            scene school day at scene_bg
            with dissolve
        else:
            "After that diversion, [voice_name] sits back and lets [mc.name] express himself a bit, and he starts actually making his way to class."

        "Of course, thanks to the diversion, we wind up being really, really late to class."

    scene hallway alt day at scene_bg
    with dissolve

    scene classroom day at scene_bg
    with dissolve

    "Class is over in the blink of an eye, though none of the students leave school immediately after class."

    "Everyone is focused on the upcoming festival.{p}Including us."

    calm "We have somewhere to be, don't we?"

    if route_choice == 'hitomi':
        jump day2_hitomi
    elif route_choice == 'nanami':
        jump day2_nanami

label day2_shopping_start:
    scene hallway alt day at scene_bg
    with dissolve

    scene school day at scene_bg
    with dissolve

    "We head outside, and start walking towards downtown."

    if voice_locked_in() is not None:
        "Before [mc.name] can get very far, however..."

        $ renpy.jump(voice_locked_in()+'_shopping_takeover') # go to shopping takeover event

    # otherwise start the endgame sequence

    "I can immediately tell, from the way [mc.name] stumbles over the first few steps down the road, that our fights for control have been taking a toll on him."

    "I don't think we'll be able to continue these fights for much longer without [mc.name]'s mind completely crumbling from the stress."

    pause

    "[mc.name] doesn't get very far before we all realize something, however:"

    "We're all quickly becoming better at reconstituting ourselves after a loss."

    "And with all of the things we have to buy, there's plenty of opportunities for us to further our own goals by forcibly diverting [mc.name] to other places."

    "Almost immediately after that shared realization, there's a subtle shift in the atmosphere..."

    $ start_combat()

    "And, once more, we're at each other throats."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)
        add_diversion_points(winner, 1)

    scene school day at scene_bg
    show screen ctrl_game
    with dissolve

    python:
        is_morning_diversion = False
        is_afternoon_diversion = False
        is_day2_diversion = True

        current_location = 'school'

        call_diversion(winner, 'day2_shopping_1')

        if voice_locked_in() is not None:
            renpy.jump(voice_locked_in()+'_shopping_takeover')
            # otherwise fallthrough to next shopping event


    ## shopping event 2
    if current_location != 'shops':
        scene shops day at scene_bg
        with dissolve

        "[mc.name], now a dazed and confused mess, stumbles his way back to downtown as our control over him briefly wavers."
    else:
        "[mc.name], now a dazed and confused mess, stumbles around downtown for a moment as our control over him briefly wavers."

    $ start_combat()

    "Of course, this just presents another opportunity for us to take control again."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)
        add_diversion_points(winner, 1)

    scene shops day at scene_bg
    show screen ctrl_game
    with dissolve

    python:
        is_morning_diversion = False
        is_afternoon_diversion = False
        is_day2_diversion = True

        current_location = 'shops'

        call_diversion(winner, 'day2_shopping_2')

        if voice_locked_in() is not None:
            renpy.jump(voice_locked_in()+'_shopping_takeover')

    ## shopping event 3
    if current_location != 'shops':
        scene shops day at scene_bg
        with dissolve

        "It's obvious to all four of us that [mc.name] is almost on the brink of a complete mental shutdown. Our influence over him wavers dangerously, and we briefly lose control entirely."

        "Despite being nearly unconscious, however, he still manages to stumble back downtown again somehow."
    else:
        "It's obvious to all four of us that [mc.name] is almost on the brink of a complete mental shutdown. Our influence over him wavers dangerously, and we briefly lose control entirely."

        "In his confusion, he simply wanders around downtown, nearly dead to the world around him."

    $ start_combat()

    "Of course, this just presents one last opportunity for us to take control again."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)
        add_diversion_points(winner, 1)

    scene shops day at scene_bg
    show screen ctrl_game
    with dissolve

    python:
        is_morning_diversion = False
        is_afternoon_diversion = False
        is_day2_diversion = True

        current_location = 'shops'

        call_diversion(winner, 'day2_shopping_3')

        if voice_locked_in() is not None:
            renpy.jump(voice_locked_in()+'_shopping_takeover')
        else:
            raise RuntimeError("A voice didn't get 4 DP! This means something is wrong with the game. Sorry!")
