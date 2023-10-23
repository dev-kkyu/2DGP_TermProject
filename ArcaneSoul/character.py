# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, \
    draw_rectangle
from sdl2 import SDLK_LCTRL

from ball import Ball
import game_world
import game_framework

# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def ctrl_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LCTRL

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# TIME_PER_ACTION = 0.5
# ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
# FRAMES_PER_ACTION = 8
FRAME_PER_TIME = 10











class Idle:

    @staticmethod
    def enter(boy, e):
        boy.dir = 0
        boy.frame = 0
        # boy.wait_time = get_time() # pico2d import 필요
        if boy.is_attack:
            Attack.enter(boy, e)
        pass

    @staticmethod
    def exit(boy, e):
        # if space_down(e):
        #     boy.fire_ball()
        if ctrl_down(e):
            boy.is_attack = True
        pass

    @staticmethod
    def do(boy):
        if boy.is_attack:
            Attack.do(boy)
        else:
            boy.frame = (boy.frame + FRAME_PER_TIME * game_framework.frame_time) % boy.idle_images[1]
        # if get_time() - boy.wait_time > 2:
        #     boy.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(boy):
        if boy.is_attack:
            Attack.draw(boy)
        else:
            if boy.face_dir == 1:
                boy.idle_images[0][int(boy.frame)].composite_draw(0, '', boy.x, boy.y, 150, 270)
            else:
                boy.idle_images[0][int(boy.frame)].composite_draw(0, 'h', boy.x, boy.y, 150, 270)



class Walk:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir = 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            boy.dir, boy.face_dir = -1, -1
        if boy.is_attack:
            Attack.enter(boy, e)

    @staticmethod
    def exit(boy, e):
        # if space_down(e):
        #     boy.fire_ball()
        if ctrl_down(e):
            boy.is_attack = True

        pass

    @staticmethod
    def do(boy):
        if boy.is_attack:
            Attack.do(boy)
        else:
            # boy.frame = (boy.frame + 1) % 8
            boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
            boy.x = clamp(25, boy.x, 1280-25)
            boy.frame = (boy.frame + FRAME_PER_TIME * game_framework.frame_time) % boy.walk_images[1]


    @staticmethod
    def draw(boy):
        if boy.is_attack:
            Attack.draw(boy)
        else:
            if boy.face_dir == 1:
                boy.walk_images[0][int(boy.frame)].composite_draw(0, '', boy.x, boy.y, 150, 270)
            else:
                boy.walk_images[0][int(boy.frame)].composite_draw(0, 'h', boy.x, boy.y, 150, 270)
            # boy.image.clip_draw(int(boy.frame) * 100, boy.action * 100, 100, 100, boy.x, boy.y)

class Attack:

    @staticmethod
    def enter(boy, e):
        boy.frame = 0
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.face_dir = 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            boy.dir, boy.face_dir = -1, -1

    @staticmethod
    def exit(boy, e):
        # if space_down(e):
        #     boy.fire_ball()

        pass

    @staticmethod
    def do(boy):
        # boy.frame = (boy.frame + 1) % 8
        boy.frame = (boy.frame + FRAME_PER_TIME * game_framework.frame_time)
        if boy.frame >= boy.attack_images[1] // 2:
            boy.is_attack = False


    @staticmethod
    def draw(boy):
        if (boy.face_dir == 1):
            boy.attack_images[0][int(boy.frame)].composite_draw(0, '', boy.x, boy.y, 324, 270)
        else:
            boy.attack_images[0][int(boy.frame)].composite_draw(0, 'h', boy.x, boy.y, 324, 270)


#
# class Sleep:
#
#     @staticmethod
#     def enter(boy, e):
#         boy.frame = 0
#         pass
#
#     @staticmethod
#     def exit(boy, e):
#         pass
#
#     @staticmethod
#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#
#
#     @staticmethod
#     def draw(boy):
#         if boy.face_dir == -1:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100,
#                                           -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
#         else:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100,
#                                           3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
#

class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Walk, left_down: Walk, left_up: Walk, right_up: Walk, space_down: Idle, ctrl_down: Idle},
            Walk: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Walk, ctrl_down: Walk},
            # Attack: {time_out: Idle}
            # Sleep: {right_down: Run, left_down: Run, right_up: Run, left_up: Run}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)





class Boy:
    def __init__(self):
        self.is_attack = False
        self.x, self.y = 150, 230
        self.frame = 0
        self.face_dir = 1
        self.dir = 0
        self.walk_images = ([load_image('Resources/Character/Walk/' + str(i) + '.png') for i in range(8)], 8)
        self.dash_images = ([load_image('Resources/Character/Dash/' + str(i) + '.png') for i in range(1)], 1)
        self.attack_images = ([load_image('Resources/Character/Attack/' + str(i) + '.png') for i in range(8)], 8)
        self.idle_images = ([load_image('Resources/Character/Idle/' + str(i) + '.png') for i in range(11)], 11)
        self.jump_images = ([load_image('Resources/Character/Jump/' + str(i) + '.png') for i in range(7)], 7)
        self.skill_images = ([load_image('Resources/Character/Skill/' + str(i) + '.png') for i in range(4)], 4)
        self.font = load_font('ENCR10B.TTF', 16)
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    # def fire_ball(self):
    #     if self.ball_count > 0:
    #         self.ball_count -= 1
    #         ball = Ball(self.x, self.y, self.face_dir*10)
    #         game_world.add_object(ball)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        # self.font.draw(self.x-10, self.y + 50, f'{self.ball_count:02d}', (255, 255, 0))
        draw_rectangle(*self.get_bb())  # 튜플을 풀어헤쳐서 각각 인자로 전달.

    # fill here
    def get_bb(self):
        return self.x - 75, self.y - 135, self.x + 75, self.y + 135 # 값 4개짜리 튜플 1개

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            self.ball_count +=1