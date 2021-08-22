from pygame import Color


class Setting():
    """Allows customization of game setting for the ship game """

    def __init__(self):
        #Window settings
        self.height = 800
        self.width = 600
        self.bg_color = (200,200,255)
        #Ship movement settings
        self.ship_speed_factor = 2.5
        #Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = 250, 60, 60
        self.bullet_allowed = 2

