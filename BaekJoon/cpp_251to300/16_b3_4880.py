# 4880

import sys

while (1):
    a1, a2, a3 = map(int, sys.stdin.readline().split())
    if (a1 == 0 and a2 == 0 and a3 == 0):
        break

    if (a2-a1 == a3-a2):
        print("AP", a3*2 - a2)
    elif (a2/a1 == a3/a2):
        print("GP", a3*(a3//a2))
