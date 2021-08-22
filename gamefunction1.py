import pygame
from bullets import Bullet
from alien import Alien
def check_keydown_events(event,ai_setting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        #Create new bullets and add to bullets group as long as it's not over limit
        if len(bullets) < ai_setting.bullet_allowed:
            new_bullet = Bullet(ai_setting,screen,ship)
            bullets.add(new_bullet)
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_q:
            #Help quit the game by pressing q
            pygame.quit()
            exit()
def check_events(ai_setting, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        #Stores any keyboard or mouse inputs
        if event.type == pygame.QUIT:
            #Help quit the game by pressing the x mark at top right corner
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
def update_screen(ai_setting, screen, ship, bullets, alien_group):
    #Update screen
    screen.fill(ai_setting.bg_color)
    #Pasting the ship on the window
    ship.blitme()
    alien_group.draw(screen)
    #Drawing all bullets from ship at the same time including the ones stored
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Make sure that the ship is infront of the screen (can cause error if sprite elements are after flip)
    pygame.display.flip()

def create_fleet(ai_setting, screen, alien_group):
    #Enemy alien class
    allien = Alien(ai_setting, screen)
    allien_width = allien.rect.width
    #Printing horizontal correct number of aliens
    available_space_x = ai_setting.width - (2 * allien_width)
    number_aliens_x = int(available_space_x / (2 * allien_width))

    #Creating row
    for alien_number in range(number_aliens_x):
        allien = Alien(ai_setting, screen)
        allien.x = allien_width + 2 * allien_width * alien_number
        allien.rect.x = allien.x 
        alien_group.add(allien)
        