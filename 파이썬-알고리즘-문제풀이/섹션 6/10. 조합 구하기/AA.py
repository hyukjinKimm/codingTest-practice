import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, s):
  global cnt
  if L == m:
   cnt += 1
   for x in res:
    print(x, end = ' ')
   print()
  
  else:
    for i in range(s, n):
      res[L] = i+1 
      d(L+1, i+1)
     
  

    
      
n, m = map(int, input().split())
res = [0] * m 
cnt = 0
d(0, 0)
print(cnt)