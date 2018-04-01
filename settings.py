class Settings():
    "A class to store all settings for Football game."

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (50, 205, 50)
        self.attacker_speed_factor = 1.5
        # Attacker settings.
        self.ball_speed_factor = 2
        self.balls_allowed = 1
        # Defender settings.
        self.defender_speed_factor = 1
        self.defense_move_speed = 10
        # defense_direction of 1 represent up : -1 represents down.
        self.defense_direction = 1
