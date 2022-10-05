import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, ssum, tsum):
  global result
  if L == n:
    if tsum > m:
      return
    else:
      if ssum > result:
        result = ssum
  else:
    d(L+1, ssum+s[L], tsum + t[L])
    d(L+1, ssum, tsum)
      
     
  

    
      
n, m = map(int, input().split())
s = []
t= [ ]
for i in range(n):
  a, b = map(int, input().split())
  s.append(a)
  t.append(b)
result = -1
d(0, 0, 0)
print(result)