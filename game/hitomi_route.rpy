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

label day2_hitomi:
    scene hallway day at scene_bg
    with dissolve

    scene library at scene_bg
    with dissolve

    "We walk back into the library, and this time find what seems to be the entire Writing Club in a frenzy of activity."

    "Hitomi immediately catches sight of us when we walk in, and runs up to us with worry written all across her face."

    show hitomi worried at center
    with dissolve

    hitomi "I'm so glad you're here, [mc.name]."

    hitomi "We're trying to decorate the library before the festival tomorrow, and we just realized there are a number of items we need here that we don't have on hand."

    hitomi "But we need everyone here to decorate and make other preparations."

    hitomi "Could you go out instead and buy the supplies we need, please?"

    mc "Of course I can. Do you have a list of what I should buy?"

    hitomi "Certainly. Here."

    "She pulls out a notebook from her uniform pocket, and neatly tears out a sheet of paper from it, handing it to us."

    "There's a list of various things written on it in Hitomi's ever-neat handwriting.{p}We quickly skim through it."

    mc "Lined paper, pens, construction paper ... candles, flour ... an HDMI cable ..."

    mc "There's a lot of different things on here. It might take me a while to go to all of the stores for these."

    hitomi "It's okay. The school will be open all night, tonight, for everyone who still needs to make preparations before the festival."

    hitomi "And we have many things we still need to finish here, so don't worry about time."

    mc "Alright, then. I guess I'll be going?"

    show hitomi happy at center
    with dissolve

    hitomi "Thank you so much for everything you've done, [mc.name]. You're a wonderful friend."

    jump day2_shopping_start


label hitomi_calm_endgame:
    "So, we immediately make our way towards the library."

    scene library festival at scene_bg
    with dissolve

    "It's been massively rearranged.{p}All of the tables have been pushed around to create a little audience seating area, in front of a podium."

    "All of the writing club members are here, of course.{p}Including, of course..."

    show hitomi smiling alt_hair at center
    with dissolve

    hitomi "Ah, [mc.name]! You made it!"

    mc "Of course. I wouldn't want to miss you reading your poem, right?{p}And nice hairdo, by the way."

    hitomi "You like it? I wanted to try something different, for the festival."

    "Before she can say anything else, one of the other Writing Club members comes up to her."

    "Writing Club Member" "Hey, Hitomi, are you ready to go up and recite? I think you're up next."

    "The girl seems to realize we're there, and shoots a few glances between us and Hitomi."

    "Writing Club Member" "Oh, sorry! Was I, uh, {w=0.5}{i}interrupting{/i}{w=0.5} anything?"

    show hitomi shy alt_hair at center
    with dissolve

    hitomi "N-no, you weren't interrupting anything! I was just talking to a-- a friend.{p}And yes, I think it is my turn to recite."

    hide hitomi with dissolve

    "She steps up to the podium, poem in hand."

    "After taking a moment to steady herself and take a breath, she begins reading her poem to us..."

    show hitomi reciting alt_hair at center
    with dissolve

    # "Every day, I imagine a future where I can be with you~"
    # "In my hand, is a pen that will write a poem~ of me and you~"

    pause .75

    # I'll figure out a poem later

    hide hitomi with dissolve

    "Everyone begins clapping as Hitomi finishes reading her poem."

    "After she steps out from behind the podium, however, she walks up to one of the Writing Club members and hands them something, before quickly stepping out of the library."

    "[mc.name] briefly wonders whether we should follow her--{w} but we remain seated, for the sake of politeness to the other Writing Club members."

    "It's not long before someone else comes up to the podium to recite their work."

    jump hitomi_confession


