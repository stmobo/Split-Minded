# For when the Pyro wins the Day 0 fight (same as Diversion 1, but at night)
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

    "[mc.name] immediately heads for the back of the store, and carefully looks through the shelves."

    pyro_mc "Let's see, let's see... matches, matches..."

    surv "When I said you would burn the house down, I didn't mean it as a suggestion."

    pyro_mc "No, no. Burning our own house down would severely limit the number of things we could burn in the future. This is just preparation."

    calm "Do you realize we're actually talking to ourselves out there? You know, in the outside world?"

    pyro_mc "So? I don't think there's anyone of consequence here.{p}Oh! There they are!"

    "The Pyro finds the matches he was looking for, at the bottom of one of the shelves."

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

label pyro_diversion_1:
    "The Pyromaniac quickly asserts control over [mc.name]."

    pyro "Ah, I've won. Excellent. Now..."

    pyro_mc "Let's get to business, shall we?"

    scene walk_to_school day at scene_bg
    with dissolve

    "The Pyro forcibly diverts [mc.name] out towards the streets near our house."

    pyro_mc "There was a convenience store near here, that I saw earlier..."

    "After a few minutes of walking, we find the store."

    pyro_mc "Ah, perfect."

    scene konbini at scene_bg
    with dissolve

    "[mc.name] immediately heads for the back of the store, and carefully looks through the shelves."

    pyro_mc "Let's see, let's see... matches, matches..."

    surv "{i}Please{/i} don't try to burn our house down or anything stupid like that."

    pyro_mc "No, no. Burning our own house down would severely limit the number of things we could burn in the future. This is just preparation."

    calm "Preparation, huh."

    pyro_mc "Yes, for all the things we will burn later. Oh, there they are!"

    "The Pyro finds the matches he was looking for, at the bottom of one of the shelves."

    "Picking them up, we quickly pay for them and leave."

    $ current_location = 'walk_to_school'

    return

label pyro_diversion_2:
    "The Pyromaniac asserts control over [mc.name] once again."

    pyro "Excellent. Now..."

    pyro_mc "Back to what I was doing."

    scene shops day at scene_bg
    with dissolve

    "The Pyro leads [mc.name] further into the city, towards the commercial district."

    pyro_mc "There is a big hardware store in this part of the city, if I recall correctly. We're going there."

    scene hardware_store day at scene_bg
    with dissolve

    "We quickly find the place, and the Pyro leads us inside."

    scene hardware_store inside at scene_bg
    with dissolve

    "He immediately brings us towards the power equipment section of the store."

    artist "...what are we doing here?"

    pyro_mc "We're not looking for much. I just need one thing..."

    "After spending a few minutes wandering through the store, we eventually come across some lawnmowers on display."

    "Something on a shelf catches the Pyro's attention."

    pyro_mc "Ah, I think those are it!"

    "We quickly walk over, and see what exactly the Pyro was looking for:"

    pyro_mc "Gas canisters. Perfect."

    surv "You know those are empty, right?"

    pyro_mc "Yes, but we can fill them later. I know there's a gas station near our house that's self-service; we can go there."

    surv "Do you really think any of us would want to help you with that?"

    pyro_mc "No, which is why I was planning to do it myself."

    scene hardware_store day at scene_bg
    with dissolve

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We leave the store, gas cans in hand, and quickly drop them off at home."

    $ current_location = 'home'

    return

# danger zone
label pyro_diversion_3:
    "The Pyromaniac asserts control over [mc.name] for the third time."

    pyro "Finally!"

    pyro_mc "I've been waiting for this opportunity!"

    if not is_morning_diversion:
        scene walk_to_school day at scene_bg
        with dissolve

        scene home day at scene_bg
        with dissolve

        "The Pyro leads [mc.name] back home, nearly giddy with excitement."

    "We pick up the gas cans that we bought earlier, and head outside."

    scene walk_to_school day at scene_bg
    with dissolve

    "We turn, and set off down the street."

    scene gas_station at scene_bg
    with dissolve

    "In a few short minutes, we come across a small corner gas station."

    pyro_mc "Yes, this is the gas station I remembered."

    "We head inside the station's store and pay for a pump. In cash, of course."

    pyro_mc "Pump number 3, please."

    "Back outside, the Pyro quickly sets about filling up the gas cans, humming as he does so."

    surv "You're really excited about this, aren't you?"

    pyro_mc "Of course! This brings me ever closer to burning flames!"

    surv "No kidding. But still, I need to ask: why fire?"

    pyro_mc "Huh?"

    surv "Of all the things you could love and be fixated about... why does it have to be fire?"

    pyro_mc "...that's a really good question, and deep one. Surprising, coming from you."

    pyro_mc "But if I had to give an answer... I guess it's just an innate part of me?"

    pyro_mc "Like asking why water is wet, or why the wind blows. It's just who I am."

    "With a {i}thump{/i}, the pump shuts off, leaving us with several filled cans of gasoline."

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "The filled cans are heavy, but with some effort we manage to bring all of them home in one go."

    $ current_location = 'home'

    return

