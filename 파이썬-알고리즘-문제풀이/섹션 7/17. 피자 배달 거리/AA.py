import sys
from collections import deque
from itertools import combinations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, s):
    global result
    if L == m:
      sum = 0
      for h in hs:
        minn = float('inf')
        for x in res:
          minn = min(minn, abs(h[0] - pz[x][0]) + abs(h[1] - pz[x][1]))
        sum += minn 
      if sum < result:
        result = sum
    else:
        for i in range(s, len(pz)):
            res[L] = i
            d(L+1, i+1)

n, m  = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
pz = []
hs = []
for i in range(n):
    for j in range(n):
        if p[i][j] == 2:
            pz.append((i, j))
        if p[i][j] == 1:
            hs.append((i, j))
res = [0] * m
result = float('inf')
d(0, 0)
print(result)

