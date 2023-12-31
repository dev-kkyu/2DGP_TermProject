import random
import math
import game_framework

from pico2d import *

import game_world
import play_mode

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
FRAME_PER_TIME = 5

class Monster:
    walk_images = ()
    attack_images = ()
    attacked_image = None

    def load_images(self):
        if not Monster.walk_images:
            Monster.walk_images = ([load_image('Resources/Monster/Walk/' + str(i) + '.png') for i in range(4)], 4)
        if not Monster.attack_images:
            Monster.attack_images = ([load_image('Resources/Monster/Attack/' + str(i) + '.png') for i in range(3)], 3)
        if not Monster.attacked_image:
            Monster.attacked_image = load_image('Resources/Monster/Attack/Attacked.png')

    def __init__(self):
        self.x, self.y = random.randint(640, play_mode.background.w - 50), 170
        self.load_images()
        self.frame = random.randint(0, 2)
        self.dir = random.choice([-1,1])
        self.is_attack = False
        self.hp = 100
        self.font = load_font('ENCR10B.TTF', 30)
        self.last_attack_time = get_time()
        self.attacked_move_value = 0


    def update(self):
        if abs(self.x - play_mode.lisa.x) < 100:
            self.is_attack = True
        else:
            self.is_attack = False
        if self.is_attack:
            self.frame = (self.frame + FRAME_PER_TIME * game_framework.frame_time / 2) % Monster.attack_images[1]
        else:
            self.frame = (self.frame + FRAME_PER_TIME * game_framework.frame_time) % Monster.walk_images[1]
            self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
            if self.x > play_mode.background.w - 50:
                self.dir = -1
            elif self.x < 640:
                self.dir = 1
        if self.attacked_move_value != 0:
            if self.attacked_move_value > 0:
                move_val = RUN_SPEED_PPS * game_framework.frame_time * 5
                self.attacked_move_value -= move_val
                self.x += move_val
            else:
                move_val = RUN_SPEED_PPS * game_framework.frame_time * -5
                self.attacked_move_value -= move_val
                self.x -= move_val
            if abs(self.attacked_move_value) < 1:
                self.attacked_move_value = 0
        self.x = clamp(640, self.x, play_mode.background.w - 50)
        if self.hp <= 0:
            game_world.remove_object(self)
            game_world.remove_collision_object(self)


    def draw(self):
        sx = self.x - play_mode.background.window_left
        if self.attacked_move_value != 0:
            Monster.attacked_image.composite_draw(0, '', sx, self.y, 163, 180)
            pass
        elif self.is_attack:
            if self.dir > 0:
                Monster.attack_images[0][int(self.frame)].composite_draw(0, '', sx, self.y, 268, 189)
            else:
                Monster.attack_images[0][int(self.frame)].composite_draw(0, 'h', sx, self.y, 268, 189)
        else:
            if self.dir > 0:
                Monster.walk_images[0][int(self.frame)].composite_draw(0, '', sx, self.y, 163, 180)
            else:
                Monster.walk_images[0][int(self.frame)].composite_draw(0, 'h', sx, self.y, 163, 180)
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 각각 인자로 전달.
        self.font.draw(sx - 25, self.y + 80, str(self.hp), (255, 0, 0))


    def add_hp(self, hp):
        now_time = get_time()
        if now_time > self.last_attack_time + 0.5:
            self.hp += hp
            self.last_attack_time = now_time


    def handle_event(self, event):
        pass


    def get_bb(self):
        return self.x - 80, self.y - 90, self.x + 80, self.y + 90 # 값 4개짜리 튜플 1개

    def handle_collision(self, group, other):
        pass