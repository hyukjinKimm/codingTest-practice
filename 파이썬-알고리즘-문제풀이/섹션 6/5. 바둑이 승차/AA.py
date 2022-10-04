import sys
from collections import deque
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, sum, tsum):
  global result
  if sum > c:
    return
  if tot - tsum + sum < result:
    return 
  if L == n:
    if result < sum:
      result = sum 
  else:
    d(L+1, sum + dog[L], tsum + dog[L])
    d(L+1, sum, tsum + dog[L])
    
    

c, n = map(int, input().split())
dog = []
for _ in range(n):
  dog.append(int(input()))
tot = sum(dog)
result = -1
d(0, 0, 0)
print(result)