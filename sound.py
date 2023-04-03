import pygame as pg
import time


class Sound:
    def __init__(self):
        pg.mixer.init()
        self.bg_music = "sounds/background.wav"
        pg.mixer.music.set_volume(0.1)
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        self.pacman_start = 'sounds/pacmanstart.wav'
        pg.mixer.music.load(self.pacman_start)
    
    def play_start(self):
        pg.mixer.music.play(-1, 0)
    

    def play_bg(self):
        pg.mixer.music.stop()
        pg.mixer.music.load(self.bg_music)
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def gameover(self):
        self.stop_bg() 
        pg.mixer.music.load('sounds/gameover.wav')
        self.play_bg()
        time.sleep(2.8)
