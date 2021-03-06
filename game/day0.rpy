label day0_hitomi:
    python:
        set_voice_visible('pyro', False)
        set_voice_visible('artist', False)
        set_voice_visible('survivor', False)

    "And with the other three voices gone, I am left in peace with [mc.name] as we walk to school."

    "The walk is uneventful, but I can feel [mc.name]'s attention being pulled towards the stores and shops we passed by on the way to school."

    mc "... crafts store, convenience store..."

    mc "... a hardware shop? I didn't realize one of those was around here..."

    scene school day at scene_bg
    with dissolve

    "We're at the school in no time."

    "That confrontation earlier must have stopped us for longer than I thought, because we barely make it to class on time."

    scene classroom day at scene_bg
    with dissolve

    "For some reason, neither [mc.name] nor I can focus at all during class. Everything just goes in one ear and out the other."

    calm "This must have something to do with those other voices..."

    "During lunch, we hear one of our classmates calling our name from behind us."

    hitomi "[mc.name]?"

    show hitomi worried at center
    with dissolve

    hitomi "[mc.name]? Are you okay?"

    mc "Huh? Oh, um... Hi, Hitomi?"

    hitomi "You seem to be a bit out of sorts today. Are you feeling well?"

    mc "Yeah, I'm... okay. Sorry, just a bit distracted."

    hitomi "Distracted? By what?"

    mc "Nothing in particular. I've just been thinking about random things, I guess?"

    hitomi "Things?"

    mc "Like cans of gas, and art supplies, and stuff. I'm not sure why. But I'm not sick, I think."

    hitomi "If you say so..."

    show hitomi happy at center
    with dissolve

    hitomi "Well, try to not actually get sick, okay? It wouldn't do for you to get sick right before the school festival."

    mc "Speaking of, what are you doing for the festival, Hitomi?"

    show hitomi happy alt at center
    with dissolve

    # NOTE: should it be a Literature Club or a Writing Club? Either way, she's going to be eerily reminiscent of DDLC...
    hitomi "Well, the Writing Club will be doing open prose and poetry recitals in the library."

    hitomi "You're still not part of any clubs, right?"

    mc "Yeah..."

    hitomi "Then you should come see us. Even if you don't recite anything yourself, listening to others read could be fun."

    show hitomi shy at center
    with dissolve

    hitomi "And, um, I will be reciting a few poems there, too, so if you could come and see that would be really nice."

    mc "If I get an opportunity to, then I'll definitely try to visit. And I'm not really going to be doing anything else, so..."

    show hitomi happy at center
    with dissolve

    hitomi "That's good to hear."

    "The lunch bell rings at that moment, interrupting our conversation."

    jump day0_nanami

label day0_nanami:
    scene hallway day at scene_bg
    with dissolve

    "The rest of our classes come and go, and before we know it we're done for the day."

    "[mc.name] is still as distracted as before, though, and instead of going home, we end up wandering down the halls, not paying attention to where we're going..."

    scene hallway day at scene_bg
    with vpunch

    "...and it's not long before we accidentally knock someone over."

    nanami "Oi, watch where you're going!"

    show nanami annoyed at center
    with dissolve

    "The girl quickly dusts herself off, though, and springs to her feet."

    mc "Ah, sorry, Nanami."

    show nanami normal at center
    with dissolve

    nanami "Wait, [mc.name]? What are you doing here? You're not part of a club or anything, right?"

    mc "I, uh... I'm not really sure. Just wandering, I guess?"

    show nanami worried at center
    with dissolve

    nanami "...are you okay? You're looking a bit... iunno, tired, it seems?"

    mc "Yeah, I'm fine, I'm fine. Just a bit distracted."

    mc "What are you doing?"

    show nanami happy at center
    with dissolve

    nanami "Oh, I'm rehearsing with the Drama Club, for the school play."

    nanami "You're coming to the festival, right?"

    mc "Yeah."

    nanami "Then you should definitely come and see the play! It's going to be awesome!"

    show nanami annoyed at center
    with dissolve

    nanami "Of course, assuming the idiots making the sets get them done in time..."

    mc "Do you need any help?"

    show nanami happy at center
    with dissolve

    nanami "I think we're fine right now, but thanks for the offer!"

    show nanami normal at center
    with dissolve

    nanami "Honestly, though, you should probably go get some rest or something. You don't look so good."

    mc "...yeah, you're right. I'll see you, then."

    nanami "Try not to get sick or anything, yeah?"

    jump day0_end

label day0_end:
    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    scene bedroom day at scene_bg
    with dissolve

    "By the time we get back home, we're almost completely exhausted mentally."

    "It's all we can do to drag ourselves to our bedroom, hit the lights, and fall asleep in our uniform."

    show black
    hide screen ctrl_game
    with dissolve

    pause

    python:
        set_screen_center(None)
        set_player_movement_allowed(True)
        set_combat_status(True)
        set_player_weapon_controllable(False)

    "Suddenly, I'm jolted back into awareness by a sound.{p}Footsteps."

    scene bedroom night dark at scene_bg
    show screen ctrl_game
    with dissolve

    calm "What? Who's there?"

    "I notice that, for some reason, I have a sword in my hand."

    python:
        set_voice_target('survivor', 'player')
        set_voice_target('pyro', 'player')
        set_voice_target('artist', 'player')

        control_game.survivor.add_effect(effects.FadeEffect(control_game.survivor, .75, 0, 255))
        control_game.pyro.add_effect(effects.FadeEffect(control_game.pyro, .75, 0, 255))
        control_game.artist.add_effect(effects.FadeEffect(control_game.artist, .75, 0, 255))

    artist "Hi."

    python:
        set_voice_visible('pyro', True)
        set_voice_visible('artist', True)
        set_voice_visible('survivor', True)

    pyro "Oh, you got a weapon as well? That makes things slightly more complicated."

    calm "What's happening? What is this?"

    surv "It's a coup, dumbass. We want to run things our own way, and you're getting in the way of that."

    pyro "If it's any consolation, though, I don't think we can truly die, being mental constructs."

    artist "But we can kill you over and over again."

    calm "So, what? You're going to kill me and take control?"

    surv "Exactly."

    $ start_combat()

    "..."

    python:
        complete_fadeout()
        winner = end_combat()

        set_control(winner)
        add_diversion_points(winner, 1)

    pause

    scene bedroom night dark at scene_bg
    show screen ctrl_game
    with dissolve

    $ day0_diverted = True

    if winner == "calm":
        $ day0_diverted = False
        jump calm_day0_winner
    elif winner == "surv":
        jump survivor_day0_winner
    elif winner == "pyro":
        jump pyro_day0_winner
    elif winner == "artist":
        jump artist_day0_winner
