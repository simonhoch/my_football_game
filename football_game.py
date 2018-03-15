import sys

import pygame

from settings import Settings
from ball import Ball
import game_functions as gf

def run_game():
    # Initialize game and create  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Foot ball game")

    # Make a ball.
    ball = Ball(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ball)
        ball.update()
        gf.update_screen(ai_settings, screen, ball)

run_game()
