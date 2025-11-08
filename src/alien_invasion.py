import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    #initialize pygame and create a screen object
    pygame.init()
    ai_settings = Settings()

    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    #make a ship
    ship = Ship(ai_settings,screen)

    # Create the alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    # light gray background
    bgcolor = (230, 230, 230)  

    
    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ship, screen, ai_settings, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()