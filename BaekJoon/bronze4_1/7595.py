# 7595

import sys

while (1):
    num = int(sys.stdin.readline())
    if (num == 0):
        break

    for i in range(1, num+1):
        print("*"*i)
