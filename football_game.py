import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from attacker import Attacker
from defender import Defender
from ball import Ball
import game_functions as gf

def run_game():
    # Initialize game and create  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Football game")

    # Make an attacker.
    attacker = Attacker(ai_settings, screen)

    # Make the initial ball
    initial_ball = Ball(ai_settings, screen, attacker)

    # Make a group of balls and a group of defender.
    balls = Group()
    defenders = Group()

    # Create the defense.
    gf.create_defense(ai_settings, screen, attacker, defenders)
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, attacker,
                initial_ball, balls)
        attacker.update()
        initial_ball.initial_update_ball(attacker)
        gf.update_balls(ai_settings, balls)
        gf.update_defenders(ai_settings, defenders)
        gf.update_screen(ai_settings, screen, attacker, defenders,
                initial_ball, balls)

run_game()
