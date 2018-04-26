label day1_hitomi_start:
    scene library at scene_bg
    with dissolve

    "We walk into the library. It's practically deserted."

    "All the Writing Club members seem to have left...."

    show hitomi normal at center
    with dissolve

    "...except for one, it seems."

    show hitomi shy alt at center
    with dissolve

    hitomi "Oh, [mc.name]? What are you doing here?"

    if winner == 'calm':
        mc "I didn't really feel like leaving yet, so I figured I'd go look for you."
    elif winner == "artist":
        mc "I just wanted to find some peace and quiet, I suppose."
    elif winner == "surv":
        mc "I figured I'd just check out the library, since I don't really come in here too often."
    elif winner == "pyro":
        mc "I just kind of wanted to see you, I think."

    mc "So what are you doing?"

    show hitomi worried at center
    with dissolve

    "Hitomi sighs."

    hitomi "I'm writing my pieces for the school festival. But I'm kind of stuck..."

    hitomi "I guess it's writer's block."

    mc "Writer's block, huh... maybe I can help inspire you?"

    show hitomi happy at center
    with dissolve

    hitomi "Do you think so?"

    hitomi "If that's the case, I'd appreciate the help."

    "We take a seat next to her."

    show hitomi shy at center
    with dissolve

    hitomi "So... um... where do we start?"

    mc "Hmm..."

    if winner == "artist":
        mc "Why don't we start with colors? You can get plenty of ideas from those."
    elif winner == "pyro":
        mc "Maybe you should write about something that you're passionate about."
    elif winner == "surv":
        mc "Wouldn't it be easiest to write about something that you like? I mean, like... something you'd want to protect at all costs."
    elif winner == "calm":
        mc "So what else is on your mind, other than the festival?"
