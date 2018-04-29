# Positions for VN characters
define left = Transform(ypos=30, xpos=-80, xzoom=-1)
define right = Transform(ypos=30, xpos=300)
define center = Transform(ypos=30, xpos=80)
define flip = Transform(xzoom=-1)

define closeup = Transform(zoom=1.1)

define scene_bg = Transform(xpos=0, ypos=0, size=(750, 720))
define shooter_bg = Transform(xpos=750, ypos=540, size=(530, 180))

image controlgame_textbox_bg = "controlgame_textbox_bg.png"

init python:
    #config.developer = False
    if config.developer:
        config.log = './renpy.log'
    config.layers = ['game_bg', 'master', 'transient', 'screens', 'overlay']
    # config.rollback_enabled = False
    config.keymap['developer'] = ['shift_F']
    config.keymap['screenshot'] = ['shift_S']

    import pygame
    import control_game
    import entities
    import effects
    import game_data
    import tiles

    is_morning_diversion = False
    is_afternoon_diversion = False
    is_day2_diversion = False

    current_location = None  # used for marking where the MC is at the end of a diversion
    current_time = None

    diverting_from = None

    calm_diversion_points = 0
    pyro_diversion_points = 0
    artist_diversion_points = 0
    survivor_diversion_points = 0

    control_panel_pos = [game_data.tile_size*15, game_data.tile_size*15.5]

    voice_in_control = 'calm'

    route_choice = None

    def set_voice_pos(voice_id, pos):
        v = game.voice_by_id(voice_id)
        v.pos = pos

    def voice_id_to_instance(voice_id):
        return game.voice_by_id(voice_id)

    def set_voice_target(voice_id, tgt):
        v = game.voice_by_id(voice_id)
        v.target = game.voice_by_id(tgt)

    def set_voice_visible(voice_id, visible):
        v = game.voice_by_id(voice_id)
        if visible:
            v.set_surface_alpha(None)
        else:
            v.set_surface_alpha(0)

    def set_screen_center(center=None):
        game.set_screen_center(center)

    def reset_to_default_spawns():
        set_voice_pos('player', game.player.default_spawn_point)
        set_voice_pos('pyro', game.pyro.default_spawn_point)
        set_voice_pos('survivor', game.survivor.default_spawn_point)
        set_voice_pos('artist', game.artist.default_spawn_point)

    def set_control(voice_id):
        global voice_in_control

        voice_in_control = voice_id

        game.player.set_surface_alpha(0)
        game.pyro.set_surface_alpha(0)
        game.survivor.set_surface_alpha(0)
        game.artist.set_surface_alpha(0)

        set_voice_pos(voice_id, control_panel_pos)
        set_screen_center(control_panel_pos)

        if voice_id == 'calm':
            game.player.vel = [0, 0]
            game.player.set_surface_alpha(None)
        else:
            v = game.voice_by_id(voice_id)

            v.vel = [0, 0]
            v.set_surface_alpha(None)
            v.rot = 0
            v.target = None

    def set_clickfoward_status(allowed):
        game.allow_clickfwd = allowed

    def set_player_weapon_controllable(status):
        game.player.weapon.controllable = status

    def set_player_movement_allowed(status):
        game.player.movement_allowed = status

    def set_combat_status(status):
        game.combat_in_progress = status

    def set_ai_active(status):
        game.ai_active = status

    def start_combat():
        renpy.choice_for_skipping()
        config.skipping = False

        renpy.block_rollback()

        set_screen_center()

        game.combat_in_progress = True
        game.ai_active = True
        game.player.movement_allowed = True
        game.player.weapon.controllable = True
        game.allow_clickfwd = False

        for voice in game.all_voices.sprites():
            if not voice.alive():
                voice.pos = list(voice.default_spawn_point)

            if isinstance(voice, entities.AIVoice) and voice.target is None:
                possible_targets = [
                    game.player,
                    game.pyro,
                    game.survivor,
                    game.artist
                ]

                possible_targets.remove(voice)
                voice.target = renpy.random.choice(possible_targets)

            voice.set_health(voice.max_health)
            set_voice_visible(voice.id, True)

    def end_combat():
        game.combat_in_progress = False
        game.ai_active = False
        game.player.weapon.controllable = False
        game.player.movement_allowed = False
        game.allow_clickfwd = True

        return game.get_winning_voice()

    config.after_load_callbacks.append(control_game.repair_weapon_references)

    def complete_fadeout():
        renpy.scene()
        renpy.show('black')
        renpy.hide_screen('ctrl_game')
        renpy.with_statement(dissolve)

    def add_diversion_points(voice_id, n):
        global calm_diversion_points, survivor_diversion_points, pyro_diversion_points, artist_diversion_points

        if voice_id == "calm" or voice_id == "player":
            calm_diversion_points += n
        elif voice_id == "survivor" or voice_id == "surv":
            survivor_diversion_points += n
        elif voice_id == "pyro":
            pyro_diversion_points += n
        elif voice_id == "artist":
            artist_diversion_points += n

    def call_diversion(voice_id, divert_from):
        global calm_diversion_points, survivor_diversion_points, pyro_diversion_points, artist_diversion_points, diverting_from

        diverting_from = divert_from

        if voice_id == "survivor" or voice_id == "surv":
            return renpy.call('survivor_diversion_'+str(survivor_diversion_points))
        elif voice_id == "pyro":
            return renpy.call('pyro_diversion_'+str(pyro_diversion_points))
        elif voice_id == "artist":
            return renpy.call('artist_diversion_'+str(artist_diversion_points))
        elif voice_id == "calm" or voice_id == "player":
            return renpy.call("calm_"+divert_from)

    def get_controlling_voice_name(i_for_calm=True): # if I_for_calm is true, then we return 'I' when Calm is in control; otherwise return 'Calm'
        global voice_in_control

        if voice_in_control == 'player' or voice_in_control == 'calm':
            if i_for_calm:
                return 'I'
            else:
                return 'Calm'
        elif voice_in_control == 'survivor' or voice_in_control == 'surv':
            return 'Survivor'
        elif voice_in_control == 'pyro':
            return 'Pyro'
        elif voice_in_control == 'artist':
            return 'Artist'

    def say_current_mc(t, *args, **kwargs):
        global voice_in_control, mc, surv_mc, pyro_mc, artist_mc

        if voice_in_control == 'player' or voice_in_control == 'calm':
            return renpy.say(mc, t, *args, **kwargs)
        elif voice_in_control == 'survivor' or voice_in_control == 'surv':
            return renpy.say(surv_mc, t, *args, **kwargs)
        elif voice_in_control == 'pyro':
            return renpy.say(pyro_mc, t, *args, **kwargs)
        elif voice_in_control == 'artist':
            return renpy.say(artist_mc, t, *args, **kwargs)

    def say_current_voice(t, *args, **kwargs):
        global voice_in_control, calm, pyro, surv, artist

        if voice_in_control == 'player' or voice_in_control == 'calm':
            return renpy.say(calm, t, *args, **kwargs)
        elif voice_in_control == 'survivor' or voice_in_control == 'surv':
            return renpy.say(surv, t, *args, **kwargs)
        elif voice_in_control == 'pyro':
            return renpy.say(pyro, t, *args, **kwargs)
        elif voice_in_control == 'artist':
            return renpy.say(artist, t, *args, **kwargs)

    def voice_locked_in():
        global calm_diversion_points, survivor_diversion_points, pyro_diversion_points, artist_diversion_points

        if calm_diversion_points >= 4:
            return "calm"
        elif survivor_diversion_points >= 4:
            return "survivor"
        elif pyro_diversion_points >= 4:
            return "pyro"
        elif artist_diversion_points >= 4:
            return "artist"
        else:
            return None

    class ClickForwardAction(Action):
        def __call__(self):
            global calm_pos, pyro_pos, artist_pos, survivor_pos, pyro_target, artist_target, survivor_target

            # HACK: make sure each Voice's position and target is saved on each interaction
            calm_pos = game.player.pos
            pyro_pos = game.pyro.pos
            survivor_pos = game.survivor.pos
            artist_pos = game.artist.pos

            if game.pyro.target is not None:
                pyro_target = game.pyro.target.id

            if game.artist.target is not None:
                artist_target = game.artist.target.id

            if game.survivor.target is not None:
                survivor_target = game.survivor.target.id

            if game.allow_clickfwd:
                return True
            else:
                return None

