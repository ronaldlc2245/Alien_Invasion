from background import Background
import random

class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800

        # Set background image
        self.bg = Background('images/space_bg.jpg', [0, 0])
        self.bg_color = (255, 255, 255)
        
        # Ship settings.
        self.ship_limit = 1
            
        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 0
        self.bullets_allowed = 3

        # Alien bullet settings
        self.enemy_bullet_color = 255, 0, 0
        self.enemy_bullet_limit = 10

        # Alien settings.
        self.fleet_drop_speed = 15
            
        # How quickly the game speeds up.
        self.speedup_scale = 1.5

        # How quickly the alien point values increase.
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 2

        """
        Use random number generator to generate a number between 1 and 5
        settings will change randomly
        
        self.ship_speed_factor = random.randint(0, 6)
        self.bullet_speed_factor = random.randint(0,6)
        self.alien_speed_factor = random.randint(0, 6)
        
        """
        
        # Scoring.
        self.alien_points = 50
    
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
