# Positions for VN characters
define left = Transform(ypos=30, xpos=-80, xzoom=-1)
define right = Transform(ypos=30, xpos=300)
define center = Transform(ypos=30, xpos=80)
define flip = Transform(xzoom=-1)

define scene_bg = Transform(xpos=0, ypos=0, size=(750, 720))
define shooter_bg = Transform(xpos=750, ypos=540, size=(530, 180))

image controlgame_textbox_bg = "controlgame_textbox_bg.png"

init python:
    #config.developer = False
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

    diverting_from = None

    calm_diversion_points = 0
    pyro_diversion_points = 0
    artist_diversion_points = 0
    survivor_diversion_points = 0

    control_panel_pos = [game_data.tile_size*15, game_data.tile_size*15.5]

    voice_in_control = 'calm'

    route_choice = None

    calm_visible = True
    pyro_visible = False
    artist_visible = False
    survivor_visible = False

    calm_pos = [0, 0]
    pyro_pos = [0, 0]
    artist_pos = [0, 0]
    survivor_pos = [0, 0]

    pyro_target = None
    survivor_target = None
    artist_target = None

    saved_screen_center = None

    combat_in_progress = False
    player_movement_allowed = False
    player_weapon_controllable = False
    click_forward_enabled = False
    ai_active = False

    def set_voice_pos(voice_id, pos):
        if voice_id == 'calm' or voice_id == 'player':
            calm_pos = pos
            control_game.player.pos = pos
        elif voice_id == 'pyro':
            pyro_pos = pos
            control_game.pyro.pos = pos
        elif voice_id == 'survivor' or voice_id == 'surv':
            survivor_pos = pos
            control_game.survivor.pos = pos
        elif voice_id == 'artist':
            artist_pos = pos
            control_game.artist.pos = pos

    def voice_id_to_instance(voice_id):
        if voice_id == 'calm' or voice_id == 'player':
            return control_game.player
        elif voice_id == 'pyro':
            return control_game.pyro
        elif voice_id == 'survivor' or voice_id == 'surv':
            return control_game.survivor
        elif voice_id == 'artist':
            return control_game.artist

    def set_voice_target(voice_id, tgt):
        if voice_id == 'pyro':
            pyro_target = tgt
            control_game.pyro.target = voice_id_to_instance(tgt)
        elif voice_id == 'survivor' or voice_id == 'surv':
            survivor_target = tgt
            control_game.survivor.target = voice_id_to_instance(tgt)
        elif voice_id == 'artist':
            artist_target = tgt
            control_game.artist.target = voice_id_to_instance(tgt)

    def set_voice_visible(voice_id, visible):
        if voice_id == 'calm' or voice_id == 'player':
            calm_visible = visible
            if visible:
                control_game.player.set_surface_alpha(None)
            else:
                control_game.player.set_surface_alpha(0)
        elif voice_id == 'pyro':
            pyro_visible = visible
            if visible:
                control_game.pyro.set_surface_alpha(None)
            else:
                control_game.pyro.set_surface_alpha(0)
        elif voice_id == 'survivor' or voice_id == 'surv':
            survivor_visible = visible
            if visible:
                control_game.survivor.set_surface_alpha(None)
            else:
                control_game.survivor.set_surface_alpha(0)
        elif voice_id == 'artist':
            artist_visible = visible
            if visible:
                control_game.artist.set_surface_alpha(None)
            else:
                control_game.artist.set_surface_alpha(0)

    def set_screen_center(center=None):
        global saved_screen_center

        control_game.set_screen_center(center)
        saved_screen_center = center

    def reset_to_default_spawns():
        set_voice_pos('player', control_game.player.default_spawn_point)
        set_voice_pos('pyro', control_game.pyro.default_spawn_point)
        set_voice_pos('survivor', control_game.survivor.default_spawn_point)
        set_voice_pos('artist', control_game.artist.default_spawn_point)

    def set_control(v):
        global calm_visible, pyro_visible, artist_visible, survivor_visible, voice_in_control

        voice_in_control = v

        calm_visible = False
        pyro_visible = False
        artist_visible = False
        survivor_visible = False

        control_game.player.set_surface_alpha(0)
        control_game.pyro.set_surface_alpha(0)
        control_game.survivor.set_surface_alpha(0)
        control_game.artist.set_surface_alpha(0)

        set_voice_pos(v, control_panel_pos)
        set_screen_center(control_panel_pos)

        if v == 'calm':
            calm_visible = True
            control_game.player.vel = [0, 0]
            control_game.player.set_surface_alpha(None)
        elif v == 'pyro':
            pyro_visible = True
            control_game.pyro.vel = [0, 0]
            control_game.pyro.set_surface_alpha(None)
            control_game.pyro.rot = 0

            control_game.pyro.target = None
        elif v == 'survivor' or v == 'surv':
            survivor_visible = True
            control_game.survivor.vel = [0, 0]
            control_game.survivor.set_surface_alpha(None)
            control_game.survivor.rot = 0

            control_game.survivor.target = None
        elif v == 'artist':
            artist_visible = True
            control_game.artist.vel = [0, 0]
            control_game.artist.set_surface_alpha(None)
            control_game.artist.rot = 0

            control_game.artist.target = None

    def set_clickfoward_status(allowed):
        global click_forward_enabled

        click_forward_enabled = allowed
        control_game.allow_clickfwd = allowed

    def set_player_weapon_controllable(status):
        global player_weapon_controllable

        player_weapon_controllable = status
        control_game.player.weapon.controllable = status

    def set_player_movement_allowed(status):
        global player_movement_allowed

        player_movement_allowed = status
        control_game.player.movement_allowed = status

    def set_combat_status(status):
        global combat_in_progress

        combat_in_progress = status
        game_data.combat_in_progress = status

    def set_ai_active(status):
        global ai_active

        ai_active = status
        game_data.ai_active = status

    def start_combat():
        global combat_in_progress, player_movement_allowed, player_weapon_controllable, click_forward_enabled, ai_active

        renpy.choice_for_skipping()
        config.skipping = False

        renpy.block_rollback()

        set_screen_center()

        combat_in_progress = True
        player_movement_allowed = True
        player_weapon_controllable = True
        ai_active = True
        click_forward_enabled = False

        game_data.combat_in_progress = True
        game_data.ai_active = True
        control_game.player.movement_allowed = True
        control_game.player.weapon.controllable = True
        control_game.allow_clickfwd = False

        for voice in entities.all_voices.sprites():
            if not voice.alive():
                voice.pos = list(voice.default_spawn_point)

            voice.set_health(voice.max_health)
            set_voice_visible(voice.id, True)

    def end_combat():
        global combat_in_progress, player_movement_allowed, player_weapon_controllable, click_forward_enabled, ai_active

        game_data.combat_in_progress = False
        game_data.ai_active = False
        control_game.player.weapon.controllable = False
        control_game.player.movement_allowed = False
        control_game.allow_clickfwd = True

        combat_in_progress = False
        player_movement_allowed = False
        player_weapon_controllable = False
        ai_active = False
        click_forward_enabled = True

        return control_game.get_winning_voice()

    def on_load_callback():
        global combat_in_progress, player_movement_allowed, player_weapon_controllable, click_forward_enabled, saved_screen_center, voice_in_control, ai_active
        global calm_pos, pyro_pos, artist_pos, survivor_pos, pyro_target, artist_target, survivor_target
        global calm_visible, pyro_visible, artist_visible, survivor_visible

        control_game.init()

        game_data.screen_center = saved_screen_center
        control_game.on_load(voice_in_control)
        set_control(voice_in_control)

        game_data.combat_in_progress = combat_in_progress
        game_data.ai_active = ai_active
        control_game.player.movement_allowed = player_movement_allowed
        control_game.player.weapon.controllable = player_weapon_controllable
        control_game.allow_clickfwd = click_forward_enabled

        control_game.player.pos = calm_pos
        control_game.pyro.pos = pyro_pos
        control_game.survivor.pos = survivor_pos
        control_game.artist.pos = artist_pos

        set_voice_target('pyro', pyro_target)
        set_voice_target('survivor', survivor_target)
        set_voice_target('artist', artist_target)

        set_voice_visible('player', calm_visible)
        set_voice_visible('pyro', pyro_visible)
        set_voice_visible('survivor', survivor_visible)
        set_voice_visible('artist', artist_visible)

    config.after_load_callbacks.append(on_load_callback)

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

    class ClickForwardAction(Action):
        def __call__(self):
            global calm_pos, pyro_pos, artist_pos, survivor_pos, pyro_target, artist_target, survivor_target

            # HACK: make sure each Voice's position and target is saved on each interaction
            calm_pos = control_game.player.pos
            pyro_pos = control_game.pyro.pos
            survivor_pos = control_game.survivor.pos
            artist_pos = control_game.artist.pos

            if control_game.pyro.target is not None:
                pyro_target = control_game.pyro.target.id

            if control_game.artist.target is not None:
                artist_target = control_game.artist.target.id

            if control_game.survivor.target is not None:
                survivor_target = control_game.survivor.target.id

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

    scene walk_to_school day at scene_bg
    show controlgame_textbox_bg at shooter_bg onlayer game_bg

    python:
        control_game.init()
        tiles.init()

        set_control('calm')
        end_combat()

        control_game.player.set_surface_alpha(0)
        control_game.pyro.set_surface_alpha(0)
        control_game.survivor.set_surface_alpha(0)
        control_game.artist.set_surface_alpha(0)

        set_screen_center([750, 750])

        set_voice_pos('calm', control_panel_pos)
        set_voice_pos('pyro', [game_data.tile_size*18, game_data.tile_size*12])
        set_voice_pos('survivor', [game_data.tile_size*11, game_data.tile_size*13])
        set_voice_pos('artist', [game_data.tile_size*15, game_data.tile_size*10])

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

    $ set_clickfoward_status(False)

    pause 1

    $ control_game.artist.add_effect(effects.FadeEffect(control_game.artist, .75, 0, 255))
    $ set_clickfoward_status(True)

    "Voice #4" "...fine. Hi." (who_color="#6800b7")

    $ control_game.survivor.turn_to(control_game.artist.pos)
    $ control_game.pyro.turn_to(control_game.artist.pos)

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

    $ set_clickfoward_status(False)
    pause 1
    $ set_clickfoward_status(True)

    $ control_game.artist.add_effect(effects.FadeEffect(control_game.artist, .75, 255, 0))

    "And with that, they vanish into the recesses of [mc.name]'s mind."

    jump day0_hitomi
