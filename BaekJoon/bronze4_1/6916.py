# 6916

import sys

n = int(sys.stdin.readline())
num = {0:[" * * *"]+['*     *']*3+['']+['*     *']*3+[' * * *'],
       1:['']+['      *']*3+['']+['      *']*3+[''],
       2:[' * * *']+['      *']*3+[' * * *']+['*']*3+[' * * *'],
       3:[' * * *']+['      *']*3+[' * * *']+['      *']*3+[' * * *'],
       4:['']+['*     *']*3+[' * * *']+['      *']*3+[''],
       5:[' * * *']+['*']*3+[' * * *']+['      *']*3+[' * * *'],
       6:[' * * *']+['*']*3+[' * * *']+['*     *']*3+[' * * *'],
       7:[' * * *']+['      *']*3+['']+['      *']*3+[''],
       8:[' * * *']+['*     *']*3+[' * * *']+['*     *']*3+[' * * *'],
       9:[' * * *']+['*     *']*3+[' * * *']+['      *']*3+[' * * *']}

for line in num[n]:
    print(line)
