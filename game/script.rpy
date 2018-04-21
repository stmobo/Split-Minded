# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("<main character>")
define hitomi = Character("Hitomi", color="#28a25b")
define nanami = Character("Nanami", color="#ff6060")

image hitomi happy = "hitomi/happy.png"

define voc1 = Character("The Calm One", color="#ffffff") # The Calm One
define voc2 = Character("The Pyromaniac", color="#ffa126") # The Pyromaniac
define voc3 = Character("The Survivor", color="#663d20") # The Survivor
define voc4 = Character("The Artist", color="#6800b7") # The Artist


init python:
    config.rollback_enabled = False  # rollback doesn't make sense with this game
    config.keymap['developer'] = ['shift_F']
    config.keymap['screenshot'] = ['shift_S']

    import control_game
    import pygame

    class MentalControlGame(renpy.Displayable, NoRollback):
        def __init__(self, **kwargs):
            super(MentalControlGame, self).__init__(**kwargs)

            self.last_st = 0
            self.primary_surf = pygame.Surface(control_game.screen_native_dims)
            self.screen_sz = None

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEMOTION and self.screen_sz is not None:
                control_game.player.mouse_update((
                    x * control_game.screen_native_dims[0] / self.screen_sz[0],
                    y * control_game.screen_native_dims[1] / self.screen_sz[1]
                ))
                renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            self.screen_sz = (width, height)

            # update game state
            dt = st - self.last_st
            self.last_st = st

            if dt < (1.0 / 25.0):
                print(dt)
                control_game.all_entities.update(dt)

            surf = render.canvas().get_surface()
            surf.fill((0, 0, 0))

            self.primary_surf.fill((0, 0, 0, 0))
            control_game.all_entities.draw(self.primary_surf)

            pygame.transform.scale(
                self.primary_surf, self.screen_sz, surf
            )

            renpy.redraw(self, 1/60)
            return render


screen ctrl_game:
    add MentalControlGame():
        xpos 750
        yalign 0
        size (530, 530)

label start:
    show screen ctrl_game

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    show hitomi happy

    hitomi "Testing!"


    "We're not sure why, but one day, as we walked to school..."

    "...we woke up to find four of ourselves talking to each other."

    voc1 "Alright. Let's set things straight, here: who are you three?"

    "The first voice to speak up sounds refined and classy."

    "Voice #2" "Well, I do suppose that a round of introductions is in order." (who_color="#ffa126")

    "Voice #2" "My name is... well, I'm not really sure what my name is, but I do know that I am a man of lofty ambition." (who_color="#ffa126")

    "Voice #2" "Simply put: I wish to spread my flaming passions to everywhere I go. I want to bring the joy of light and heat to every--" (who_color="#ffa126")

    "He's quickly interrupted by a rough, growling voice."

    "Voice #3" "He means he's a fucking pyromaniac, and that his life's goal is to burn everything to the ground." (who_color="#663d20")

    voc2 "That- that is simply not true! I have many other interests other than burning! For example, I find the varying smells of gasoline to be quite--"

    "Voice #3" "Just shut up for now, okay?" (who_color="#663d20")

    "He sighs, and we can all feel the exasperation rolling off of him."

    "Voice #3" "Okay, look. I don't know who I am or what my name is either, but there is one thing I do know:" (who_color="#663d20")

    voc3 "I am a {i}survivor{/i}. I fought in the war. I've {i}seen{/i} shit out there."

    voc1 "--wait, what war? We're not even out of high scho--"

    voc3 "--like my buddy John getting sniped by one of them Krauts back in Bastogne, yeah? Horrifying stuff, really. Brains and blood, splattered all over the snow."

    "I don't bother trying to remind him that we're a student at a Japanese high school, and that World War II ended over 70 years ago."

    voc3 "--so yeah, I'm going to damn well make sure we're safe and secure while we operate here, deep behind enemy lines."

    voc2 "Oh, please. You, {i}defending{/i} us? I doubt you could defend us from anything more than stray cats and mice."

    voc3 "Yeah? Well, what do {i}you{/i} know about perimeter security then, Mister Pompous Asshole?"

    voc2 "I'd say I know more about the kinds of threats we'll be facing at this {i}high school{/i} than you ever will.
    For example, I know the best ways to discreetly dispose of a charred corpse, and how to sneak lighter fluid onto a school campus."

    "It's at this point that we all notice a fourth presence amidst us."

    voc3 "Hey, who's there?! You'd better fucking show yourself, or I'll-- I'll fucking put a bullet between your eyes!"

    voc2 "Please do remember that we are {i}disembodied voices{/i}. How do you possibly think you're going to accomplish that?"

    voc2 "Though I, myself, am rather curious about the newcomer. Why don't you show yourself?"

    pause 1

    "Voice #4" "...fine. Hi." (who_color="#6800b7")

    pause 2.5

    "There's nothing but silence for a few moments, while we wait for the newcomer to say more."

    pause 2.5

    voc3 "...Well? Is that it? Speak {i}up{/i}, for Christ's sake!"

    pause 1

    voc4 "I'm an artist. All I want to do is make artwork."

    voc4 "Is that enough?"

    voc3 "Fine. Just stay out of my fucking way, and we won't have problems. Capiche?"

    voc2 "I must agree. So long as you do not disturb my mission, I see no problem with letting you pursue your artwork."

    voc1 "He does bring up a good point, though. We're four minds inhabiting one body. How are we supposed to share?"

    voc2 "Well, I can't be certain with regards to everyone else, but: I {i}will{/i} carry out my tasks, even if I must seize control by force."

    return
