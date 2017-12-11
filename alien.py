import pygame
import random
from enemy_bullet import Enemy_Bullet
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def add_enemy_bullets(self, ai_settings, screen, enemy_bullets):

        random_number = random.randint(0, 10)

        # Use random number to determine which alien fires
        if random_number % 3 == 0:
            if 10 >= ai_settings.enemy_bullet_limit > 0:
                enemy_bullets.add(Enemy_Bullet(ai_settings, screen, self))
                ai_settings.enemy_bullet_limit -= 1



    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self, ai_settings, screen, enemy_bullets, random_number):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.add_enemy_bullets(ai_settings, screen, enemy_bullets)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