screen ctrl_game:
    zorder 0
    tag game_screen

    key "S" action NullAction()
    key "D" action NullAction()
    key "dismiss" action ClickForwardAction()

    add control_game.ControlGameDisplay() id "game_display":
        xpos 750
        yalign 0
        size (530, 540)

label start:
    show screen ctrl_game

    scene walk_to_school day at scene_bg
    show controlgame_textbox_bg at shooter_bg onlayer game_bg

    python:
        game = control_game.MentalControlGame()

        game.allow_clickfwd = True

        game.player.movement_allowed = True
        player_movement_allowed = True

        set_control('calm')
        end_combat()

        game.player.set_surface_alpha(0)
        game.pyro.set_surface_alpha(0)
        game.survivor.set_surface_alpha(0)
        game.artist.set_surface_alpha(0)

        set_screen_center([750, 750])

        set_voice_pos('calm', control_panel_pos)
        set_voice_pos('pyro', [game_data.tile_size*18, game_data.tile_size*12])
        set_voice_pos('survivor', [game_data.tile_size*11, game_data.tile_size*13])
        set_voice_pos('artist', [game_data.tile_size*15, game_data.tile_size*10])

        game.pyro.turn_to(game.player.pos)
        game.survivor.turn_to(game.player.pos)
        game.artist.turn_to(game.player.pos)

    "I am the voice inside of [mc.name]'s head."

    "I've been here for as long as I can remember, guiding him through life as best as I can."

    "And thanks to me, [mc.name] has had a pretty calm, uneventful life so far, which is all I really want for him."

    "Unfortunately..."

    "I'm not sure why, but one day, as [mc.name] and I were walking to school..."

    "...I suddenly found two other voices sharing [mc.name]'s head with me."

    $ game.player.add_effect(effects.FadeEffect(game.player, .75, 0, 255))

    calm "Alright. Let's set things straight, here: who are you two?"

    "The first voice to speak up sounds refined and classy."

    $ game.pyro.add_effect(effects.FadeEffect(game.pyro, .75, 0, 255))

    "Voice #2" "Well, I do suppose that a round of introductions is in order." (who_color="#ffa126")

    "Voice #2" "My name is... well, I'm not really sure what my name is, but I do know that I am a man of lofty ambition." (who_color="#ffa126")

    "Voice #2" "Simply put: I wish to spread my flaming passions to everywhere I go. I want to bring the joy of light and heat to every--" (who_color="#ffa126")

    "He's quickly interrupted by a rough, growling voice."

    $ game.survivor.add_effect(effects.FadeEffect(game.survivor, .75, 0, 255))

    "Voice #3" "He means he's a fucking pyromaniac, and that his life's goal is to burn everything to the ground." (who_color="#3d660e")

    $ game.pyro.turn_to(game.survivor.pos)

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

    $ game.survivor.turn_to(game.pyro.pos)

    surv "Yeah? Well, what do {i}you{/i} know about defense then, Mister Pompous Asshole?"

    pyro "I'd say I know more about the kinds of threats we'll be facing at this {i}high school{/i} than you ever will.
    For example, I know the best ways to discreetly dispose of a charred corpse, and how to sneak gasoline onto a school campus."

    "It's at this point that we all notice a fourth presence amidst us."

    surv "Hey, who's there?! You'd better fucking show yourself, or I'll-- I'll fucking put a bullet between your eyes!"

    pyro "Please do remember that we are {i}mental constructs{/i}. How do you possibly think you're going to accomplish that?"

    pyro "Though I, myself, am rather curious about the newcomer. Why don't you show yourself?"

    $ set_clickfoward_status(False)

    pause 1

    $ game.artist.add_effect(effects.FadeEffect(game.artist, .75, 0, 255))
    $ set_clickfoward_status(True)

    "Voice #4" "...fine. Hi." (who_color="#6800b7")

    $ game.survivor.turn_to(game.artist.pos)
    $ game.pyro.turn_to(game.artist.pos)

    $ set_clickfoward_status(False)
    pause 2.5
    $ set_clickfoward_status(True)

    "There's nothing but silence for a few moments, while we wait for the newcomer to say more."

    $ set_clickfoward_status(False)
    pause 2.5
    $ set_clickfoward_status(True)

    surv "...Well? Is that it? Speak {i}up{/i}, for Christ's sake!"

    $ set_clickfoward_status(False)
    pause 1
    $ set_clickfoward_status(True)

    artist "I'm an artist. All I want to do is make artwork."

    artist "Is that enough?"

    surv "Fine. Just stay out of my fucking way, and we won't have problems. Capiche?"

    pyro "I must agree. So long as you do not disturb my mission, I see no problem with letting you pursue your artwork."

    calm "He does bring up a good point, though. We're four minds inhabiting one body. We can't share."

    $ game.pyro.turn_to(game.player.pos)

    pyro "Well, I can't be certain with regards to everyone else, but: I {i}will{/i} carry out my tasks, and if I have to fight you three somehow to do so, then I will not hesitate."

    $ game.survivor.turn_to(game.pyro.pos)

    surv "See, we're going to have a {i}problem{/i} with that, since your whole 'burning everything in sight' schtick is going to get us all killed by the enemy, here."

    artist "Both of your goals will prevent me from making art. Therefore, I will have to stop you."

    "Personally, I wouldn't want either of those two to have control at all; I just want [mc.name] to have a nice, calm, peaceful life."

    calm "So there's no way for any of us to cooperate then?"

    $ game.survivor.turn_to(game.player.pos)

    surv "Negative."

    pyro "I'm afraid not."

    artist "No."

    calm "Well, I'm sorry, but I'm afraid you all won't be able to do anything without my say-so. I still have control, and I don't think there's any way for you to take it from me."

    surv "Hrmph. Well, if that's how you want to play it... fine. But I will find a way, I promise you that."

    $ game.survivor.add_effect(effects.FadeEffect(game.survivor, .75, 255, 0))

    pyro "I suggest you watch your back from here on out. I {i}will{/i} see my mission through."

    $ game.pyro.add_effect(effects.FadeEffect(game.pyro, .75, 255, 0))

    artist "..."

    $ set_clickfoward_status(False)
    pause 1
    $ set_clickfoward_status(True)

    $ game.artist.add_effect(effects.FadeEffect(game.artist, .75, 255, 0))

    "And with that, they vanish into the recesses of [mc.name]'s mind."

    jump day0_hitomi
