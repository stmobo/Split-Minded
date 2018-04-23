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

    "Everyone is focused on the upcoming festival."

    
