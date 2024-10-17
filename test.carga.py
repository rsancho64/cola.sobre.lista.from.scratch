#! /usr/bin/python3

from cola import cola
import random

c = cola(20)

tries = 0
while tries < 100:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        print('enqueu...')
        dice = random.randint(1, 6)
        try:
            c.enqueue(dice)
            print(c)
        except:
            pass
    if coin == 2:
        print('dequeu...')
        try:
            data = c.dqueue()
            print(data)
        except:
            pass

total = tries
print(total)