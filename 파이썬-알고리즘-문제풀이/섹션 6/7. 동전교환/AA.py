import sys
from collections import deque
from itertools import product
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, sum):
  global result
  if L >= result:
    return 
  if sum > m:
    return 
  if sum == m:
    if L < result:
      result = L 
      return 
    
  else:
    for c in coin:
      d(L+1, sum + c)

      
n = int(input())
coin = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
result = 1000
d(0, 0)
print(result)