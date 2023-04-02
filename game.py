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
import sys

from pygame.sprite import Sprite, Group


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height  # tuple
        self.screen = pg.display.set_mode(size=size)
        self.maze = Maze(game=self)
        self.ghosts = Ghosts(game=self)
        self.pacman = Pacman(game=self)
        self.scoreboard = Scoreboard(game=self)
        
        
        pg.display.set_caption("Pacman Portal")

        self.sound = Sound(bg_music="sounds/startrek.wav")
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
                # self.scoreboard.scoreboard_list()
                # self.game_over()
                # self.d.close()
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                key = event.key
                if key in keys_dir:
                    self.pacman.v += self.settings.pac_speed * keys_dir[key]
                    

            elif event.type == pg.KEYUP:
                key = event.key
                if key in keys_dir:
                    self.pacman.v = Vector()
                    self.pacman.portal = False

    def check_collisions(self):
        # pacman - wall
        pass

    def game_over(self):
        # self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        # self.sound.play_bg()
        while True:
            self.handle_events()
            self.screen.fill(self.settings.bg_color)
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

