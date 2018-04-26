# For when the Survivor wins the Day 0 fight
label survivor_day0_winner:
    "And that's how the Survivor seized the controls from me."

    surv "Hah! Who's a mental construct {i}now{/i}, Pyro?"

    pyro "All of us, last I checked."

    surv "Well, fuck you anyways! I'm taking control now!"

    surv "And wait, how are you still around, anyways?"

    pyro "As I said: I don't think we can truly die. We just fade, for a moment."

    calm "...so we have an opportunity to take control again."

    surv "Yeah, maybe.{p}But if you think I'm going to go down to the likes of you, you've got another thing coming!"

    surv "Anyways, I think..."

    surv_mc "...I think we should go recon the area."

    scene home night dark at scene_bg
    with dissolve

    scene walk_to_school night dark at scene_bg
    with dissolve

    "Grabbing a notebook and pencil, he quickly brings [mc.name] out of the house and out into the street."

    artist "What area?"

    surv_mc "Huh?"

    artist "What are we observing?"

    surv_mc "Well, I was thinking we should recon that facility we went to this morning. It seems to be highly important to the enemy, seeing as how so many of them congregate there."

    calm "You mean the school?"

    surv_mc "Yeah, that place!"

    scene school night dark at scene_bg
    with dissolve

    surv_mc "No security here at night, it seems."

    calm "...they even left the front gate wide open."

    surv_mc "Our enemy's negligence plays into our hands, it seems."

    scene school back night dark at scene_bg
    with dissolve

    "We circle around the school, with the Survivor noting every window and door that seems to be unlocked."

    surv_mc "North-northeast door, by the open field... seems to be unlocked and disused. Potential entry point..."

    scene school night dark at scene_bg
    with dissolve

    "By the time he's satisfied, it's almost 3 o'clock in the morning."

    surv_mc "There, finished. Every single potential entrance and hole in their defenses, mapped out and listed for our eyes only!"

    scene walk_to_school night dark at scene_bg
    with dissolve

    scene home night dark at scene_bg
    with dissolve

    scene bedroom night dark at scene_bg
    with dissolve

    "We head back home to our bed, and [mc.name] falls asleep nearly instantly."

    $ complete_fadeout()

    jump day1_start


label survivor_diversion_1:
    "The Survivor quickly asserts control over [mc.name]."

    surv "Hah! I won! Take {i}that{/i}, you assholes!{p}So let's see here, how did you guys get this to work..."

    surv_mc "Aha! Got it!"

    pyro "Oh, great. Try not to run into any walls, while you're--"

    if is_day2_diversion:
        scene shops day at scene_bg
        with vpunch
    elif is_morning_diversion:
        scene home day at scene_bg
        with vpunch
    elif is_afternoon_diversion:
        scene hallway alt day at scene_bg
        with vpunch

    surv_mc "Ouch!"

    pyro "--figuring out how to walk. You idiot."

    surv_mc "These legs are hard to work with, okay?!"

    "We quickly pick ourselves back up, and take a look around."

    if is_day2_diversion:
        surv_mc "So, anyways! I think we should go recon that big facility we keep going to."
    elif is_morning_diversion:
        surv_mc "So, anyways! I think we should go recon that big facility we went to yesterday."
    elif is_afternoon_diversion:
        surv_mc "So, anyways! I think we should go recon this place."

    artist "...recon?"

    surv_mc "Yeah. Scope out the place, look for insecure entry points, things like that."

    pyro "You're going to reconnoiter the school."

    surv_mc "Exactly!"

    if not is_afternoon_diversion:
        scene walk_to_school day at scene_bg
        with dissolve

        scene school_back day at scene_bg
        with dissolve

        "We make our way to the school, and instead of walking up to the front gate, circle around to the back."
    else:
        scene school_back day at scene_bg
        with dissolve

        "We exit at the back of the school, and hide behind some plants."

    "The Survivor pulls out a notebook and pen, and starts walking around the school, noting every unlocked window and unused entrance."

    surv_mc "North-northeast door, by the open field... seems to be unlocked and disused. Potential entry point..."

    "By the time he's satisfied, it's nearly an hour later."

    surv_mc "There, finished. Every single potential entrance and hole in their defenses, mapped out and listed for our eyes only!"

    calm "So wait, what was the purpose of this?"

    surv_mc "Son, good intelligence is vital to winning any war.{p}'If you know both yourself and your enemy, you can win a hundred battles', yeah?"

    return

label survivor_diversion_2:
    "The Survivor asserts control over [mc.name] again."

    surv "Hah, I'm in the driver's seat again!"

    surv_mc "On to the next objective!"

    surv_mc "Say, do any of you know where that hardware store was? You know, the one we saw earlier?"

    calm "...why do you want to know?"

    pyro "And why do you think we'd tell you?"

    artist "...down the street. Take a left at the second intersection."

    surv_mc "Hah! I knew I could count on you, Artist."

    scene walk_to_school day at scene_bg
    with dissolve

    scene shops day at scene_bg
    with dissolve

    scene hardware_store day at scene_bg
    with dissolve

    "We follow the Artist's directions, and quickly come to a hardware store."

    surv_mc "Ah, there we are."

    calm "So wait, what are we doing here?"

    surv_mc "I need to requisition some supplies."

    calm "...for what, exactly?"

    surv_mc "I'm afraid you're not cleared for that knowledge yet, Calm."

    calm "Seriously?"

    scene hardware_store inside at scene_bg
    with dissolve

    "The Survivor immediately finds the carpentry section of the store, and starts picking out random pieces of wood and boxes of nails."

    surv_mc "Yeah, these'll do..."

    "He quickly takes his things to the checkout counter and leaves."

    scene shops day at scene_bg
    with dissolve

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We leave the wood and nails in a big pile in the living room."

    return

label survivor_diversion_3:

label survivor_diversion_4:
