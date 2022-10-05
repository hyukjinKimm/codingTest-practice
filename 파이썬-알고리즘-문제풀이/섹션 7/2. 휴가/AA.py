import sys
from collections import deque
from itertools import permutations
import heapq as hq
# sys.stdin=open("input.txt", "r")

def d(L, sum):
  global result
  if L == n+1:
    if sum > result:
      result = sum
  else:
    if L + t[L] <= n+1:
      d(L+t[L], sum + p[L])
    d(L+1, sum)
     
  

n = int(input())
t = [0]
p = [0]
for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)
result = - 1
d(1, 0)
print(result)
