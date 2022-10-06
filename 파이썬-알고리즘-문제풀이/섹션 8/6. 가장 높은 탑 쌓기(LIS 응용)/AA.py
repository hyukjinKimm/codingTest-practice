import sys
from collections import deque
from itertools import combinations
import heapq as hq
#sys.stdin=open("input.txt", "r")
n = int(input())
info = []
for i_ in range(n):
  info.append(list(map(int, input().split())))
info.sort()
dy = [0] * n
dy[0] = info[0][1]
for i in range(1, n):
  for j in range(i):
    if info[j][2] < info[i][2]:
      dy[i] = max(dy[i], dy[j])
  dy[i] += info[i][1]
maxx=  - 1
for i in range(n):
  maxx = max(dy[i], maxx)
print(maxx)