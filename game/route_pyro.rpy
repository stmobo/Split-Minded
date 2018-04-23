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

    return

# Diversions 5, 6, and 7 always happen during the end-game shopping segment
label pyro_diversion_5:
    "The Pyromaniac reassumes control over [mc.name]."

    pyro_mc "Hmm... well, I've got everything I need for my main goals, don't I?"

    pyro_mc "I'm sure I'll find something to do. I have extra gas at home, if I recall..."

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We return home, and pick up an extra can of gas lying around the house."

    scene walk_to_school day at scene_bg
    with dissolve

    "Heading back out onto the street, the Pyro's attention is immediately captured by a sleek black car several doors down."

    pyro_mc "Ah, that looks flammable! And expensive, too!"

    "He quickly dashes to the car, gas can in hand."

    calm "Oh no."

    "Of course, none of us can do anything to stop him."

    "The Pyro pours the entire can out onto the car, and the gas seeps into it, working its way through the gaps in the windows and the body..."

    "Then the Pyro pulls a matchbook from his pocket, and picks out a match."

    "With a single deft stroke, he lights the match and tosses it onto the car."

    "We immediately turn to run away, the fireball's heat scorching the hairs on the back of our neck."

    "Running back to our home, we dive behind our trash bin and watch the flames from there."

    pyro_mc "It's so beautiful..."

    surv "I wonder where the owner is."

    artist "Orange, red, yellow..."

    calm "We're definitely going to get arrested, at the rate we're going..."

    return
