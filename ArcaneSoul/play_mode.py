import random

from pico2d import *

import boss_mode
import game_framework

import game_world
from background import Grass, Background
from character import Lisa
from monster import Monster

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

    background = Background()
    lisa = Lisa()

    game_world.add_object(background, 0)
    game_world.add_object(lisa, 1)

    grass = Grass()
    game_world.add_object(grass, 0)

    monsters = [Monster() for _ in range(10)]
    game_world.add_objects(monsters, 1)

    game_world.add_collision_pair('lisa:monster', lisa, None)
    for mon in monsters:
        game_world.add_collision_pair('lisa:monster', None, mon)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()
    # fill here
    if len(game_world.objects[1]) <= 1:
        game_framework.change_mode(boss_mode)
    # for ball in balls.copy():
    #     if game_world.collide(boy, ball):
    #         print('COLLISION by:ball')
    #         # 충돌 처리
    #         # 볼은 없앤다.
    #         balls.remove(ball)
    #         game_world.remove_object(ball)
    #         # 소년은 볼 카운트 증가
    #         boy.ball_count += 1


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

