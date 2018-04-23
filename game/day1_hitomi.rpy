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

    show hitomi curious at center
    with dissolve

    hitomi "So... where do we start?"

    mc "Hmm..."

    if winner == "artist":
        mc "Really, you can find inspiration in anything: love, the sky, your dreams... why don't we start with those?"

        hitomi "My dreams? Love? ...well, now that I think about it..."
    elif winner == "pyro":
        mc "Maybe you should write about something that you're passionate about."

        hitomi "Passionate? ...Well, I guess it's not something I'm {i}passionate{/i} about, but..."
    elif winner == "surv":
        mc "Wouldn't it be easiest to write about something or someone that you care about? I mean, like... someone you'd want to protect at all costs."

        hitomi "Someone I care about? ...well, now that you mention it..."
    elif winner == "calm":
        mc "Is there anything on your mind, other than the festival?"

        hitomi "Well... since you're asking..."

    show hitomi shy alt at center
    with dissolve

    hitomi "I have a... a friend. And she's known this boy for a really long time..."

    hitomi "But they're not as close as they were before. And..."

    hitomi "She's... {size=-10}kindofinlovewithhim.{/size}"

    mc "Huh? What was that?"

    hitomi "I meant she's in... love with him."

    hitomi "But they're drifting apart, and now she thinks he's out of reach."

    mc "Hmm...{p}You know, Hitomi..."

    show hitomi shy at center
    with dissolve

    hitomi "Yes, [mc.name]?"

    mc "...that would make a really good theme for a poem.{p}You know, unrequited love?"

    show hitomi thinking at center
    with dissolve

    hitomi "Yeah... I guess you're right."

    hitomi "I could... write it from her perspective, I suppose?"

    mc "Yeah, that could work."

    hitomi "..."

    hitomi "...what if I started the poem with this line, then.."

    "She put her pen to paper, and began to write."

    "Hitomi puts intense thought and care into every word she writes and re-writes."

    "We fall into silence at her side, not wanting to break her focus."

    "Eventually, she comes to something she's satisfied with."

    hitomi "There. I think it's complete."

    mc "Oh? Can I read it?"

    "She pulls the poem close to her chest."

    hitomi "Hmm... no."

    show hitomi happy at center
    with dissolve

    hitomi "I'll read it at the festival. If you want to hear it, you'll have to come visit me there."

    mc "Then I'll definitely make sure to drop by."

    hitomi "I'll hold you to that.{p}See you later."

    jump day1_leaving_school
