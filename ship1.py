import pygame

class Ship():
    def __init__(self,ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load(r"C:\Users\omidd\Downloads\Spaceshipbit1 (1).png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Starting ship at bottom center screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Store decimal value for for the ship's center
        self.center = float(self.rect.centerx)
        self.centere = float(self.rect.centery)
        #Movement initalization
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.moving_up == True and self.rect.top > 0:
            self.centere -= self.ai_setting.ship_speed_factor
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.centere += self.ai_setting.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.centery = self.centere

            