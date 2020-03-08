#Snake Game
#Name: Richard John

import curses
import random

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snkX = sw/4
snkY = sh/4

snake = [
    [snkY, snkX],
    [snkY, snkX-1],
    [snkY, snkX-2]
]

apple = [sh/2, sw/2]
w.addch(apple[0], apple[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()


    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_LEFT:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[0] += 1

    snake.insert(0, new_head)

    if snake[0] == apple:
        apple = None
        while apple is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
                ]
            apple = nf if nf not in snake else None
        w.addch(apple[0], apple[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)