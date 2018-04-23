label day1_start:
    $ reset_to_default_spawns()
    $ set_screen_center(control_panel_pos)

    pause

    scene bedroom day at scene_bg
    show screen ctrl_game
    with dissolve

    "We still feel exhausted when we wake up the next day."

    "[mc.name] drags himself out of bed and starts going about his morning routine purely on autopilot..."
