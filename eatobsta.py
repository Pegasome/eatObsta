import time
import msvcrt
import random

s = [' ']*103
s[0], s[102] = '[[[[', ']]]]'

prev = 1
up = False
speed = 0.4
speed_incr = 0.034
lvl = 1

while lvl <= 10:
    #obstackles
    for i in range(lvl + 3):
        pos1 = random.randint(5, 90)
        s[pos1] = '*'
        pos2 = random.randint(10, 95)
        if abs(pos1 - pos2) > 3: s[pos2] = '_'
        else: s[pos2 + 3] = '_'

    key = msvcrt.getch()
   
    if key == b'w' or key == b'W':
        up = True
    elif key == b's' or key == b's':
        up = False
    elif key == b'q' or key == b'Q':
        break

    for i in range(2, 102):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'w' or key == b'W': up = True
            elif key == b's' or key == b's': up = False

        s[prev] = ' '
        if up:
            s[i] = '->'
        else:
            s[i] = '|'
        prev = i
        
        print(''.join(s), i-1, '% of lvl {0:d} / 10 complete  '.format(lvl),  end='\r', flush=True)
        time.sleep(speed)

        if (s[i] == '->' and s[i+1] == '_') or (s[i] == '|' and s[i+1] == '*'):
            print('\nOops you lose !!!')
            quit(0)
        

    lvl += 1
    if speed > 0:
        speed -= speed_incr
   