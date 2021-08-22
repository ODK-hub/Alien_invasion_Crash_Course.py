#Importing packages to run code
import pygame
#Importing setting customization
from settings1 import Setting
#Importing ship attributes
from ship1 import Ship
#Importing ship functions 
import gamefunction1 as gf
#Importing function that stores bullets in special group list
from pygame.sprite import Group
#Importing alien enemies
from alien import Alien
def run_code():
    """Function to run game"""
    pygame.display.init()
    #Providing variables to classes from imported modules 
    ai_setting = Setting()
    #Creates window screen
    screen = pygame.display.set_mode((ai_setting.width,ai_setting.height))
    #Sets screen color
    open = True
    ship = Ship(ai_setting, screen)
    #Make a group to store bullets
    bullets = Group()
    alien_group = Group()
    gf.create_fleet(ai_setting, screen, alien_group)
    #Create movement
    open = True
    while open:
            gf.check_events(ai_setting, screen, ship, bullets)
            ship.update()
            bullets.update()
            gf.update_screen(ai_setting, screen, ship, bullets, alien_group)
            #Deleting bullets when gone off screen
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
                    

            pygame.display.update() 

run_code()
