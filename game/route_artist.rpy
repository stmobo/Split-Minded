# For when the Artist wins the Day 0 fight
label artist_day0_winner:
    "And that's how the Artist seized the controls from me."

    artist "...I won?"

    surv "For such a quiet guy, you sure fight fiercely."

    artist "...it's what I do."

    calm "Wait, how are we still talking?"

    pyro "As I said before: I don't think we can truly die. We just fade, for a moment."

    calm "So we have an opportunity to take control again."

    artist "...I won't lose to you."

    "[mc.name] stands up, and walks to the window."

    "We stare outside for a moment."

    pyro "Artist? You there?"

    artist_mc "Supplies. I need supplies."

    scene home night dark at scene_bg
    with dissolve

    scene walk_to_school night dark at scene_bg
    with dissolve

    scene shops night light at scene_bg
    with dissolve

    "The Artist brings [mc.name] outside, onto the street, and quickly starts walking in the direction of an arts and crafts store we passed by, on our way to school this morning."

    scene store night light at scene_bg
    with dissolve

    "It's still open, even this late at night."

    scene art_store at scene_bg
    with dissolve

    "The Artist takes to the aisles with intensity bordering on anger, dashing from shelf to shelf and carefully selecting the items that suit his needs."

    artist_mc "Paints... aquamarine, viridian, charteruse, burnt umber..."

    "As we walk along the back of the store, however, something in particular catches The Artist's eye."

    "It's a large, white piece of clothing of some sort, haphazardly placed on a T-shaped stand.{p}In front of it, on the ground, lies a large bag with a zipper."

    artist_mc "A smock and a bag. This will do."

    "The Artist takes the smock and holds it up to himself. As expected, it completely covers our body and drapes across the floor."

    "Throwing the smock over our shoulder, he quickly gathers up the bag and the rest of his supplies, pays for them, and leaves the store."

    scene walk_to_school night dark at scene_bg
    with dissolve

    scene home night dark at scene_bg
    with dissolve

    "It's almost midnight by the time we get back."

    scene bedroom night dark at scene_bg
    with dissolve

    "We dump the things we bought in a corner of the living room, and we quickly head back to bed."

    "[mc.name] falls asleep almost instantly..."

    $ complete_fadeout()

    jump day1_start

label artist_diversion_1:
    "The Artist quickly asserts control over [mc.name]."

    artist_mc "Supplies. I need supplies."

    scene walk_to_school day at scene_bg
    with dissolve

    scene shops day at scene_bg
    with dissolve

    "The Artist quickly starts walking in the direction of an arts and crafts store we passed by, on our way to school this morning."

    scene store day at scene_bg
    with dissolve

    "We quickly walk inside."

    scene art_store at scene_bg
    with dissolve

    "The Artist takes to the aisles with intensity bordering on anger, dashing from shelf to shelf and carefully selecting the items that suit his needs."

    artist_mc "Paints... aquamarine, viridian, charteruse, burnt umber..."

    "As we walk along the back of the store, however, something in particular catches The Artist's eye."

    "It's a large, white piece of clothing of some sort, haphazardly placed on a T-shaped stand.{p}In front of it, on the ground, lies a large bag with a zipper."

    artist_mc "A smock and a bag. This will do."

    "The Artist takes the smock and holds it up to himself. As expected, it completely covers our body and drapes across the floor."

    "Throwing the smock over our shoulder, he quickly gathers up the bag and the rest of his supplies, pays for them, and leaves the store."

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We quickly make our way home, supplies in tow."

    "We dump the things we bought in a corner of the living room."

    $ current_location = 'home'

    return


label artist_diversion_2:
    "The Artist quickly reasserts control over [mc.name]."

    artist_mc "Need more supplies."

    scene walk_to_school day at scene_bg
    with dissolve

    scene shops day at scene_bg
    with dissolve

    "The Artist quickly makes his way back to the arts and crafts store he visited last time."

    scene store day at scene_bg
    with dissolve

    scene art_store at scene_bg
    with dissolve

    "He seems to be searching for something specific, this time."

    "He quickly finds what he's looking for, however, and holds his sought-after items up to the light for inspection."

    pyro "...knives and scissors?"

    artist_mc "Yes. These will suffice."

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We quickly make our way home, with the Artist's tools."

    "He carefully places them on an unused area of our dining table."

    $ current_location = 'home'

    return


label artist_diversion_3:
    "The Artist smoothly takes control over [mc.name] for the third time."

    artist_mc "Need a few more supplies."

    scene walk_to_school day at scene_bg
    with dissolve

    scene shops day at scene_bg
    with dissolve

    scene hardware_store day at scene_bg
    with dissolve

    "The Artist swiftly walks to the hardware store, this time."

    surv "The hardware store?"

    artist_mc "Yes. Need carpentry tools and material. Wood and a saw, mostly."

    scene hardware_store inside at scene_bg
    with dissolve

    "The Artist darts over to the lumber section of the hardware store, and picks out a few of the oddest-looking pieces available, as well as a large hand saw."

    artist "These will be perfect."

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We quickly make our way home, with the Artist's last materials."

    "He carefully places them on an unused area of our dining table, next to the scissors and knives."

    $ current_location = 'home'

    return


