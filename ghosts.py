import pygame as pg 
from pygame.sprite import Sprite, Group


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
    def update(self): pass
    def draw(self): pass


class Blinky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
    def update(self): pass
    def draw(self): pass


class Inky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
    def update(self): pass
    def draw(self): pass


class Pinky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
    def update(self): pass
    def draw(self): pass


class Clyde(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game
    def update(self): pass
    def draw(self): pass
