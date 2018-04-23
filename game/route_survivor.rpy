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

    "We circle around the school, with the Survivor noting every window and door that seems to be unlocked."

    surv_mc "North-northeast door, by the open field... seems to be unlocked and disused. Potential entry point..."

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
