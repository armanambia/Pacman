import pygame
from pygame.sprite import Sprite
from vector import Vector

class Portal(Sprite):
    def __init__(self, game):
        super(Portal, self).__init__()
        self.screen = game.screen
        self.size = (15, 15)
        
        self.image = pygame.image.load('images/portal.png')
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.game = game
        
        self.image = self.image
        self.rect = self.image.get_rect()        
        self.posn = Vector()

    def update(self): pass
    def draw(self):
        self.screen.blit(self.image, self.rect)