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

    surv "Hah! I won! Take {i}that{our/i}, you assholes!{p}So let's see here, how did you guys get this to work..."

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

    $ current_location = 'school'

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

    $ current_location = 'home'

    return


label survivor_diversion_3:
    "The Survivor asserts control over [mc.name] for the third time."

    surv_mc "There we go. Hey, I think I'm getting used to this!"

    pyro "Unfortunately."

    scene walk_to_school day at scene_bg
    with dissolve

    scene shops day at scene_bg
    with dissolve

    scene hardware_store day at scene_bg
    with dissolve

    "The Survivor quickly brings [mc.name] out to the hardware store."

    artist "Here again?"

    surv_mc "Yeah... I need some more supplies, see?"

    scene hardware_store inside at scene_bg
    with dissolve

    "We quickly head inside.{p}The Survivor pulls out his notebook again."

    surv_mc "Let's see... what first..."

    "The first section we visit seems to carry a wide variety of electrical cables and equipment."

    surv_mc "I'll need that... and that..."

    "The Survivor picks out an equally wide selection of cables and sautering equipment."

    "As we're walking down one of the aisles near the back of the store, a shiny black spool of wire catches the Survivor's eye."

    surv_mc "Wait, is that..."

    "He picks up the spool and inspects it."

    calm "...barbed wire?"

    surv_mc "Heh, this is a pleasant surprise. I didn't know they sold this stuff here."

    "After picking up a few more items-- pipes, tools, batteries, nails, screws, and so on-- we pay for our things and leave."

    scene shops day at scene_bg
    with dissolve

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We dump the things in the same disorganized pile left from our previous hardware store trip."

    $ current_location = 'home'

    return


label survivor_diversion_4:
    "The Survivor asserts control over [mc.name] so smoothly, we can barely notice it."

    surv_mc "Heheh. Just one last thing I need to get..."

    scene walk_to_school day at scene_bg
    with dissolve

    scene shops day at scene_bg
    with dissolve

    scene hardware_store day at scene_bg
    with dissolve

    scene hardware_store inside at scene_bg
    with dissolve

    "The Survivor quickly brings us back to the hardware store once more, and heads for the outdoors section."

    "There, he picks up a large bag of fertilizer."

    pyro "...ammonium nitrate?"

    surv_mc "Yeah. It's the last thing I need from here."

    calm "Wait, isn't that the stuff people use in homemade explosives?"

    surv_mc "Yep. Or at least, I think so."

    scene shops day at scene_bg
    with dissolve

    scene walk_to_school day at scene_bg
    with dissolve

    scene home day at scene_bg
    with dissolve

    "We quickly bring the ammonium nitrate back home, and set it off to the side."

    "The Survivor looks over the large pile of stuff from the hardware store that's accumulated in our living room."

    calm "Wood, nails, barbed wire, electrical cables, and fertilizer.{p}What are you planning to do with these?"

    surv_mc "Well, at this point I might as well tell you..."

    surv_mc "I've received vital intelligence regarding the movements of the enemy around the school."

    surv_mc "They're planning some sort of major operation tomorrow."

    calm "...the school festival?"

    surv_mc "Yeah, whatever. Anyways, we need to strike back and make a stand."

    surv_mc "So I've been gathering these materials to fortify a central position to base myself in during the enemy operation."

    calm "...you're going to make some kind of bunker. In the middle of the school."

    surv_mc "Yeah. I'm thinking about hunkering down in that big room with the books."

    pyro "That's a library, you idiot."

    surv_mc "Oh, that's what it was? I thought it was just some random storeroom."

    "The Survivor sits down at our kitchen table, and starts filling some pipes with fertilizer."

    "He then starts taking some matches, and wrapping bare, thin electrical wire around them..."

    surv_mc "Then just wire that to this, connect this... drop this in here..."

    surv_mc "...and... there. This looks good, eh?"

    "In our hands is a pipe bomb."

    pyro "Just... try not to get us blown up, okay?"

    surv_mc "Son, you know I can't make that promise. War is dangerous, okay?"

    $ current_location = 'home'

    return
