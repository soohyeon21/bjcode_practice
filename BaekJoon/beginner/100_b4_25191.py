# 25191

import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
beverage = a//2 + b

print(min(n, beverage))
