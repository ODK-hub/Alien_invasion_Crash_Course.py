import pygame
from pygame.sprite import Sprite


class Alien():
    def __init__(self,ai_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load(r"C:\Users\omidd\Downloads\Somealien (1).png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Starting alien at top-left
        self.rect.x = self.rect.left
        self.rect.y = self.rect.top
    def blitme(self):
        """Paste the picture of the alien onto the screen"""
        self.image = pygame.transform.smoothscale(self.image,(160,160))
        self.screen.blit(self.image, self.rect)