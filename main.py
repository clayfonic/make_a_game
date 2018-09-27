import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # init pygame, settings, and screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("What are we even doing?")

    # make a ship
    ship = Ship(game_settings, screen)
    # make a group to store bullets in
    bullets = Group()
    # make an alien
    alien = Alien(game_settings, screen)

    # start the main loop for the game
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, alien, bullets)


run_game()
