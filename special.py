import pygame
from pygame.sprite import Sprite

class Special(Sprite):
    def __init__(self, game):
        super(Special, self).__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen

        self.size = (self.settings.spc_size, self.settings.spc_size)
        self.image = pygame.image.load('images/special.png')
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        
        
        self.rect = self.image.get_rect()     
        self.rect.x = -5
        self.rect.y = -5   

    def update(self): pass

    def draw(self):
        self.screen.blit(self.image, self.rect)