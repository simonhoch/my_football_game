import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from attacker import Attacker
from ball import Ball
import game_functions as gf

def run_game():
    # Initialize game and create  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Foot ball game")

    # Make an attacker.
    attacker = Attacker(ai_settings, screen)

    # Make a group to store balls in.
    balls = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, attacker, balls)
        attacker.update()
        gf.update_balls(ai_settings, balls)
        gf.update_screen(ai_settings, screen, attacker, balls)

run_game()
