# When Calm wins the day 0 fight
label calm_day0_winner:
    "And that's how I kept control even after the others tried to kill me."

    calm "That was... frightening.{p}How did all of this happen?"

    pyro "Good show there, Mr. Calm."

    calm "Wait, what? I thought I..."

    pyro "As I said before, I don't think we can truly die.{p}We just fade, for a moment."

    calm "...so you all will be back to try and take over again."

    surv "You betcha."

    calm "Fuck."

    pyro "Rather unfortunately, I think it will take some time for us to reconstitute ourselves.{p}So we'll be seeing you later, rather than sooner."

    "...{p}I feel their presences vanish."

    "And with that out of the way, I guide [mc.name] back to sleep..."

    $ complete_fadeout()

    jump day1_start

# When Calm wins the day 1 morning fight
label calm_day1_start:
    "I quickly reassert control over [mc.name]'s mind as well as my own, racing thoughts."

    "It takes me a couple of minutes, but eventually I feel stable enough to continue on."

    $ current_location = 'home'

    return

label calm_day1_leaving_school:
    "I regain control over [mc.name]'s mind, trying to do so as quickly and smoothly as I can."

    "There's a brief moment of instability that I fail to avoid, however-- one that seems to last worryingly long."

    "It passes, though, and [mc.name] quickly catches his bearings."

    $ current_location = 'school'

    return

label calm_day2_start:
    "I assert control over [mc.name]'s mind once more."

    "As soon as he tries to take a step, however, he goes dizzy, trips, and falls, nearly winding up on his face."

    "When he tries to get up, again, the same thing happens, and he winds up back on the ground."

    "I end up having to take direct control of him to get him upright and steady again-- if only enough so to guide him to a chair."

    "After a few worry-filled minutes, however, he seems to have regained enough mental strength to stand up and start moving again."

    "I give him a slight mental prod to speak, just to make sure that's still working..."

    mc "...I-- what-- ...what was {i}that{/i}...?"

    "...I decide it's good enough for now. It'll probably fade over time as we walk to school.{p}Hopefully."

    $ current_location = 'home'

    return

label calm_day2_shopping_1:
    "I try to guide [mc.name] to the first store on our list-- but he trips and falls almost immediately when I do so."

    scene store day at scene_bg
    with dissolve

    "In the end, I end up taking direct control of him, so that we can at least buy the things we need from this store and go."

    $ current_location = 'store'

    return


label calm_day2_shopping_2:
    "I preemptively take direct control of [mc.name], so that we can go and buy some of the things on our list."

    scene hardware_store day at scene_bg
    with dissolve

    "My direct control gives much better results when we get to the store and buy things, compared to when I tried to get him to do it on his own."

    "Naturally, this does not reassure me."

    $ current_location = 'store'

    return


label calm_day2_shopping_3:
    "I preemptively take direct control of [mc.name], simply to prevent him from collapsing on the spot."

    scene shops day at scene_bg
    with dissolve

    "I don't even try going very far-- just to the nearest bench, to give [mc.name] a mental breather."

    "It takes him a bit over 30 minutes to regain enough mental strength to get up again and, with an unsteady gait, start shuffling around."

    "Before I have the opportunity to do anything else, however..."

    $ current_location = 'shops'

    return



label calm_shopping_takeover:
    $ voice_name = get_controlling_voice_name(True)
    "[mc.name]'s mental exhaustion suddenly overcomes us, nearly crushing us with a wave of fatigue and deabilitiation."

    if voice_in_control == 'calm':
        "I quickly power through it, though, and use the opportunity to do something I've been waiting for this whole time."
    else:
        "I feel much less affected by it, however, and take advantage of The [voice_name]'s temporary weakness to do something I've been waiting for this whole time."

    "Using the energy I've accumulated from my previous battles and control takeovers, I quickly force myself into control and lock myself in with a mental block."

    "The others immediately sense a change."

    surv "Huh? What just happened?"

    pyro "The Calm One just did something to the controls."

    calm "I've locked myself in, here. You guys can't take control anymore-- you're too weak from the constant battles, right?"

    surv "Why you little-- I'll show you!"

    "I can feel him futilely try to struggle against the barrier I've set up. He gets nowhere, of course."

    "It feels good to be back in control. Permanently.{p}Just like before."

    jump calm_endgame

label calm_endgame:
    python:
        complete_fadeout()
        reset_to_default_spawns()
        set_screen_center(control_panel_pos)
        set_control('calm')

    $ who_needed_stuff = '<somebody>'
    if route_choice == 'hitomi':
        $ who_needed_stuff = 'Hitomi and the Writing Club'
    else:
        $ who_needed_stuff = 'Nanami and the Drama Club'

    "After dropping off everything [who_needed_stuff] needed yesterday, we immediately went home and collapsed onto our bed."

    scene bedroom evening at scene_bg
    show screen ctrl_game
    with dissolve

    "And, when we woke up, much {i}much{/i} later, it was already the evening of the school festival."

    "After quickly freshening up and putting on a new uniform, we head back up to the school."

    scene school evening at scene_bg
    show crowd at scene_bg
    with dissolve

    "Fortunately, we make it to the school not long after the festival's start--{w} but even from here we can tell that it's in full swing.{p}The school grounds are bustling with activity."

    scene hallway evening at scene_bg
    show crowd thin at scene_bg
    with dissolve

    "We walk past dozens of booths and stalls on our way through the school grounds, and I make sure to take note of the ones we're most interested in."

    "Of course, there's one particular thing at the festival that we need to go see above all else."

    if route_choice == 'hitomi':
        jump hitomi_calm_endgame
    else:
        jump nanami_calm_endgame

label calm_closeout: # The Calm One's last words to round out the story.
    "And meanwhile, in the control room, there's a smile plastered across my face."

    "Because, even if things were a bit... {w=0.5}{i}heated and uncertain{/i}, to say the least, over the past few days..."

    "We still did a damn good job."

    "And everything should be fine, from here on out."

    $ complete_fadeout()

    "\n{p}...right?"

    "~ Fin ~"

    # and that's all for now, folks
