import pygame as pg

class Launch:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.title_images = []
        self.set_1 = []
        self.animation_1 = []
        self.animation_1_offset = 0
        self.animation_2 = []
        self.animation_2_offset = 0
        self.default_color = (255, 255, 255)
        self.offset = 3
        self.title()
        self.prep_set_1()
        self.prep_animation_1()
        self.prep_animation_2()
        self.current = 0
        self.time = pg.time.get_ticks()

    def title(self):
        self.title_images.append(self.prep_Text("PA", 120, offsetX=140, offsetY=60))
        self.title_images.append(self.prep_Text("CMAN", 120, offsetX=400, offsetY=60))
        pacman = pg.transform.rotozoom(pg.image.load(f'images/pacman/2.png'), 0, 5)
        self.title_images.append((pacman, (260, 40)))

    
    def prep_set_1(self):
        self.set_1.append(self.prep_Text("BLINKY", 40, color=(255,0,0), offsetX=150, offsetY=300))
        self.set_1.append(self.prep_Text("PINKY", 40, color=(255, 138, 224), offsetX=300, offsetY=300))
        self.set_1.append(self.prep_Text("INKY", 40,color=(77, 216, 255), offsetX=450, offsetY=300))
        self.set_1.append(self.prep_Text("CLYDE", 40, color=(255, 147, 84), offsetX=600, offsetY=300))
        blinky = pg.transform.rotozoom(pg.image.load(f'images/blinky/sprite_00.png'), 0, 1)
        self.set_1.append((blinky, (180, 350)))
        pinky = pg.transform.rotozoom(pg.image.load(f'images/pinky/sprite_00.png'), 0, 1)
        self.set_1.append((pinky, (330, 350)))
        inky = pg.transform.rotozoom(pg.image.load(f'images/inky/sprite_00.png'), 0, 1)
        self.set_1.append((inky, (480, 350)))
        clyde = pg.transform.rotozoom(pg.image.load(f'images/clyde/sprite_00.png'), 0, 1)
        self.set_1.append((clyde, (630, 350)))
    
   
    def prep_animation_1(self):
        blinky = pg.transform.rotozoom(pg.image.load(f'images/blinky/sprite_00.png'), 0, 1)
        self.animation_1.append((blinky, (50, 350)))
        pinky = pg.transform.rotozoom(pg.image.load(f'images/pinky/sprite_00.png'), 0, 1)
        self.animation_1.append((pinky, (90, 350)))
        inky = pg.transform.rotozoom(pg.image.load(f'images/inky/sprite_00.png'), 0, 1)
        self.animation_1.append((inky, (130, 350)))
        clyde = pg.transform.rotozoom(pg.image.load(f'images/clyde/sprite_00.png'), 0, 1)
        self.animation_1.append((clyde, (170, 350)))
        pacman = pg.transform.rotozoom(pg.image.load(f'images/pacman/2.png'), 0, 1.5)
        self.animation_1.append((pacman, (250, 350)))
        fruit = pg.transform.rotozoom(pg.image.load(f'images/fruit.png'), 0, 1)
        self.animation_1.append((fruit, (300, 350)))

    def prep_animation_2(self):
        ghost = pg.transform.rotozoom(pg.image.load(f'images/blue_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (500, 350)))
        ghost = pg.transform.rotozoom(pg.image.load(f'images/blue_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (540, 350)))
        ghost = pg.transform.rotozoom(pg.image.load(f'images/blue_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (580, 350)))
        ghost = pg.transform.rotozoom(pg.image.load(f'images/blue_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (620, 350)))
        pacman = pg.transform.rotozoom(pg.image.load(f'images/pacman/2.png'), 180, 1.5)
        self.animation_2.append((pacman, (700, 350)))

        

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

        return (text_image,rect)
    


    def reset(self):
        self.images = []
        # self.prep_aliens()

    def update(self):
        if self.current == 0:
            if pg.time.get_ticks() - self.time > 2000:
                self.current = 1
        elif self.current == 1:
            if self.animation_1_offset > 600:
                self.current = 2
                self.animation_1_offset = 0
            elif (pg.time.get_ticks() - self.time) % 20 == 0:
                self.animation_1_offset += self.offset
        elif self.current == 2:
            if self.animation_2_offset > 600:
                self.current = 0
                self.animation_2_offset = 0
                self.time = pg.time.get_ticks()
            elif (pg.time.get_ticks() - self.time) % 20 == 0:
                self.animation_2_offset += self.offset
            
        self.draw()

    def draw(self):
        for image in self.title_images:
            self.screen.blit(image[0], image[1])
        
        if self.current == 0:
            for image in self.set_1:
                self.screen.blit(image[0], image[1])
        elif self.current == 1:
             for image in self.animation_1:
                x = image[1][0] + self.animation_1_offset 
                y = image[1][1]
                self.screen.blit(image[0], (x,y))
        elif self.current == 2:
             for image in self.animation_2:
                x = image[1][0] - self.animation_2_offset 
                y = image[1][1]
                self.screen.blit(image[0], (x,y))