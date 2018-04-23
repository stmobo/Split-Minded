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

    "[mc.name] takes to the aisles with intensity bordering on anger, dashing from shelf to shelf and carefully selecting the items that suit his needs."

    artist_mc "Paints... aquamarine, viridian, charteruse, burnt umber..."

    "As we walk along the back of the store, however, something in particular catches [mc.name]'s eye."

    "It's a large, white piece of clothing of some sort, haphazardly placed on a T-shaped stand.{p}In front of it, on the ground, lies a large bag with a zipper."

    artist_mc "A smock and a bag. This will do."

    "[mc.name] takes the smock and holds it up to himself. As expected, it completely covers our body and drapes across the floor."

    "Throwing the smock over our shoulder, [mc.name] quickly gathers up the bag and the rest of his supplies, pays for them, and leaves the store."

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
