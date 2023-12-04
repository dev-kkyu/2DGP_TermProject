import random

from pico2d import *
import game_framework

import game_world
import play_mode


class Title:
    def __init__(self):
        self.bg_image = load_image('Resources/Lobby/bg1.png')
        self.bg2_image = load_image('Resources/Lobby/bg0.png')
        self.title_image = load_image('Resources/Lobby/title.png')

    def update(self):
        pass

    def draw(self):
        self.bg_image.draw(640, 360, 1280, 720)
        self.bg2_image.draw(640, 360, 1280, 720)
        self.title_image.draw(640, 400, 1000, 320)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)
        else:
            pass

def init():
    global grass
    global lisa

    running = True

    title = Title()
    game_world.add_object(title, 0)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()
    # fill here


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

