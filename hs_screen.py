import pygame as pg

class HighScore:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.images = []
        self.prep_strings()
        
        # self.prep_aliens()

    
    def prep_strings(self):
        
        self.prep_Text("HIGH SCORE", 150, offsetY=40)
        
        strings  = [f"{x}.    Score: " + str(self.game.disk[f"hs_{x}_score"]) 
                        + ",  Level: " + str(self.game.disk[f"hs_{x}_level"]) for x in range (1,4) ]

        self.prep_Text(strings[0], 90,  offsetY=200)
        self.prep_Text(strings[1], 70, offsetY=300)
        self.prep_Text(strings[2], 70, offsetY=400)
    

    def prep_Text(self, msg, size, color=(255,255,255), offsetX=0, offsetY=0):
        font = pg.font.SysFont(None, size)
        text_image = font.render(msg, True, color, self.settings.bg_color)
        rect = text_image.get_rect()
        if offsetY == 0:
            rect.centery = self.screen_rect.centery
        else:
            rect.top = offsetY
        if offsetX == 0:
            rect.centerx = self.screen_rect.centerx
        else:
            rect.left = offsetX

        self.images.append((text_image,rect))

    def reset(self):
        self.images = []
        self.prep_strings()
        # self.prep_aliens()

    def update(self):
        self.draw()

    def draw(self):
        for image in self.images:
            self.screen.blit(image[0], image[1])