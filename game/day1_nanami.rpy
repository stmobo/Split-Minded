label day1_nanami_start:
    scene auditorium day at scene_bg
    with dissolve

    "We walk into the auditorium, which is full of activity and chatter."

    "The Drama Club is definitely working hard towards their performance."

    show nanami reciting at center
    with dissolve

    "Up on stage, Nanami recites what seems to be a few of her lines.{p}As she finishes, though, she catches sight of us."

    show nanami happy at center
    with dissolve

    nanami "Oh, [mc.name]! Hi! What are you doing here?"

    if winner == 'calm':
        mc "I didn't really feel like leaving yet, so I figured I'd come and see if you needed any help."

        nanami "Well, I definitely think you're just in time..."
    elif winner == "artist":
        mc "I was just curious, and wanted to come see what you were doing."

        nanami "Well, you're definitely not going to be disappointed by it."
    elif winner == "surv":
        mc "I don't really come over here too often-- so I just wanted to come and check it out, I guess?"

        nanami "Well... it's the auditorium. What else is there to see?"
    elif winner == "pyro":
        mc "I just kind of wanted to see you and your performance, really."

        show nanami shy at center
        with dissolve

        nanami "Well, um, thanks, I guess? Ehehe..."

    show nanami annoyed at center
    with dissolve

    nanami "Well, anyways! Since you're here, could you help us make some of the sets?"

    nanami "The guys who were {i}supposed{/i} to be making them had to bail on us {i}today{/i}, of all days, so we're seriously short on free hands backstage."

    nanami "If you could lend us a hand, that would be really great."

    mc "Well, okay then."

    show nanami happy

    nanami "Great! Follow me."

    scene auditorium backstage at scene_bg
    show nanami excited at center
    with dissolve

    "As we walk behind the curtain and into the wings, Nanami yells out to a group of students kneeling next to some unfinished set backdrops."

    nanami "Okay, everyone! This is [mc.name], and he's here to help us out with the sets for today. Treat him well, okay?"

    "With a small nudge she pushes us towards the students, before running back out onstage."

    "Drama Club Student" "So Nanami dragged you into helping us?"

    mc "Yeah, kind of. But, I mean, I'm happy to help."

    "Drama Club Student" "Hey, no sweat. We're happy to have you. It's just a shame that {i}some{/i} of our club members are slacking off and leaving us to do the work, you know?"

    mc "So what's with them? Why aren't they here?"

    "Drama Club Student" "They don't really care about the club. They never have."

    "Drama Club Student" "So, yeah, this is normal for them."

    "Drama Club Student" "Sometimes, I wonder why they're still even a part of the club.{p}Hey, can you pass me the red paint?"

    "We start helping the Drama Club paint the sets. Though they're huge, there's a surprising level of detail in the outlines that leaves us impressed."

    "After a while though, we hear something that causes us to look up, and out onto the stage.{p}Music, and a voice."

    show nanami reciting at center
    with dissolve

    "Nanami seems to be singing something in the center of the stage."

    nanami "{i}Suddenly I'm in the cockpit!{/i}{p}{i}Suddenly, everything's changed~{/i}"

    "Drama Club Student" "[mc.name]? You watching Nanami?"

    mc "Oh! Um, yeah..."

    "Drama Club Student" "Yeah, she has that effect on people. You get used to it, though."

    mc "Really..."

    "[mc.name] gets entranced, watching her for the next few minutes without even realizing it."

    "Up in [mc.name]'s head, I can feel something else as well.{p}It's small, and almost drowned out by our influence, but..."

    "They're undoubtedly [mc.name]'s own feelings.{w} He's in love."

    calm "Do you guys feel that, too?"

    artist "It's love, right?"

    pyro "Certainly. Such passion..."

    surv "This kid's in love, huh? Interesting..."

    hide nanami
    with dissolve

    "Eventually, however, we return to our work."

    "After some more time and effort, we manage to finish painting the sets."

    "Drama Club Student" "Well, that's all we can do today."

    "Drama Club Student" "Thanks for the help, [mc.name]."

    mc "No problem. Hey, uh... is it a problem if I come back tomorrow?"

    "Drama Club Student" "I was actually about to ask if you could. There's a few more things we'll have to do to finish up once the paint dries, and I think we'll need your help again."

    mc "So I'll see you tomorrow then."

    "Drama Club Student" "I guess you will. See you."

    show nanami happy at center
    with dissolve

    "Nanami waves to us as we exit the auditorium."

    nanami "Hey, thanks for your help today, [mc.name]! Seeya!"

    jump day1_leaving_school
