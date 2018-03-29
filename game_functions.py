import sys

import pygame

from ball import Ball
from defender import Defender
from random import randint

def check_keydown_events(event, ai_settings, screen, attacker,
        initial_ball, balls):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        attacker.moving_right = True
    elif event.key == pygame.K_LEFT:
        attacker.moving_left = True
    elif event.key == pygame.K_UP:
        attacker.moving_up = True
    elif event.key == pygame.K_DOWN:
        attacker.moving_down = True
    elif event.key == pygame.K_SPACE:
        kick_ball(ai_settings, screen, attacker, balls)

def kick_ball(ai_settings, screen, attacker, balls):
    """Kick a ball if limit is not reached yet."""
    # Create a new ball and add it to the balls group.
    if len(balls) < ai_settings.balls_allowed:
        new_ball = Ball(ai_settings, screen, attacker)
        new_ball.draw_ball()
        balls.add(new_ball)

def check_keyup_events(event, attacker):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        attacker.moving_right = False
    elif event.key == pygame.K_LEFT:
        attacker.moving_left = False
    elif event.key == pygame.K_UP:
        attacker.moving_up = False
    elif event.key == pygame.K_DOWN:
        attacker.moving_down = False
    elif event.key == pygame.K_q:
        sys.exit()

def check_events (ai_settings, screen, attacker,
        initial_ball, balls):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, attacker,
                    initial_ball, balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, attacker)

def update_screen(ai_settings, screen, attacker, defenders, initial_ball, balls):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all balls behind attacker and defenders.
    for ball in balls.sprites():
        ball.draw_ball()
    attacker.blitme()
    initial_ball.draw_ball()
    defenders.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_balls(ai_settings, balls):
    """Update position of balls and get rid of old balls."""
    # Update ball positions.
    balls.update()

    # Get rid of balls that have disappeared.
    for ball in balls.copy():
        if ball.rect.left >= ai_settings.screen_width:
            balls.remove(ball)

def get_number_defenders_y(ai_settings, defender_height):
    """Determine the number of defender that fit in a row."""
    random_defender = randint(2,4)
    available_space_y = ai_settings.screen_height - 2 * defender_height
    number_defenders_y = int(available_space_y /
            (random_defender * defender_height))
    return number_defenders_y

def get_number_rows(ai_settings, defender_width):
    """Determine the number of rows of the defense."""
    #random_rows = randint(3,6)
    #available_space_x = (ai_settings.screen_width -
            #(random_rows * defender_width))
    number_rows = 3 #int(available_space_x / (3 * defender_width))
    return number_rows

def create_defender(ai_settings, screen, defenders, defender_number,
        row_number):
    """Create a defender and place it in the row."""
    defender = Defender(ai_settings, screen)
    defender_height = defender.rect.height
    defender.y  = (defender_height + 3 * defender_height *
        defender_number)
    defender.rect.y = defender.y
    defender.rect.x = ai_settings.screen_width - (4 * defender.rect.width *
            row_number)
    defenders.add(defender)

def create_defense(ai_settings, screen, attacker, defenders):
    """Create the defense."""
    # Create a defender and find the number of defenders in a row.
    defender = Defender(ai_settings, screen)
    number_defenders_y = get_number_defenders_y(ai_settings, defender.
            rect.height)
    number_rows = get_number_rows(ai_settings, defender.rect.width)

    # Create the first row of defenders.
    for row_number in range(number_rows):
        for defender_number in range(number_defenders_y):
            create_defender(ai_settings, screen, defenders,
                    defender_number, row_number)
