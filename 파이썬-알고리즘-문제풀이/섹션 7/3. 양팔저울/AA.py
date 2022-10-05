import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, sum):
  global result
  if L == n:
    if sum > 0:
      result.add(sum)
    return     
  d(L+1, sum + w[L])
  d(L+1, sum - w[L])
  d(L+1, sum )
    
  

n = int(input())
w = list(map(int, input().split()))
result = set()

d(0, 0)
print(sum(w) - len(result))