# point of no return
label pyro_diversion_4:
    "The Pyromaniac asserts control over [mc.name] so quickly and seamlessly that we can barely notice it."

    pyro "I'm getting used to this, it seems."

    pyro_mc "On to business."

    if not is_morning_diversion:
        scene walk_to_school day at scene_bg
        with dissolve

        scene home day at scene_bg
        with dissolve

        "Walking at a brisk pace, the Pyro brings [mc.name] back home."

    "The Pyro takes one of the blankets inside of our house and uses them as a makeshift sack, placing a few tightly-capped cans of gas inside."

    surv "Huh. Where are we taking these?"

    scene walk_to_school day at scene_bg
    with dissolve

    pyro_mc "Out to school, of course."

    calm "Wait, are you serious? What if we get caught?"

    pyro_mc "We won't get caught. Trust me."

    "We walk to school with the gas. We get a few strange looks along the way, but no one bothers to stop or ask us about what we're carrying."

    scene school back day at scene_bg
    with dissolve

    "We avoid going in via the front gate, however, and instead circle around to the back of the school."

    pyro_mc "Hmm... now where should I put these..."

    "We walk around the back parts of the school, hiding the gas cans one by one in bushes, underneath stairwells, behind rocks, and so on."

    "It takes us a good half-hour or so, but eventually we hide them all."

    pyro_mc "Excellent. Now I won't have to carry these all the way from home before the festival."

    calm "The festival?"

    pyro_mc "Yes. See, my ultimate goal here, is..."

    pause # dramatic

    pyro_mc "...to burn down the entire school on the day of the festival."

    pause # more dramatics

    calm "...you're definitely serious about this."

    pyro_mc "Of course! Why wouldn't I be?"

    calm "Shit."

    "And with the rate things are going, he's definitely going to be able to do just that..."

    $ current_location = 'school'

    return

label pyro_shopping_takeover:
    $ voice_name = get_controlling_voice_name(True)
    "[mc.name]'s mental exhaustion suddenly overcomes us, nearly crushing us with a wave of fatigue and deabilitiation."

    if voice_in_control == 'pyro':
        "The Pyro powers through it surprisingly quickly, though, and uses the opportunity to do something none of us expected."
    elif voice_in_control == 'calm':
        "The Pyro seems much less affected by it, however, and takes advantage of my temporary weakness to do something none of us expected."
    else:
        "The Pyro seems much less affected by it, however, and takes advantage of The [voice_name]'s temporary weakness to do something none of us expected."

    "Using the energy he's accumulated from his previous battles and control takeovers, he quickly forces myself into control and locks himself in with a mental block."

    "Those of us left outside immediately sense a change."

    surv "Huh? What just happened?"

    calm "The Pyro just did something to the controls."

    pyro "I've locked myself into the controls. If I'm correct, your energy will be too drained from the constant battles to take control anymore."

    surv "Why you little-- I'll show you!"

    "I can feel him futilely try to struggle against the barrier The Pyro's set up. He gets nowhere, of course."

    "And for me... it's over. The Pyro's permanently taken control."

    "All I can do is just sit and watch what he does."

    jump pyro_endgame


label pyro_endgame:
    python:
        complete_fadeout()
        reset_to_default_spawns()
        set_screen_center(control_panel_pos)
        set_control('pyro')

    pause

    scene bedroom day at scene_bg
    show screen ctrl_game
    with dissolve

    "It's the day of the festival."

    "[mc.name], under the Pyro's control, doesn't even bother going to school that day."

    "Instead, he waits until the evening, until the festival opens, before making his way to the school."

    if pyro_diversion_points < 4:
        "Naturally, he brings some cans of gas along with him, wrapped and hidden inside a blanket."

    scene walk_to_school evening at scene_bg
    with dissolve

    scene school back at scene_bg
    with dissolve

    "[mc.name] circles around and enters the school grounds near the back. It's completely deserted-- all of the excitement of the festival is towards the front of the school."

    if pyro_diversion_points < 4:
        "Then, he begins liberally dousing the school with the cans of gas he brought along with him."
    elif pyro_diversion_points >= 4:
        "Then, he begins liberally dousing the school with the cans of gas he'd hid around the grounds."

    "With that done, he takes a match and..."

    $ complete_fadeout()

    "...the entire school is lit aflame."