label hitomi_confession:  # in which Kei is basically deaf
    scene library festival at scene_bg
    with dissolve

    "Eventually, however, the Writing Club member from before walks up to us, and hands us a folded piece of paper."

    "Writing Club Member" "So, um, Hitomi wanted you to have this, but for some reason she wanted me to wait a while before I gave it to you. She said she needed 'time to prepare', whatever that means."

    "Writing Club Member" "So... here, I guess?"

    "We carefully unfold the paper and read through it."

    "It seems to be the paper Hitomi wrote her poem on.{p}However, at the very bottom, she's written us a short note..."

    # maybe use a special screen for this?
    hitomi "{i}Please come to the cherry blossom trees behind the school.\n{p}There's something I have to tell you.{/i}"

    "I look up. It looks like most of the Writing Club is done reciting their poems-- {w}they're busy dragging some poor freshman up to the podium--{w} so we quietly slip out of the library."

    scene hallway alt cloudy at scene_bg
    with dissolve

    "The sky outside the windows is already dark and starry.{p}Did the sun really set that quickly?"

    scene school back night light at scene_bg
    with dissolve

    "The rear portions of the school are practically deserted-- most of the excitement of the festival is occuring further towards the school's front."

    scene school back sakura at scene_bg
    with dissolve

    "Of course, there were still some decorations put up, even here."

    show hitomi shilouette alt_hair at center
    with dissolve

    "We find Hitomi easily, shilouetted against the lights strung up on the trees."

    "She's turned to face away from us, staring wistfully into the blossoms falling around her."  # holy shit this is so cliche

    show hitomi alt_hair worried at center
    with dissolve

    "She turns to us as soon as we walk up to her, however."

    hitomi "[mc.name]! Y-You really came!{p}I was so worried that you wouldn't..."

    mc "Of course I would have shown up, Hitomi.{p}So, what's up?"

    hitomi "Well... do you remember, the friend I told you about, when I was writing my poem?"

    mc "Yes?"

    hitomi "That...{w=0.5} {size=-5}friend... {/size} {w=0.75}{size=-8}wasme.{/size}{p=0.75}{size=-11}AndI'minlovewithyou.{/size}"

    mc "..."

    "[mc.name] is silent for a moment, and I can tell from the instruments on the control panel that he's struggling to process the sounds he's hearing.{p}Because..."

    hitomi "[mc.name]?"

    mc "...\n{fast}I'm sorry, Hitomi, but..."

    show hitomi shocked alt_hair at center
    with dissolve

    hitomi "W-wait, [mc.name]-- d-don't tell me, you're rej--"

    mc "...\nI'm sorry, Hitomi, but...\n{fast}...you'll have to speak up."

    mc "I couldn't hear you.{p}What did you say?"

    "We all stand there, in a stunned silence."

    "Hitomi's expression is frozen across her face, {p}I'm trying to not bang my head repeatedly on the controls, {p}and [mc.name] is simply--{w}purely--{w}confused beyond speech."

    show hitomi shy angry alt_hair at center
    with dissolve

    "Hitomi quickly recovers from that bit of denseness on [mc.name]'s part.{p}She still seems to be at a loss for words, however."

    hitomi "You didn't-- {w}did you really not-- {w}I--"

    show hitomi annoyed alt_hair at center
    with dissolve

    "Hitomi groans, and her annoyance is obvious to everyone here--{w}except for [mc.name], of course."

    hitomi "...how did I even fall in love with someone as dense as you, anyways?"

    mc "Wait, hang on-- what? Fall in love?{p}You're-- you're joking, right?"

    show hitomi annoyed closeup alt_hair at center
    with dissolve

    "She takes a few steps forward, right up against [mc.name]'s rapidly beating heart."

    hitomi "Just-- please stay quiet for now, [mc.name].{w} Please."

    show hitomi shy eyes_closed closeup alt_hair at center
    with dissolve

    "Then she closes her eyes..."

    scene hitomi_kiss_cg
    hide screen ctrl_game
    with dissolve

    "...{fast}and kisses [mc.name]."

    pause 0.5

    "And meanwhile, in the control room, there's a smile plastered across my face."

    "Because, even if things were a bit... {w=0.5}{i}heated and uncertain{/i}, to say the least, over the past few days..."

    "We still did a damn good job."

    "And everything should be fine, from here on out."

    $ complete_fadeout()

    "\n{p}...right?"

    # and that's all for now, folks
