# 25304

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
cal = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cal += a*b

if (x == cal):
    print("Yes")
else:
    print("No")
