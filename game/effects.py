import math
## effects for use with control game entities
# add these functions to any entity's update_hooks list.

class FadeEffect:
    def __init__(self, sprite, fade_time, start_alpha, end_alpha):
        self.start_alpha = start_alpha
        self.end_alpha = end_alpha
        self.fade_time = fade_time

        sprite.set_surface_alpha(start_alpha)

    def __call__(self, sprite, dt, acc):
        if sprite.surf_alpha is None:
            return False

        if (
            (self.start_alpha < self.end_alpha and sprite.surf_alpha < self.end_alpha)    # fade in
            or (self.start_alpha > self.end_alpha and sprite.surf_alpha > self.end_alpha) # fade out
        ):
            sprite.set_surface_alpha(
                sprite.surf_alpha
                + int((float(self.end_alpha) - float(self.start_alpha)) * dt / float(self.fade_time))
            )
            return True
        else:
            sprite.set_surface_alpha(self.end_alpha)
            return False

class BlinkEffect:
    def __init__(self, sprite, time, blink_alpha):
        self.blink_alpha = blink_alpha
        self.time = time
        self.elapsed_time = 0

        sprite.set_surface_alpha(255)

    def __call__(self, sprite, dt, acc):
        if sprite.surf_alpha is None:
            return False

        self.elapsed_time += dt

        if self.elapsed_time % 0.200 < 0.100:
            sprite.set_surface_alpha(self.blink_alpha)
        else:
            sprite.set_surface_alpha(255)

        if self.elapsed_time > self.time:
            sprite.set_surface_alpha(255)
            return False

        return True


class PushbackEffect:
    def __init__(self, sprite, force_src, push_time, push_speed):
        self.src = force_src
        self.sprite = sprite
        self.time = push_time
        self.speed = push_speed

        self.elapsed_time = 0

    def __call__(self, sprite, dt, acc):
        self.elapsed_time += dt

        if self.elapsed_time > self.time:
            sprite.vel = [0, 0]
            return False

        dsp_x = float(self.sprite.pos[0] - self.src.pos[0])
        dsp_y = float(self.sprite.pos[1] - self.src.pos[1])
        dist = math.sqrt(dsp_x ** 2 + dsp_y**2)

        sprite.vel[0] = dsp_x * self.speed / dist
        sprite.vel[1] = dsp_y * self.speed / dist

        return True
