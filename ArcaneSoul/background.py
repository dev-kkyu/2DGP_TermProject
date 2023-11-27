from pico2d import *

import play_mode


class Background:
    width = 2500
    def __init__(self):
        self.image = load_image('Resources/Background/b1.png')
        self.cw = get_canvas_width()

        self.w = Background.width

        self.window_left = 0

    def update(self):
        self.window_left = int(play_mode.lisa.x) - self.cw // 2
        self.window_left = clamp(0, self.window_left, self.w - self.cw - 1)
        pass

    def draw(self):
        for x in range(0, 1280 + 249, 498):
                self.image.draw(x - (int(self.window_left) % 498), 360, 498, 720)


class Grass:
    def __init__(self):
        self.image = load_image('Resources/Background/n.png')

    def update(self):
        pass

    def draw(self):
        for x in range(0, 1280, 68):
            self.image.draw(x + 34, 83)

