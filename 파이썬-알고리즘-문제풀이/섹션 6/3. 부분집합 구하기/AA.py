import sys
from collections import deque
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L):
  if L == n  :
    for i in range(n):
      if res[i] == 1:
        print(i+1, end = ' ')
    print()
  else:
    res[L] = 1
    d(L+1)
    res[L] = 0
    d(L+1)
    


n = int(input())
res = [0] * n
d(0)