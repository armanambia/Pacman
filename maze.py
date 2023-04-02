import pygame as pg
from pygame.sprite import Group
from barrier import Barrier
from fruit import Fruit
from portal import Portal
from shield import Shield
from vector import Vector


class Maze:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.barriers = Group()
        self.fruits = Group()
        self.parent_fruits = Group()
        self.shields = Group()
        self.portals = Group()
        self.create_maze()
        
    def update(self):
        # TODO -- update maze as necessary to show points being eaten
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

    def check_collisions(self):
        # check pacman with barrier
        
        for portal in self.portals:
            if pg.sprite.collide_rect(self.game.pacman, portal):
                self.pac_por_col(portal)
        for bar in self.barriers:
            if pg.sprite.collide_rect(self.game.pacman, bar):
                self.pac_mov_col(bar)
        for shield in self.shields:
            if pg.sprite.collide_rect(self.game.pacman, shield):
                self.pac_mov_col(shield)
        for fruit in self.fruits:
            if pg.sprite.collide_rect(self.game.pacman, fruit):
                (self.fruits).remove(fruit)
                self.game.scoreboard.increment_score()
        if not self.fruits:
            self.fruits = self.parent_fruits.copy()
            self.game.scoreboard.next_level()
            self.game.pacman.init_position()
    
    def pac_por_col(self, portal):
        if not self.game.pacman.portal:
            self.game.pacman.portal = True
            self.game.pacman.v = Vector(0,0)
            if portal == self.portals.sprites()[0]:
                self.game.pacman.posn = self.portals.sprites()[2].posn
                # self.game.pacman.posn.y -= 100
                # self.game.pacman.posn.x += 100
            elif portal == self.portals.sprites()[2]:
                self.game.pacman.posn = self.portals.sprites()[0].posn
            elif portal == self.portals.sprites()[1]:
                self.game.pacman.posn = self.portals.sprites()[3].posn
                # self.game.pacman.posn.x += 2
                # self.game.pacman.posn.y -= 3
            elif portal == self.portals.sprites()[3]:
                self.game.pacman.posn = self.portals.sprites()[1].posn 
                # self.game.pacman.posn.x -= 3
                # self.game.pacman.posn.y -= 10
        
        

    def pac_mov_col(self,spr):
        if self.game.pacman.rect.centerx <= spr.rect.centerx:
            self.game.pacman.posn.x -= 1
        else:
            self.game.pacman.posn.x += 1
        if self.game.pacman.rect.y + self.game.pacman.rect.height / 2 <= spr.rect.y + spr.rect.height / 2:
            self.game.pacman.posn.y -= 1
        else:
            self.game.pacman.posn.y += 1


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
                    new_Barrier.rect.x += 13 * off_horz
                    new_Barrier.rect.y += 13 * off_vert
                    self.barriers.add(new_Barrier)
                elif e == 'd':
                    new_fruit = Fruit(self.game)
                    new_fruit.rect.x += 13 * off_horz
                    new_fruit.rect.y += 13 * off_vert
                    self.fruits.add(new_fruit)
                    self.parent_fruits.add(new_fruit)
                elif e == 'o':
                    new_shield = Shield(self.game)
                    new_shield.rect.x += 13 * off_horz
                    new_shield.rect.y += 13 * off_vert
                    self.shields.add(new_shield)
                elif e == 'h':
                    pass
                elif e == 'P':
                    new_portal = Portal(self.game)
                    new_portal.rect.x += 13 * off_horz
                    new_portal.rect.y += 13 * off_vert
                    new_portal.posn = Vector(new_portal.rect.x, new_portal.rect.y)
                    self.portals.add(new_portal)
                off_horz += 1
            off_horz = 0
            off_vert += 1