## effects for use with control game entities
# add these functions to any entity's update_hooks list.

class FadeEffect:
    def __init__(self, sprite, fade_time, start_alpha, end_alpha):
        self.start_alpha = start_alpha
        self.end_alpha = end_alpha
        self.fade_time = fade_time

        sprite.set_surface_alpha(start_alpha)

    def __call__(self, sprite, dt, acc):
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
