class Settings():
    """ a class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """ initiailze the game's settings"""
        # screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10000
        
        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
