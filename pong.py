# Author: Xiaoxuan
# Date: 4/25/2021
# Purpose: 2-player pong game

from cs1lib import *

# window dimensions
W_WIDTH = 400
W_HEIGHT = 400

# paddle dimensions
P_WIDTH = 20
P_HEIGHT = 80

# paddle coordinates
LPX = 0
RPX = W_WIDTH - P_WIDTH
lpy = 0
rpy = W_HEIGHT - P_HEIGHT

# paddle movement
P_MOVEMENT = 10
apressed = False
zpressed = False
kpressed = False
mpressed = False

# ball dimension
B_RADIUS = 7

# ball coordinates
bx = W_WIDTH/2
by = W_HEIGHT/2

# ball movement
bxmovement = 3
bymovement = 4

# game state
game_in_progress = True
new_game = False


# key press function for paddle movement and game progress
def my_kpress(value):
    global apressed, zpressed, kpressed, mpressed, game_in_progress, new_game
    if value.lower() == 'a':
        apressed = True
    if value.lower() == 'z':
        zpressed = True
    if value.lower() == 'k':
        kpressed = True
    if value.lower() == 'm':
        mpressed = True
    if value == ' ':
        new_game = True
        game_in_progress = True
    if value.lower() == 'q':
        cs1_quit()


# key release function for paddle movement
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


# use keyboard to move the two paddles up or down
def move_paddles():
    global lpy, rpy
    if apressed and lpy >= P_MOVEMENT:
        lpy -= P_MOVEMENT
    if zpressed and lpy <= W_HEIGHT - P_HEIGHT - P_MOVEMENT:
        lpy += P_MOVEMENT
    if kpressed and rpy >= P_MOVEMENT:
        rpy -= P_MOVEMENT
    if mpressed and rpy <= W_HEIGHT - P_HEIGHT - P_MOVEMENT:
        rpy += P_MOVEMENT

    draw_rectangle(LPX, lpy, P_WIDTH, P_HEIGHT)
    draw_rectangle(RPX, rpy, P_WIDTH, P_HEIGHT)


# check if the ball moved beyond the top wall
def hit_top_wall(by, wy):
    return by - B_RADIUS <= wy


# check if the ball moved beyond the bottom wall
def hit_bottom_wall(by, wy):
    return by + B_RADIUS >= wy


# check if the ball moved beyond the right wall
def hit_right_wall(bx, wx):
    return bx + B_RADIUS >= wx


# check if the ball moved beyond the left wall
def hit_left_wall(bx, wx):
    return bx - B_RADIUS <= wx


# check if the ball made contact with the right paddle
def hit_right_paddle(bx, by):
    return bx + B_RADIUS >= RPX and by - B_RADIUS >= rpy and by + B_RADIUS <= rpy + P_HEIGHT


# check if the ball made contact with the left paddle
def hit_left_paddle(bx, by):
    return bx - B_RADIUS <= LPX + P_WIDTH and by - B_RADIUS >= lpy and by + B_RADIUS <= lpy + P_HEIGHT


# control how the ball moves and bounces
def ball_movement():
    global bxmovement, bymovement, bx, by, game_in_progress

    # if the ball hits the vertical walls, stop the game
    if hit_left_wall(bx, 0) or hit_right_wall(bx, W_WIDTH):
        game_in_progress = False

    # update ball position only if the game is in progress
    if game_in_progress:
        bx += bxmovement
        by += bymovement

    # if the ball hits the horizontal walls, change the direction of vertical movement
    if hit_top_wall(by, 0) or hit_bottom_wall(by, W_HEIGHT):
        bymovement = -bymovement

    # if the ball hits the two paddles, change the direction of horizontal movement
    if hit_left_paddle(bx, by):
        bxmovement = -bxmovement
        if game_in_progress:
            bx += B_RADIUS  # prevent slithering behavior
    if hit_right_paddle(bx, by):
        bxmovement = -bxmovement
        if game_in_progress:
            bx -= B_RADIUS  # prevent slithering behavior

    draw_circle(bx, by, B_RADIUS)


# if the user starts a new game, reset ball position
def game_restart():
    global new_game, bx, by
    if new_game:
        bx = W_WIDTH / 2
        by = W_HEIGHT / 2
        new_game = False


# set the background to yellow
def set_background_yellow():
    set_clear_color(1, 1, 0)  # yellow
    clear()


# set the fill color to brown
def set_fill_brown():
    set_fill_color(.5, .4, .2)  # brown


# main animation function
def main_draw():
    set_background_yellow()
    disable_stroke()
    set_fill_brown()

    game_restart()
    move_paddles()
    ball_movement()


start_graphics(main_draw, key_press=my_kpress, key_release=my_krelease)
