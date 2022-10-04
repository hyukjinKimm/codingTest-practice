import sys
from collections import deque
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, sum):
  if L == n:
    if tot - sum == sum:
      print('YES')
      sys.exit()
  else:
    d(L+1, sum + arr[L])
    d(L+1, sum)
    


n = int(input())
arr = list(map(int, input().split()))
tot = sum(arr)
d(0, 0)
print('NO')