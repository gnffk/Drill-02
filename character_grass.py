from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')
x = 0
y=0

turn = 0
if turn == 0:
    if x ==0 :
        while (x <= 750):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y+90)
            x = x + 2
            delay(0.01)
    if x >= 750:
        while (y <= 500):
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y+90)
            y = y + 2
            delay(0.01)
    if y >= 500:
        while(x>=0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y+90)
            x = x-2
            delay(0.01)
    if x <=0:
        while(y>=0):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y+90)
            y = y-2
            delay(0.01)
    if y <= 0:
        while(x<=400):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y+90)
            x = x+2
            delay(0.01)
            turn =1
if turn == 1:
    while(x<=400):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(math.sin(x/360*2*math.pi),math.sin((y+90)/360*2*math.pi))
         delay(0.01)
close_canvas()
