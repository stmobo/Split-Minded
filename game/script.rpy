# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("<main character>")
define hitomi = Character("Hitomi", color="#28a25b")
define nanami = Character("Nanami", color="#ff6060")

image hitomi happy = "hitomi/upscaled/happy.png"

define calm = Character("The Calm One", color="#ffffff") # The Calm One
define pyro = Character("The Pyromaniac", color="#ffa126") # The Pyromaniac
define surv = Character("The Survivor", color="#3d660e") # The Survivor
define artist = Character("The Artist", color="#6800b7") # The Artist

init python:
    config.rollback_enabled = False  # rollback doesn't make sense with this game
    config.keymap['developer'] = ['shift_F']
    config.keymap['screenshot'] = ['shift_S']

    import control_game
    import effects
    import pygame

    class ClickForwardAction(Action):
        def __call__(self):
            if control_game.allow_clickfwd:
                return True
            else:
                return None

    left = Transform(ypos=30, xpos=-50)


screen ctrl_game:
    key "S" action NullAction()
    key "D" action NullAction()
    key "dismiss" action ClickForwardAction()

    add control_game.MentalControlGame():
        xpos 750
        yalign 0
        size (530, 530)

label start:
    show screen ctrl_game

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    python:
        control_game.allow_clickfwd = True

        control_game.player.set_surface_alpha(0)
        control_game.pyro.set_surface_alpha(0)
        control_game.survivor.set_surface_alpha(0)
        control_game.artist.set_surface_alpha(0)

        control_game.set_screen_center([1200, 1200])

        control_game.player.pos = [1120, 1400]
        control_game.pyro.pos = [1360, 1300]
        control_game.survivor.pos = [1040, 1100]
        control_game.artist.pos = [1200, 1000]

        control_game.pyro.turn_to(control_game.player.pos)
        control_game.survivor.turn_to(control_game.player.pos)
        control_game.artist.turn_to(control_game.player.pos)

    "We're not sure why, but one day, as we were walking to school..."

    "...we woke up to find four of ourselves talking to each other."

    $ control_game.player.add_effect(effects.FadeEffect(control_game.player, 5.0, 0, 255))

    calm "Alright. Let's set things straight, here: who are you two?"

    "The first voice to speak up sounds refined and classy."

    $ control_game.pyro.add_effect(effects.FadeEffect(control_game.pyro, 5.0, 0, 255))

    "Voice #2" "Well, I do suppose that a round of introductions is in order." (who_color="#ffa126")

    "Voice #2" "My name is... well, I'm not really sure what my name is, but I do know that I am a man of lofty ambition." (who_color="#ffa126")

    "Voice #2" "Simply put: I wish to spread my flaming passions to everywhere I go. I want to bring the joy of light and heat to every--" (who_color="#ffa126")

    "He's quickly interrupted by a rough, growling voice."

    $ control_game.survivor.add_effect(effects.FadeEffect(control_game.survivor, 5.0, 0, 255))

    "Voice #3" "He means he's a fucking pyromaniac, and that his life's goal is to burn everything to the ground." (who_color="#3d660e")

    pyro "That- that is simply not true! I have many other interests other than burning! For example, I find the varying smells of gasoline to be quite--"

    $ control_game.pyro.turn_to(control_game.survivor.pos)

    "Voice #3" "Just shut up for now, okay?" (who_color="#3d660e")

    "He sighs, and we can all feel the exasperation rolling off of him."

    "Voice #3" "Okay, look. I don't know who I am or what my name is either, but there is one thing I do know:" (who_color="#3d660e")

    surv "I am a {i}survivor{/i}. I fought in the war. I've {i}seen{/i} shit out there."

    calm "--wait, what war? We're not even out of high scho--"

    surv "--like my buddy John getting sniped by one of them Krauts back in Bastogne, yeah? Horrifying stuff, really. Brains and blood, splattered all over the snow."

    "I don't bother trying to remind him that we're a student at a Japanese high school, and that World War II ended over 70 years ago."

    surv "--so yeah, I'm going to damn well make sure we're safe and secure while we operate here, deep behind enemy lines."

    pyro "Oh, please. You, {i}defending{/i} us? I doubt you could defend us from anything more than stray cats and mice."

    surv "Yeah? Well, what do {i}you{/i} know about perimeter security then, Mister Pompous Asshole?"

    $ control_game.survivor.turn_to(control_game.pyro.pos)

    pyro "I'd say I know more about the kinds of threats we'll be facing at this {i}high school{/i} than you ever will.
    For example, I know the best ways to discreetly dispose of a charred corpse, and how to sneak lighter fluid onto a school campus."

    "It's at this point that we all notice a fourth presence amidst us."

    surv "Hey, who's there?! You'd better fucking show yourself, or I'll-- I'll fucking put a bullet between your eyes!"

    pyro "Please do remember that we are {i}mental constructs{/i}. How do you possibly think you're going to accomplish that?"

    pyro "Though I, myself, am rather curious about the newcomer. Why don't you show yourself?"

    $ control_game.allow_clickfwd = False

    pause 1

    $ control_game.artist.add_effect(effects.FadeEffect(control_game.artist, 5.0, 0, 255))
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

    calm "He does bring up a good point, though. We're four minds inhabiting one body. How are we supposed to share?"

    pyro "Well, I can't be certain with regards to everyone else, but: I {i}will{/i} carry out my tasks, even if I must seize control by force."

    return
