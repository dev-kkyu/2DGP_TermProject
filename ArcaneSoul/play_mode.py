import random

from pico2d import *
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
    global grass
    global lisa

    running = True

    background = Background()
    game_world.add_object(background, 0)

    grass = Grass()
    game_world.add_object(grass, 0)

    monsters = [Monster() for _ in range(5)]
    game_world.add_objects(monsters, 1)

    lisa = Lisa()
    game_world.add_object(lisa, 1)

    # fill here
    # # 축구공 바닥에 뿌리기
    # global balls
    # balls = [Ball(random.randint(0, 1600), 60, 0.0) for _ in range(30)]
    # game_world.add_objects(balls, 1)
    #
    # # 충돌 상황을 등록... boy와 balls들의 충돌 상황을 등록.
    # game_world.add_collision_pair('boy:ball', boy, None)
    # for ball in balls:
    #     game_world.add_collision_pair('boy:ball', None, ball)
    #
    # # 좀비 5마리 추가
    # zombies = [Zombie() for _ in range(5)]
    # game_world.add_objects(zombies, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()
    # fill here

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

