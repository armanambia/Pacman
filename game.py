from random import randint
import pygame as pg
from maze import Maze
from pacman import Pacman
from ghosts import Ghosts
from fruit import Fruit
from settings import Settings
from sound import Sound
from scoreboard import Scoreboard
from vector import Vector
from launch_screen import Launch
from button import Button
from hs_screen import HighScore
import sys

import shelve

from pygame.sprite import Sprite, Group

# only run this on first launch, comment out line 36 if running the below script

# d = shelve.open('score.txt')  
# d['score'] = 0            
# d['hs_1_score'] = 0           
# d['hs_1_level'] = 1      
# d['hs_2_score'] = 0           
# d['hs_2_level'] = 1     
# d['hs_3_score'] = 0           
# d['hs_3_level'] = 1             
# d.close()

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.disk = shelve.open('score.txt')
        
        size = self.settings.screen_width, self.settings.screen_height  # tuple
        self.screen = pg.display.set_mode(size=size)
        self.maze = Maze(game=self)
        self.ghosts = Ghosts(game=self)
        self.pacman = Pacman(game=self)
        self.scoreboard = Scoreboard(game=self)
        self.play_button = Button( "Play", game=self, offsety=200)
        self.hs_button = Button( "High Score", game=self, offsety=280)
        self.back_button = Button( "Back", game=self, offsety=280)
        
        pg.display.set_caption("Pacman Portal")

        self.sound = Sound(bg_music="sounds/startrek.wav")
        self.launch = Launch(game=self)
        self.hs = HighScore(game=self)
        self.scoreboard = Scoreboard(game=self)

        
    def restart(self): pass

    def handle_events(self):
        #TODO handle Pacman movement  -- ghosts move by themselves
        keys_dir = {pg.K_w: Vector(0, -1), pg.K_UP: Vector(0, -1), 
                    pg.K_s: Vector(0, 1), pg.K_DOWN: Vector(0, 1),
                    pg.K_a: Vector(-1, 0), pg.K_LEFT: Vector(-1, 0),
                    pg.K_d: Vector(1, 0), pg.K_RIGHT: Vector(1, 0)}
        
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                self.game_over()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.pacman.v += self.settings.pac_speed * keys_dir[key]
            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.pacman.v = Vector()
                    self.pacman.portal = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.check_buttons(mouse_x, mouse_y)
    
    def game_over(self):
        # self.sound.gameover()
        self.scoreboard.update_disk()
        pg.quit()
        sys.exit()

    def check_buttons(self, mouse_x, mouse_y):
        if not self.settings.game_active:
            if not self.settings.hs_active:
                self.check_hs_button(mouse_x, mouse_y)
                self.check_play_button(mouse_x, mouse_y)
            else:
                self.check_back_button(mouse_x, mouse_y)


    def check_back_button(self, mouse_x, mouse_y):
        button_clicked = self.back_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.scoreboard.reset()
            self.settings.hs_active = False

    def check_hs_button(self, mouse_x, mouse_y):
        button_clicked = self.hs_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.scoreboard.reset()
            self.settings.hs_active = True

    def check_play_button(self, mouse_x, mouse_y):
        button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.settings.init_speeds()
            self.sound.play_bg()
            pg.mouse.set_visible(False)

            self.scoreboard.reset()
            self.settings.game_active = True

            self.scoreboard.prep_score()
            

    def update_screen(self):

        if not self.settings.game_active:
            # self.space_text.draw_button()
            # self.invaders_text.draw_button()
            self.sound.stop_bg()
            if self.settings.hs_active:
                self.hs.update()
                self.back_button.draw_button()
            else:
                self.launch.update()
                self.play_button.draw_button()
                self.hs_button.draw_button()

    def play(self):
        # self.sound.play_bg()
        while True:
            self.handle_events()
            self.screen.fill(self.settings.bg_color)
            self.update_screen()
            if self.settings.game_active:
                self.maze.update()
                self.ghosts.update()
                self.pacman.update()
                self.scoreboard.update()
                self.maze.check_collisions()
            
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()

