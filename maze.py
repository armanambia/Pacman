import pygame as pg
from pygame.sprite import Group
from barrier import Barrier
from fruit import Fruit
from portal import Portal
from shield import Shield


class Maze:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.barriers = Group()
        self.fruits = Group()
        self.shields = Group()
        self.portals = Group()
        
    def update(self):
        # TODO -- update maze as necessary to show points being eaten
        self.create_maze()
        self.draw()

    def draw(self):
        for e in self.barriers:
            e.draw()
        for e in self.shields:
            e.draw()
        for e in self.fruits:
            e.draw()
        for e in self.portals:
            e.draw()

    def create_maze(self):

        lines = []
        curr = []
        off_horz = off_vert = 0
        file = open("images/maze.txt", "r")
        raw_data = file.read()
        for e in raw_data:
            if e != '\n':
                curr.append(e)
            else:
                lines.append(curr)
                curr = []

        for row in lines:
            for e in row:
                if e == 'X':
                    new_Barrier = Barrier(self.game)
                    new_Barrier.rect.x = 13 * off_horz
                    new_Barrier.rect.y = 13 * off_vert
                    self.barriers.add(new_Barrier)
                elif e == 'd':
                    new_fruit = Fruit(self.game)
                    new_fruit.rect.x = 13 * off_horz
                    new_fruit.rect.y = 13 * off_vert
                    self.fruits.add(new_fruit)
                elif e == 'o':
                    new_shield = Shield(self.game)
                    new_shield.rect.x = 13 * off_horz
                    new_shield.rect.y = 13 * off_vert
                    self.shields.add(new_shield)
                elif e == 'h':
                    pass
                elif e == 'P':
                    new_portal = Portal(self.game)
                    new_portal.rect.x = 13 * off_horz
                    new_portal.rect.y = 13 * off_vert
                    self.portals.add(new_portal)
                off_horz += 1
            off_horz = 0
            off_vert += 1