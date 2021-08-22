import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired from ship"""
    def __init__(self,ai_setting,screen,ship):
        super().__init__()
        self.screen = screen 
    
        # Create a bullet at rect(0,0) and then set correct position
        self.rect = pygame.Rect(0,0, ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store bullets position as decimal
        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """Move bullet up the screen"""
        #Update decimal position of bullet
        self.y -= self.speed_factor
        #Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen,self.color,self.rect)
