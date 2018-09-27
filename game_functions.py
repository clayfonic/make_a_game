import sys
import pygame

from bullet import Bullet

# tossing some junk in here to test github

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


def update_screen(game_settings, screen, ship, alien, bullets):
    """update screen images and flip to a new screen"""

    # redraw the screen with each pass through the loop
    screen.fill(game_settings.bg_color)

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # draw the ship
    ship.blitme()

    # draw the alien
    alien.blitme()

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