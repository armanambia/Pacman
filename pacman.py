import pygame as pg
from timer import Timer
from vector import Vector
from utils import Util

class Pacman:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = self.game.settings
        self.size = (self.settings.pac_size, self.settings.pac_size)
        self.images = [ pg.transform.scale(pg.image.load(f'images/pacman/{x}.png'), (self.size[0], self.size[1])) for x in range(4)]
        self.timer = Timer(self.images, 0, delay=50)
        self.cur_img = self.timer.image()
        self.rect = self.cur_img.get_rect()
        self.portal = False
        self.init_position()

    def init_position(self):
        self.rect.x = self.settings.pac_start_x
        self.rect.y = self.settings.pac_start_y
        self.posn = Vector(self.rect.left, self.rect.top)
        self.v = Vector()
        self.rotation = 0

    def rotate(self):
        if self.v.x == 0:
            # down
            if self.v.y > 0:
                self.rotation = 270
            # up
            elif self.v.y < 0:
                self.rotation = 90
        # left
        elif self.v.x < 0:
            self.rotation = 180
        # right
        elif self.v.x > 0:
            self.rotation = 0

    def update(self):
        self.posn += self.v
        
        # tunnel 1
        if self.posn.x < 14:
            self.posn = Vector(580, self.posn.y)
        # tunnel 2
        elif self.posn.x > 600: 
            self.posn = Vector(20, self.posn.y)
        self.posn, self.rect = Util.clamp(posn=self.posn, rect=self.rect, settings=self.settings)
        self.rotate()
        self.draw()

    def draw(self): 
        image = pg.transform.rotate(self.timer.image(), self.rotation)
        rect = self.rect
        rect.center = (self.rect.x, self.rect.y)
        self.screen.blit(image, rect)