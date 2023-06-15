# 25206

import sys

nxg = 0
nsum = 0
table = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}
for _ in range(20):
    cname, num, grade = sys.stdin.readline().split()
    if (grade != "P"):
        nxg += float(num)*table[grade]
        nsum += float(num)

print(nxg/nsum)
