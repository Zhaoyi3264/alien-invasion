import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # initialize pygaem, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create an instance to store game statistics
    stats = GameStats(ai_settings)
    
    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in
    bullets = Group()
    # make a group of aliens
    aliens = Group()
    
    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the game loop
    while True:
        
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
                    
run_game()
