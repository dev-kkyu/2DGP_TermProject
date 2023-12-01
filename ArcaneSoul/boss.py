import random
import math

import boss_mode
import game_framework

from pico2d import *

import game_world

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
FRAME_PER_TIME = 5

class Boss:
    walk_images = ()
    attack_images = ()

    def load_images(self):
        if not Boss.walk_images:
            Boss.walk_images = ([load_image('Resources/Boss/Walk/' + str(i + 1) + '.png') for i in range(4)], 4)
        if not Boss.attack_images:
            Boss.attack_images = ([load_image('Resources/Boss/Attack/' + str(i + 1) + '.png') for i in range(6)], 6)

    def __init__(self):
        self.x, self.y = random.randint(640, boss_mode.background.w - 50), 330
        self.load_images()
        self.frame = random.randint(0, 2)
        self.dir = random.choice([-1,1])
        self.is_attack = False
        self.hp = 300
        self.font = load_font('ENCR10B.TTF', 64)
        self.last_attack_time = get_time()
        self.attacked_move_value = 0


    def update(self):
        if abs(self.x - boss_mode.lisa.x) < 200:
            self.is_attack = True
        else:
            self.is_attack = False
        if self.is_attack:
            self.frame = (self.frame + FRAME_PER_TIME * game_framework.frame_time) % Boss.attack_images[1]
        else:
            self.frame = (self.frame + FRAME_PER_TIME * game_framework.frame_time) % Boss.walk_images[1]
            self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
            if self.x - boss_mode.lisa.x > 0:
                self.dir = -1
            else:
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
        self.x = clamp(640, self.x, boss_mode.background.w - 50)
        if self.hp <= 0:
            game_world.remove_object(self)
            game_world.remove_collision_object(self)


    def draw(self):
        sx = self.x - boss_mode.background.window_left
        if self.is_attack:
            if self.dir > 0:
                Boss.attack_images[0][int(self.frame)].composite_draw(0, '', sx, self.y + 45, 476, 592)
            else:
                Boss.attack_images[0][int(self.frame)].composite_draw(0, 'h', sx, self.y + 45, 476, 592)
        else:
            if self.dir > 0:
                Boss.walk_images[0][int(self.frame)].composite_draw(0, '', sx, self.y, 314, 516)
            else:
                Boss.walk_images[0][int(self.frame)].composite_draw(0, 'h', sx, self.y, 314, 516)
        # draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 각각 인자로 전달.
        self.font.draw(sx - 25, self.y + 300, str(self.hp), (255, 0, 0))


    def add_hp(self, hp):
        now_time = get_time()
        if now_time > self.last_attack_time + 0.5:
            self.hp += hp
            self.last_attack_time = now_time


    def handle_event(self, event):
        pass


    def get_bb(self):
        return self.x - 150, self.y - 250, self.x + 150, self.y + 250 # 값 4개짜리 튜플 1개

    def handle_collision(self, group, other):
        pass