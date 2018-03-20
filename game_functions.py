import sys

import pygame

from ball import Ball

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
            check_keyup_events(event, attacker, initial_ball)

def update_screen(ai_settings, screen, attacker, initial_ball, balls):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all balls behind attacker and defenders.
    for ball in balls.sprites():
        ball.draw_ball()
    attacker.blitme()
    initial_ball.draw_ball()
    # Make  the most recently drawn screen visible.
    pygame.display.flip()

def update_balls(ai_settings, balls):
    """Update position of balls and get rid of old balls."""
    # Update ball positions.
    balls.update()

    # Get rid of bullets that have disappeared.
    for ball in balls.copy():
        if ball.rect.left >= ai_settings.screen_width:
            balls.remove(ball)
