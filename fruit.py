import pygame
from pygame.sprite import Sprite

class Fruit(Sprite):
    def __init__(self, game):
        super(Fruit, self).__init__()
        self.screen = game.screen
        self.size = (7, 7)
        self.image = pygame.image.load('images/fruit.png')
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.game = game
        
        self.rect = self.image.get_rect()        

    def update(self): pass

    def draw(self):
        self.screen.blit(self.image, self.rect)