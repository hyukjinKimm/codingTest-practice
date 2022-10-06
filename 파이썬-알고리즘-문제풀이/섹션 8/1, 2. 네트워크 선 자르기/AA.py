import sys
from collections import deque
from itertools import combinations
import heapq as hq
#sys.stdin=open("input.txt", "r")
def d(x):
  if f[x] != 0:
    return f[x]
  else:
    f[x] = d(x-1) + d(x-2)
    return f[x]
n = int(input())
f = [0]*(n+1)
f[1] = 1
f[2] = 2
print(d(n))
