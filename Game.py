import pygame
import game_functions as gf
from button import Button
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import Game_Stats
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    pygame.display.set_caption('Alien Invasion')
    ai_settings=Settings()
    stats=Game_Stats(ai_settings)
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship=Ship(ai_settings,screen)
    scoreboard=Scoreboard(ai_settings,screen,stats,ship)
    play_button=Button(ai_settings,screen,'Play')
    aliens=Group()
    bullets=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets,play_button,stats,aliens,scoreboard)
        if stats.game_active:
            ship.updata()
            gf.updata_bullets(ai_settings,screen,ship,aliens,bullets,stats,scoreboard)
            gf.updata_aliens(ship,ai_settings,aliens,stats,bullets,screen,scoreboard)
        gf.updata_screen(ai_settings,screen,ship,bullets,aliens,play_button,stats,scoreboard)

run_game()