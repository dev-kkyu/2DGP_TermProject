from pico2d import open_canvas, delay, close_canvas, hide_lattice
import game_framework

import play_mode as start_mode
import title_mode as start_mode
open_canvas(1280, 720)
hide_lattice()
game_framework.run(start_mode)
close_canvas()

