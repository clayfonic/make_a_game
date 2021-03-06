import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, game_settings, screen, ship, bullets):
    """respond to key presses"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, ship):
    """respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(game_settings, screen, ship, bullets):
    """respond to key pressing and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(game_settings, screen, ship, aliens, bullets):
    """update screen images and flip to a new screen"""

    # redraw the screen with each pass through the loop
    screen.fill(game_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # draw the ship
    ship.blitme()
    aliens.draw(screen)

    # make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    """update position of bullets and get rid of old bullets"""
    # update bullet positions
    bullets.update()

    # get rid of bullets that have left the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(game_settings, screen, ship, bullets):
    """fire a bullet if limit not reached"""
    # create a new bullet and add it to the bullets group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(game_settings, alien_width):
    """determine number of aliens that fit in a row"""
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, ship_height, alien_height):
    """determine the number of rows of aliens that will fit on the screen"""
    available_space_y = (game_settings.screen_height - (3 * alien_height) -
                         ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    """create a full fleet of aliens"""
    # create an alien and find the number of aliens that can fit in a row
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height,
                                  alien.rect.height)

    # create the fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number,
                         row_number)


def check_fleet_edges(game_settings, aliens):
    """respond appropriately if any aliens reach an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """drop the entire fleet and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def update_aliens(game_settings, aliens):
    """check if the fleet is at an edge and then update the positions of all
    aliens in the fleet"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()
