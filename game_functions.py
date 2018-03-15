import sys

import pygame

def check_keydown_events(event, ball):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ball.moving_right = True
    elif event.key == pygame.K_LEFT:
        ball.moving_left = True
    elif event.key == pygame.K_UP:
        ball.moving_up = True
    elif event.key == pygame.K_DOWN:
        ball.moving_down = True

def check_keyup_events(event, ball):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ball.moving_right = False
    elif event.key == pygame.K_LEFT:
        ball.moving_left = False
    elif event.key == pygame.K_UP:
        ball.moving_up = False
    elif event.key == pygame.K_DOWN:
        ball.moving_down = False

def check_events(ball):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ball)

def update_screen(ai_settings, screen, ball):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ball.blitme()

    # Make  the most recently drawn screen visible.
    pygame.display.flip()
