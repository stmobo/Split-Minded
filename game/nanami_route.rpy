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

label day2_nanami:
    scene hallway day at scene_bg
    with dissolve

    scene auditorium day at scene_bg
    with dissolve

    "We make our way back to the auditorium, and find everyone there in a frenzy of activity."

    "Nanami immediately notices us when we walk in, and runs up to us, worry etched across her face."

    show nanami worried at center
    with dissolve

    nanami "Oh, thank goodness you're here! The set crew just realized they're missing a ton of things they need for the play, and we need every hand on deck here to finish preparations."

    nanami "Do you think you could run out and go buy those things for us?"

    mc "Of course. Do you have a list or anything?"

    nanami "Yeah, yeah! Um, wait, hang on."

    hide nanami with dissolve
    pause 0.5
    show nanami worried with dissolve

    "She runs off backstage, and comes back with a piece of paper."

    nanami "Here it is. There's not actually a whole lot of stuff on the list, but some of the things here are kind of hard to find. You'll probably need to go to a bunch of different stores."

    nanami "Don't worry about taking too long. At the rate things are going, we're going to be here all night anyways."

    mc "Alright then. I guess I'll be going, then."

    nanami "Thank you so much for all your help, [mc.name]. Seriously, you don't know how much you've done for us."

    jump day2_shopping_start

label nanami_calm_endgame:
    "So, we immediately make our way towards the auditorium."

    scene auditorium evening at scene_bg
    show crowd at scene_bg
    with dissolve

    "Everything is set up for tonight's production.{p}There's already a ton of people here, waiting for the show to begin."

    "We take a seat, and eventually, the performance starts."

    "The play--or is it a musical?-- seems to be about airplanes."

    show nanami reciting alt_clothes alt_hair at center
    with dissolve

    "Nanami, naturally, plays one of the lead roles, and seems all dressed up for the part--she's even sporting a new hairstyle."

    "She plays her part like a pro, captivating the entire audience with the emotion and force behind her lines."

    "The performance is over almost all too quickly."

    hide nanami with dissolve

    "[mc.name] seems to be stuck in a sort of daze as he gets up from his seat."

    "As we're about to walk out of the auditorium, however, someone taps our shoulder from behind.{p}It's the Drama Club member we worked alongside on the sets, two days ago."

    "Drama Club Member" "Hey, [mc.name]! I thought I'd find you here.{p}Listen, the Drama Club's having a small party on the rooftop to celebrate the performance. Care to join us?"

    "Watching the controls, I notice a large spike in [mc.name]'s hesitation-- but I override it."

    mc "Uhm... yeah, sure, I guess?"

    "Drama Club Member" "Great! I've gotta go clean up some stuff backstage first-- but I'll see you there!"

    jump nanami_confession

