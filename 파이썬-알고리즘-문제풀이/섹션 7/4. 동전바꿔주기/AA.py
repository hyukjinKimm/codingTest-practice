import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, sum):
  global result
  if sum > T:
    return
  if L == N:
    if sum == T:
      result += 1
  else:
    for i in range(n[L] + 1): 
      d(L+1, sum + i*c[L])

   
  
T = int(input())
N = int(input())
c = []
n = []
for _ in range(N):
  a, b= map(int, input().split())
  c.append(a)
  n.append(b)
result = 0
d(0, 0)
print(result)