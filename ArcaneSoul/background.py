from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Resources/Background/b1.png')

    def update(self):
        pass

    def draw(self):
        for x in range(0, 1600, 498):
                self.image.draw(x + 249, 450, 498, 900)


