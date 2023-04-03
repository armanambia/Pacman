import pygame as pg

class Button():
    def __init__(self, msg, game, offsetx=0, offsety=0):
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (31, 105, 224)
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centerx = self.screen_rect.centerx + offsetx
        self.rect.centery = self.screen_rect.centery + offsety

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)