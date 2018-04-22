# Positions for VN characters
define left = Transform(ypos=30, xpos=-80, xzoom=-1)
define right = Transform(ypos=30, xpos=300)
define center = Transform(ypos=30, xpos=80)
define flip = Transform(xzoom=-1)

define scene_bg = Transform(xpos=0, ypos=0, size=(750, 720))
define shooter_bg = Transform(xpos=750, ypos=540, size=(530, 180))

image controlgame_textbox_bg = "controlgame_textbox_bg.png"
image walk_to_school = "dummy-school.png"
image school = Placeholder('bg')
image classroom = Placeholder('bg')
image hallway = Placeholder('bg')
image theatre = Placeholder('bg')
image library = Placeholder('bg')
image home = Placeholder('bg')
image bedroom = Placeholder('bg')
image black = Solid('#000')

image hitomi happy = "hitomi/upscaled/happy.png"
image hitomi happy2 = "hitomi/upscaled/happy2.png"
image hitomi shy = "hitomi/upscaled/shy.png"
image hitomi shy2 = "hitomi/upscaled/shy2.png"
image hitomi angry = "hitomi/upscaled/angry.png"
image hitomi annoyed = "hitomi/upscaled/annoyed.png"
image hitomi curious = "hitomi/upscaled/curious.png"
image hitomi worried = "hitomi/upscaled/worried.png"

image nanami happy = "nanami/upscaled/happy.png"
image nanami angry = "nanami/upscaled/angry.png"
image nanami annoyed = "nanami/upscaled/annoyed.png"
image nanami normal = "nanami/upscaled/normal.png"
image nanami worried = "nanami/upscaled/worried.png"

define mc = Character("Kei")
define hitomi = Character("Hitomi", color="#28a25b")
define nanami = Character("Nanami", color="#ff6060")

define calm = Character("The Calm One", color="#ffffff") # The Calm One
define pyro = Character("The Pyromaniac", color="#ffa126") # The Pyromaniac
define surv = Character("The Survivor", color="#3d660e") # The Survivor
define artist = Character("The Artist", color="#6800b7") # The Artist

init python:
    #config.developer = False
    config.layers = ['game_bg', 'master', 'transient', 'screens', 'overlay']
    config.rollback_enabled = False
    config.keymap['developer'] = ['shift_F']
    config.keymap['screenshot'] = ['shift_S']

    import pygame
    import control_game
    import effects
    import game_data
    import tiles

    class ClickForwardAction(Action):
        def __call__(self):
            if control_game.allow_clickfwd:
                return True
            else:
                return None

screen ctrl_game:
    zorder 0

    key "S" action NullAction()
    key "D" action NullAction()
    key "dismiss" action ClickForwardAction()

    add control_game.MentalControlGame():
        xpos 750
        yalign 0
        size (530, 540)

