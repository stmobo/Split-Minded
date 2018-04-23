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

    "After the dust settles, the one left standing is..."

    pause
