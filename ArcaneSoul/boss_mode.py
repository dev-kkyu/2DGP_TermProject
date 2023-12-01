import random

from pico2d import *
import game_framework

import game_world
from background2 import Grass2, Background2
from boss import Boss
from character import Lisa

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            lisa.handle_event(event)

def init():
    global background
    global grass
    global lisa

    running = True

    background = Background2()
    lisa = Lisa()

    game_world.add_object(background, 0)
    game_world.add_object(lisa, 1)

    grass = Grass2()
    game_world.add_object(grass, 0)

    monster = Boss()
    game_world.add_object(monster, 1)

    game_world.add_collision_pair('lisa:monster', lisa, None)
    game_world.add_collision_pair('lisa:monster', None, monster)

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

