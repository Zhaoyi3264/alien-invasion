class GameStats():
    """ track statistics for Alien Invasion"""
    
    def __init__(self, ai_settings):
        """ initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True
        
    def reset_stats(self):
        """ initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        
