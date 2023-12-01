from pico2d import *

import boss_mode
import play_mode
import server


class Background2:
    width = 2500
    def __init__(self):
        self.image = load_image('Resources/Background/b1.png')
        self.cw = get_canvas_width()

        self.w = Background2.width

        self.window_left = 0

        server.background = self

    def update(self):
        self.window_left = int(boss_mode.lisa.x) - self.cw // 2
        self.window_left = clamp(0, self.window_left, self.w - self.cw - 1)
        pass

    def draw(self):
        for x in range(0, 1280 + 498, 498):
                self.image.draw(x - (int(self.window_left) % 498), 360, 498, 720)


class Grass2:
    def __init__(self):
        self.image = load_image('Resources/Background/n2.png')

    def update(self):
        pass

    def draw(self):
        for x in range(0, 1280, 68):
            self.image.draw(x + 34, 83)

