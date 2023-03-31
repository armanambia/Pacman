class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 598 # 46 x 13
        self.screen_height = 663 # 51 x 13
        self.bg_color = (0, 0, 0)

        self.aliens_shoot_every = 120    # about every 2 seconds at 60 fps
        self.alien_points = 50

# # TODO: set a ship_limit of 3
        self.ship_limit = 3         # total ships allowed in game before game over

        self.fleet_drop_speed = 1
        self.fleet_direction = 1     # change to a Vector(1, 0) move to the right, and ...
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.alien_speed = 1
        self.ship_speed = 3
        self.laser_speed = 3

    def increase_speed(self):
        scale = self.speedup_scale
        self.ship_speed *= scale
        self.laser_speed *= scale
