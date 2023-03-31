import pygame as pg
from pygame.sprite import Sprite, Group
from Barrier import Barrier


class Maze:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.walls = Group()
        self.create_maze()
        

    def update(self):
        # TODO -- update maze as necessary to show points being eaten
        self.draw()

    def draw(self):
        rect = self.image.get_rect()
        self.screen.blit(self.image, rect)

    def create_maze():
        file = open("layout.txt", "r")
        order = file.read()
        rows = []
        curr_row = []
        for el in order:
            if el != '\n':
                curr_row.append(el)
            else:
                rows.append(curr_row)
                curr_row = []

        offset_horizontal = 0
        offset_vertical = 0

        for row in rows:
            for el in row:
                if el == 'X':
                    new_wall = Wall(self.game)
                    new_wall.rect.x = 13 * offset_horizontal
                    new_wall.rect.y = 13 * offset_vertical
                    (self.game.walls).add(new_wall)
                elif el == 'd':
                    new_fruit = Fruit(self.game)
                    new_fruit.rect.x = 13 * offset_horizontal
                    new_fruit.rect.y = 13 * offset_vertical
                    (self.game.food).add(new_fruit)
                elif el == 'o':
                    new_shield = Shield(self.game)
                    new_shield.rect.x = 13 * offset_horizontal
                    new_shield.rect.y = 13 * offset_vertical
                    (self.game.shield).add(new_shield)
                elif el == 'h':
                    pass
                elif el == 'P':
                    new_portal = Portal(self.game)
                    new_portal.rect.x = 13 * offset_horizontal
                    new_portal.rect.y = 13 * offset_vertical
                    (self.game.portal).add(new_portal)
                offset_horizontal += 1
            offset_horizontal = 0
            offset_vertical += 1