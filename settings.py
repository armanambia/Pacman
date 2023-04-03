class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.init_system()
        self.init_speeds()
        self.init_traits()
        self.init_points()
    

    def init_system(self):
        self.screen_width = 800 # 46 x 13 + 2 + 200
        self.screen_height = 666 # 51 x 13 + 3
        self.bg_color = (0, 0, 0)
        self.game_active = False
        self.hs_active = False
    
    def init_speeds(self):
        self.pac_speed = 1
        
    def init_traits(self):
        self.pac_start_x = 300
        self.pac_start_y = 500
        self.pac_size = 27
        self.bar_size = 15
        self.frt_size = 9
        self.shld_size = 5
        self.shld_off_x = 5
        self.shld_off_y = 5

    def init_points(self):
        self.fruit_points = 1
