import sys
from collections import deque
from itertools import product
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L):
  global cnt
  if L == m:
    cnt += 1
    for x in res:
      print(x, end = ' ')
    print()
  else:
    for i in range(n): # i 0 - 2
      res[L] = i+1
      d(L+1)
      
n, m = map(int, input().split())
cnt = 0
res = [0] * m 
d(0)
print(cnt)