label nanami_confession:  # in which Kei gets a "nervous love confession" scene of his very own.
    scene roof night at scene_bg
    show crowd thin at scene_bg
    with dissolve

    "We make our way to the rooftop."

    "Pretty much the entire Drama Club is up here already, celebrating the success of the production."

    "And, of course, [mc.name] has no idea who any of these people are."

    "For his sake, however, I silence the second thoughts running through the back of his mind."

    "It's all I can do, however, to make him awkwardly shuffle to the back edge of the rooftop, against the railing."

    "After a few minutes of silently gazing down at the brightly lit school grounds, however, a familiar voice approaches us from behind."

    show nanami happy alt_clothes at center
    with dissolve

    nanami "Hiya, [mc.name]! Great show tonight, huh?"

    "I try to not make the anxiety and nerves in [mc.name] too obvious in his voice."

    mc "Yeah, you really put on a nice performance..."

    "Nanami, of course, seems to pick up on it instantly."

    show nanami wide_smile alt_clothes at center
    with dissolve

    nanami "Ehe, thanks!\nBut you know, we really couldn't have done it without you.{p}You did as much for this performance as I did."

    mc "Eh... I kind of have a hard time believing that."

    show nanami normal alt_clothes at center
    with dissolve

    mc "Eh... I kind of have a hard time believing that.{fast}\nI mean, come on. I just kind of showed up two days before the performance and helped out a bit."

    mc "And you're... you know, one of the leading roles."

    nanami "Sure, you may have shown up towards the end.{p}{i}Buuut,{/i} when you did, it was at the exact right time, to fill in for a place that no one else could."

    show nanami annoyed alt_clothes at center
    with dissolve

    nanami "Which is still much more than {i}some{/i} of our supposed 'members' did."

    show nanami happy alt_clothes at center
    with dissolve

    nanami "So wipe that gloomy look off your face, [mc.name]!{p}You're one of us, now. You belong here."

    "Before [mc.name] can stammer his way through another response, however, a voice calls out to us from a few feet away.{p}It's the guy from before."

    "Drama Club Member" "[mc.name]! You actually did decide to show up! How are you--"

    "It takes him a second to notice that we're not alone, here.{p}He looks back and forth between Nanami and [mc.name], before putting on a sheepish grin."

    "Drama Club Member" "Hehe, shoot. Was I interrupting anything? I'll go ahead and leave you two alone, if you'd like."

    show nanami questioning alt_clothes at center
    with dissolve

    "[mc.name]'s heart rate and nervousness surge in response to this, but Nanami just seems confused and unaware of the implications somehow."

    nanami "...no, you weren't interrupting anything? I mean, I was trying to get this guy to be a bit less awkward, here, but it's nothing private."

    "Drama Club Member" "Eh, seriously? [mc.name] hasn't--"

    "Before I can react, [mc.name] decides to seize on the first course of action to come to mind, and gestures at the drama club member."

    mc "{i}Aaaaaand,{/i} um, hey...{p}You know, I, uh, never got your name. What was it?"

    "Drama Club Member" "...wait, seriously?"

    show hiro normal at left
    show nanami questioning alt_clothes at right
    with dissolve

    hiro "My name's Hiro. How did we not introduce ourselves to each other?"

    "[mc.name] shrugs."

    mc "Beats me."

    show hiro smiling at left
    with dissolve

    hiro "Eh, whatever. We'll have time to chat later-- {w}but if I'm correct, [mc.name], {i}you{/i} have {i}something{/i} to say to Nanami, right?"

    "[mc.name] picks up on the implication a split second after Hiro says that, bringing his nervousness back in full force."

    mc "Ehhh... well, um. Maybe? That's, um, you see--"

    hiro "--well, anyways. I'm going to get out of your hair now.\nLater, and good luck, [mc.name]!"

    hide hiro
    show nanami normal alt_clothes at center
    with dissolve

    nanami "...what was {i}that{/i} all about?{p}And, more importantly: what did you have to say to me, [mc.name]?"

    "[mc.name]'s mind completely blanks out at this point, all of his thoughts replaced by thoughts of doom and curses on Hiro's name."

    "So, I intervene.{p}I gather up whatever scraps of courage we've got left, and with a few keypresses, use them up."

    mc "Well, um, you know two days ago, when I showed up and helped with the sets?{p}Well, you were rehearsing on stage, and I was kind of watching you while I worked..."

    # man, I love using this "shrinking text" schtick
    mc "And I {size=-3}kinda-{/size}{size=-5}sorta{/size}{size=-7}mighthave{/size}{size=-9}falleninlove{/size}{size=-11}withyou?{/size}"

    "[mc.name]'s voice dies as he forces that sentence out, and his heart nearly follows suit."

    "We sit there, for a second or two, in silence.{p}Then Nanami starts chucking softly."

    show nanami happy alt_clothes at center
    with dissolve

    nanami "Oh, [mc.name]. I-- {w}I was not expecting that.{p}I'm not even sure how I didn't notice--"

    nanami "--but now that I think back about it, it was really, {i}really{/i} obvious!{p}I'm not even sure what to say."

    hide crowd
    show nanami shy smiling closeup alt_clothes at center
    with dissolve

    "She takes a few steps closer to us, cupping our face in her hands.\nThe crowd around us seems to vanish as our focus converges on Nanami."

    nanami "But, um, [mc.name]? I {i}do{/i} accept your confession."

    show nanami shy eyes_closed closeup alt_clothes at center
    with dissolve

    "With that said, she closes her eyes..."

    scene nanami_kiss_cg
    hide screen ctrl_game
    with dissolve

    "...and kisses [mc.name]."

    pause 0.5

    jump calm_closeout
