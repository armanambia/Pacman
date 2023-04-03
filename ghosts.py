import pygame as pg 
from pygame.sprite import Sprite, Group
from timer import Timer

class Ghosts:
    def __init__(self, game):
        self.game = game
        self.ghosts = Group()
        self.ghost_list = [Blinky(game=game), Inky(game=game), 
                           Pinky(game=game), Clyde(game=game)]
        for ghost in self.ghost_list:
            self.ghosts.add(ghost)

    def update(self): 
        for ghost in self.ghosts:
            ghost.update()
        self.draw()

    def draw(self): 
        for ghost in self.ghosts:
            ghost.draw()


class Ghost(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.size = (self.settings.ghost_size , self.settings.ghost_size)
    def setParameters(self, off_x=0, off_y=0):
        self.image = pg.transform.scale(self.image, (self.size[0], self.size[1]))
        self.rect = self.image.get_rect()
        self.rect.x = 240 + off_x
        self.rect.y = 300
    def setAnimation(self, name):
        self.images = [ pg.transform.scale(pg.image.load(f'images/{name}/sprite_{("0" + str(x)) if x < 10 else x}.png'), (self.size[0], self.size[1])) for x in range(12)]
        self.timer_normal = Timer(self.images, 0, delay=50)
        self.blue_images = [pg.transform.scale(pg.image.load(f'images/blue_ghost/sprite_{x}.png'), (self.size[0], self.size[1])) for x in range(4)]
        self.timer_blue = Timer(self.blue_images, 0, delay=50)
        self.timer = self.timer_normal
    def update(self): 
        self.draw
    def draw(self): 
        self.image = self.timer.image()
        self.screen.blit(self.image, self.rect)


class Blinky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
        self.image = pg.image.load('images/blinky/sprite_00.png')
        super().setParameters()
        super().setAnimation("blinky")
    def update(self): 
        super().update()
    def draw(self): 
        super().draw()


class Inky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
        self.image = pg.image.load('images/inky/sprite_00.png')
        super().setParameters(off_x= 30)
        super().setAnimation("inky")
    def update(self): 
        super().update()
    def draw(self): 
        super().draw()

class Pinky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
        self.image = pg.image.load('images/pinky/sprite_00.png')
        super().setParameters(off_x= 60)
        super().setAnimation("pinky")
    def update(self): 
        super().update()
    def draw(self): 
        super().draw()


class Clyde(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
        self.image = pg.image.load('images/clyde/sprite_00.png')
        super().setParameters(off_x= 90)
        super().setAnimation("clyde")
    def update(self): 
        super().update()
    def draw(self): 
        super().draw()
