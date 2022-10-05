# Author: Xiaoxuan
# Date: 4/21/2021
# Purpose: move the paddles in a pong game

from cs1lib import *

W_WIDTH = 400
W_HEIGHT = 400
P_WIDTH = 20
P_HEIGHT = 80
MOVEMENT = 10
X1 = 0
y1 = 0
X2 = W_WIDTH - P_WIDTH
y2 = W_HEIGHT - P_HEIGHT
apressed = False
zpressed = False
kpressed = False
mpressed = False


def my_kpress(value):
    global apressed, zpressed, kpressed, mpressed
    if value.lower() == 'a':
        apressed = True
    if value.lower() == 'z':
        zpressed = True
    if value.lower() == 'k':
        kpressed = True
    if value.lower() == 'm':
        mpressed = True


def my_krelease(value):
    global apressed, zpressed, kpressed, mpressed
    if value.lower() == 'a':
        apressed = False
    if value.lower() == 'z':
        zpressed = False
    if value.lower() == 'k':
        kpressed = False
    if value.lower() == 'm':
        mpressed = False


def main_draw():
    set_clear_color(1, 1, 0)  # yellow
    clear()

    disable_stroke()
    set_fill_color(.5, .4, .2)  # brown

    global y1, y2
    if apressed and y1 >= MOVEMENT:
        y1 -= MOVEMENT
    if zpressed and y1 <= W_HEIGHT-P_HEIGHT-MOVEMENT:
        y1 += MOVEMENT
    if kpressed and y2 >= MOVEMENT:
        y2 -= MOVEMENT
    if mpressed and y2 <= W_HEIGHT-P_HEIGHT-MOVEMENT:
        y2 += MOVEMENT

    draw_rectangle(X1, y1, P_WIDTH, P_HEIGHT)
    draw_rectangle(X2, y2, P_WIDTH, P_HEIGHT)


start_graphics(main_draw, key_press=my_kpress, key_release=my_krelease)