label start:
    show screen ctrl_game

    scene walk_to_school at scene_bg
    show controlgame_textbox_bg at shooter_bg onlayer game_bg

    python:
        tiles.init()
        control_game.allow_clickfwd = True
        control_game.combat_in_progress = False

        control_game.player.set_surface_alpha(0)
        control_game.pyro.set_surface_alpha(0)
        control_game.survivor.set_surface_alpha(0)
        control_game.artist.set_surface_alpha(0)

        control_game.set_screen_center([750, 750])

        control_game.player.pos = [670, 950]
        control_game.pyro.pos = [910, 850]
        control_game.survivor.pos = [590, 650]
        control_game.artist.pos = [800, 550]

        control_game.pyro.turn_to(control_game.player.pos)
        control_game.survivor.turn_to(control_game.player.pos)
        control_game.artist.turn_to(control_game.player.pos)

    "I am the voice inside of [mc.name]'s head."

    "I've been here for as long as I can remember, guiding him through life as best as I can."

    "And thanks to me, [mc.name] has had a pretty calm, uneventful life so far, which is all I really want for him."

    "Unfortunately..."

    "I'm not sure why, but one day, as [mc.name] and I were walking to school..."

    "...I suddenly found two other voices sharing [mc.name]'s head with me."

    $ control_game.player.add_effect(effects.FadeEffect(control_game.player, .75, 0, 255))

    calm "Alright. Let's set things straight, here: who are you two?"

    "The first voice to speak up sounds refined and classy."

    $ control_game.pyro.add_effect(effects.FadeEffect(control_game.pyro, .75, 0, 255))

    "Voice #2" "Well, I do suppose that a round of introductions is in order." (who_color="#ffa126")

    "Voice #2" "My name is... well, I'm not really sure what my name is, but I do know that I am a man of lofty ambition." (who_color="#ffa126")

    "Voice #2" "Simply put: I wish to spread my flaming passions to everywhere I go. I want to bring the joy of light and heat to every--" (who_color="#ffa126")

    "He's quickly interrupted by a rough, growling voice."

    $ control_game.survivor.add_effect(effects.FadeEffect(control_game.survivor, .75, 0, 255))

    "Voice #3" "He means he's a fucking pyromaniac, and that his life's goal is to burn everything to the ground." (who_color="#3d660e")

    $ control_game.pyro.turn_to(control_game.survivor.pos)

    pyro "That- that is simply not true! I have many other interests other than burning! For example, I find the varying smells of gasoline to be quite--"

    "Voice #3" "Just shut up for now, okay?" (who_color="#3d660e")

    "He sighs, and we can all feel the exasperation rolling off of him."

    "Voice #3" "Okay, look. I don't know who I am or what my name is either, but there is one thing I do know:" (who_color="#3d660e")

    surv "I am a {i}survivor{/i}. I fought in the war. I've {i}seen{/i} shit out there."

    calm "--wait, what war? We're not even out of high scho--"

    surv "--like my buddy John getting sniped by one of them Krauts back in Bastogne, yeah? Horrifying stuff, really. Brains and blood, splattered all over the snow."

    "I don't bother trying to remind him that we're a student at a Japanese high school, and that World War II ended over 70 years ago."

    surv "--so yeah, I'm going to damn well make sure we're safe and secure while we operate here. I'm thinking we should go fortify a forward base and then strike against the enemy."

    pyro "Oh, please. You, {i}defending{/i} us? I doubt you could defend us from anything more than stray cats and mice."

    $ control_game.survivor.turn_to(control_game.pyro.pos)

    surv "Yeah? Well, what do {i}you{/i} know about defense then, Mister Pompous Asshole?"

    pyro "I'd say I know more about the kinds of threats we'll be facing at this {i}high school{/i} than you ever will.
    For example, I know the best ways to discreetly dispose of a charred corpse, and how to sneak gasoline onto a school campus."

    "It's at this point that we all notice a fourth presence amidst us."

    surv "Hey, who's there?! You'd better fucking show yourself, or I'll-- I'll fucking put a bullet between your eyes!"

    pyro "Please do remember that we are {i}mental constructs{/i}. How do you possibly think you're going to accomplish that?"

    pyro "Though I, myself, am rather curious about the newcomer. Why don't you show yourself?"

    $ control_game.allow_clickfwd = False

    pause 1

    $ control_game.artist.add_effect(effects.FadeEffect(control_game.artist, .75, 0, 255))
    $ control_game.allow_clickfwd = True

    "Voice #4" "...fine. Hi." (who_color="#6800b7")

    $ control_game.survivor.turn_to(control_game.artist.pos)
    $ control_game.pyro.turn_to(control_game.artist.pos)

    $ control_game.allow_clickfwd = False
    pause 2.5
    $ control_game.allow_clickfwd = True

    "There's nothing but silence for a few moments, while we wait for the newcomer to say more."

    $ control_game.allow_clickfwd = False
    pause 2.5
    $ control_game.allow_clickfwd = True

    surv "...Well? Is that it? Speak {i}up{/i}, for Christ's sake!"

    $ control_game.allow_clickfwd = False
    pause 1
    $ control_game.allow_clickfwd = True

    artist "I'm an artist. All I want to do is make artwork."

    artist "Is that enough?"

    surv "Fine. Just stay out of my fucking way, and we won't have problems. Capiche?"

    pyro "I must agree. So long as you do not disturb my mission, I see no problem with letting you pursue your artwork."

    calm "He does bring up a good point, though. We're four minds inhabiting one body. We can't share."

    $ control_game.pyro.turn_to(control_game.player.pos)

    pyro "Well, I can't be certain with regards to everyone else, but: I {i}will{/i} carry out my tasks, and if I have to fight you three somehow to do so, then I will not hesitate."

    $ control_game.survivor.turn_to(control_game.pyro.pos)

    surv "See, we're going to have a {i}problem{/i} with that, since your whole 'burning everything in sight' schtick is going to get us all killed by the enemy, here."

    artist "Both of your goals will prevent me from making art. Therefore, I will have to stop you."

    "Personally, I wouldn't want either of those two to have control at all; I just want [mc.name] to have a nice, calm, peaceful life."

    calm "So there's no way for any of us to cooperate then?"

    $ control_game.survivor.turn_to(control_game.player.pos)

    surv "Negative."

    pyro "I'm afraid not."

    artist "No."

    calm "Well, I'm sorry, but I'm afraid you all won't be able to do anything without my say-so. I still have control, and I don't think there's any way for you to take it from me."

    surv "Hrmph. Well, if that's how you want to play it... fine. But I will find a way, I promise you that."

    $ control_game.survivor.add_effect(effects.FadeEffect(control_game.survivor, .75, 255, 0))

    pyro "I suggest you watch your back from here on out. I {i}will{/i} see my mission through."

    $ control_game.pyro.add_effect(effects.FadeEffect(control_game.pyro, .75, 255, 0))

    artist "..."

    $ control_game.allow_clickfwd = False
    pause 1
    $ control_game.allow_clickfwd = True

    $ control_game.artist.add_effect(effects.FadeEffect(control_game.artist, .75, 255, 0))

    "And with that, they vanish into the recesses of [mc.name]'s mind."

    jump day0_hitomi
