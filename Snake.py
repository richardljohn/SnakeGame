#Snake Game
#Name: Richard John

import curses
import random

s = curses.initscr()
curses.curs_set(0)
h, w = s.getmaxyx()
w = curses.newwin(h, w, 0, 0)
w.keypad(1)
w.timeout(100)

snkX = w/4
snkY = h/4

snek = [
    [snkY, snkX],
    [snkY, snkX-1],
    [snkY, snkX-2]
]

apple = [h/2, w/2]
w.addch(apple[0], apple[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, h] or snake[0][1] in [0, w] or snake 