label artist_diversion_4:
    "The Artist smoothly takes control over [mc.name] for the fourth time, and for some reason I immediately get a chill down my figurative spine."

    artist_mc "Need one last thing for my masterpiece."

    pyro "Oh, is that what you were making? I was curious to see what you were doing with all of these things."

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "The Artist quickly grabs the saw and canvas bag off the dining table, and dons the smock, before heading outside again."

    scene shops day at scene_bg
    with dissolve

    "The Artist quickly walks downtown-- but doesn't go to any of the stores. Instead, he goes and walks into an alleyway."

    "Within the alleyway, we find a homeless man, slumped against the wall. There are a number of beer bottles in a pile next to him, and he appears to be asleep."

    "Before any of us have time to react, the Artist violently grabs the homeless man by the neck, and slices it open with one quick motion from the saw."

    "The man's blood splatters all over the smock, and he dies almost instantly with a soft gurgling sound."

    "Afterwards, the Artist swiftly and efficiently begins dismembering the man, neatly fitting the bodyparts within the bag."

    "The whole affair is over in less than 15 minutes, after which the Artist hides the bloody smock and saw inside the bag as well."

    "It's as clean as it is horrifying: there's hardly a trace of blood or evidence on our body, clothing, or in the alleyway."

    scene walk_to_school day at scene_bg
    with dissolve

    "We're all shocked into silence by the whole thing, however."

    "The Survivor is the first to regain the ability to speak."

    surv "Wha-- {i}what the fuck{/i}, Artist? What the hell was that?!"

    artist_mc "It was art."

    "The finality of that statement precludes any further discussion."

    scene home day at scene_bg
    with dissolve

    "We come home, and the Artist leaves the bag and its gruesome contents underneath the dining table."

    $ current_location = 'home'

    return


label artist_shopping_takeover:
    $ voice_name = get_controlling_voice_name(True)
    "[mc.name]'s mental exhaustion suddenly overcomes us, nearly crushing us with a wave of fatigue and deabilitiation."

    if voice_in_control == 'artist':
        "The Artist powers through it surprisingly quickly, though, and uses the opportunity to do something none of us expected."
    elif voice_in_control == 'calm':
        "The Artist seems much less affected by it, however, and takes advantage of my temporary weakness to do something none of us expected."
    else:
        "The Artist seems much less affected by it, however, and takes advantage of The [voice_name]'s temporary weakness to do something none of us expected."

    "Using the energy he's accumulated from his previous battles and control takeovers, he quickly forces myself into control and locks himself in with a mental block."

    "Those of us left outside immediately sense a change."

    pyro "Eh? What just happened?"

    calm "The Artist just did something to the controls."

    surv "I'm locked in. It's nice and quiet in here, now..."

    pyro "Why you little-- I'll show you!"

    "I can feel him futilely try to struggle against the barrier The Artist's set up. He gets nowhere, of course."

    "And for me... it's over. The Artist's permanently taken control."

    "All I can do is just sit and watch what he does."

    jump artist_endgame

label artist_endgame:
    python:
        complete_fadeout()
        reset_to_default_spawns()
        set_screen_center(control_panel_pos)
        set_control('artist')

    pause

    scene bedroom cloudy at scene_bg
    show screen ctrl_game
    with dissolve

    "It's the early, early morning before the festival. The sun is barely out."

    scene walk_to_school cloudy at scene_bg
    with dissolve

    scene school front cloudy at scene_bg
    with dissolve

    "[mc.name], under the Artist's control, swiftly makes his way to the school, with his saw, smock, and other supplies at the ready."

    if route_choice == 'hitomi':
        scene auditorium cloudy at scene_bg
        with dissolve
        "Briefly darting inside, he finds something surprising: Nanami is curled up against one of the walls in the auditorium alongside some other members of the Drama Club."

        "Apparently, they had too much work to finish for their performance to leave the night before."
    elif route_choice == 'nanami':
        scene library at scene_bg
        with dissolve
        "Briefly darting inside, he finds something surprising: Hitomi is fast asleep inside the library, her head down on a desk, alongside other members of the Writing Club."

        "Apparently, they had too much work to finish for their festival event to leave the night before."

    scene school back cloudy at scene_bg
    with dissolve

    "[mc.name] picks up the girl's surprisingly light body, and quietly carries her outside, without waking her."

    "As [mc.name] lays her on the ground and readies his saw, she stirs briefly."

    if route_choice == 'hitomi':
        nanami "Wha... [mc.name]... what are--"
    elif route_choice == 'nanami':
        hitomi "Hmm... [mc.name]? ...what are--"

    "Without a word, [mc.name] slices her neck open in one saw-stroke."

    "She dies almost instantly with a soft gurgling sound."

    if artist_diversion_points < 4:
        "[mc.name] immediately sets about dismembering her body, haphazardly throwing the parts into the bag."
    else:
        "[mc.name] immediately sets about dismembering her body, neatly placing the parts into the bag alongside the ones from before."

    scene school front cloudy at scene_bg
    with dissolve

    "Walking around to the front, [mc.name] begins work on his final masterpiece..."

    $ complete_fadeout()

    "...when the first students find him that morning, their eyes are filled with horror and disgust as they see what he's created."
