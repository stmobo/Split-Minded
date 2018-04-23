# For when the Pyro wins the Day 0 fight
label pyro_day0_winner:
    "And that's how the Pyromaniac seized the controls from me."

    calm "No, no, no! This can't be happening..."

    surv "Fucking fantastic. First I get killed in this mind-space-thing by you three, and now I'm going to {i}actually{/i} get killed when this lunatic sets the fucking house on fire or something."

    pyro "You really should just relax, you two. I'll take it from here."

    calm "The idea of you having control makes it hard for me to relax.{p}Also, wait, how are we..."

    pyro "As I said: I don't think we can truly die. We just fade, for a moment."

    calm "So we have a chance to take control again."

    pyro "Certainly. But I've already won once. I can do it again."

    pyro "In any case..."

    pyro_mc "Let's get to business, shall we?"

    scene home night dark at scene_bg
    with dissolve

    scene walk_to_school night dark at scene_bg
    with dissolve

    "He brings [mc.name] out of the house and into a convenience store down the street."

    scene konbini at scene_bg
    with dissolve

    "[mc.name] immediately heads for the back of the store, and carefully looks through the shelves..."

    pyro_mc "Let's see, let's see... matches, matches..."

    surv "When I said you would burn the house down, I didn't mean it as a suggestion."

    pyro_mc "No, no. Burning our own house down would severely limit the number of things we could burn in the future. This is just preparation."

    calm "Do you realize we're actually talking to ourselves out there? You know, in the outside world?"

    pyro_mc "So? I don't think there's anyone of consequence here.{p}Oh! There they are!"

    "[mc.name] finds the matches he was looking for, at the bottom of one of the shelves."

    "Picking them up, we quickly pay for them and leave."

    scene walk_to_school night dark at scene_bg
    with dissolve

    scene home night dark at scene_bg
    with dissolve

    scene bedroom night dark at scene_bg
    with dissolve

    "We head back to our home and bed, and [mc.name] falls asleep without further ado..."

    $ complete_fadeout()

    jump day1_start
