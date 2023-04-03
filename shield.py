import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
    def __init__(self, game):
        super(Shield, self).__init__()
        self.time = pygame.time.get_ticks()
        self.screen = game.screen
        self.size = (5, 5)
        self.image = pygame.image.load('images/shield.png')
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.game = game
        
        self.rect = self.image.get_rect() 
        self.rect.x = 5
        self.rect.y = 5       

    def update(self): pass
    
    def draw(self):
        if pygame.time.get_ticks() - self.time < 3000:
            self.screen.blit(self.image, self.rect)