import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #initialize pygame and create a screen object
    pygame.init()
    ai_settings = Settings()

    # Make a group to store bullets in.
    bullets = Group()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #make a ship
    ship = Ship(ai_settings,screen)
    # light gray background
    bgcolor = (230, 230, 230)  

    
    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ship, screen, ai_settings, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()