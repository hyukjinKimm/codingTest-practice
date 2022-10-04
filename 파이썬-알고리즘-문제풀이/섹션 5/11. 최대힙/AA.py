import sys
from collections import deque
import heapq as hq
#sys.stdin=open("input.txt", "r")


arr = []
while True:
  n = int(input())
  if n == -1:
    break 
  elif n == 0:
    if len(arr) == 0:
      print(-1)
    else:
      print(-hq.heappop(arr))
  else:
    hq.heappush(arr, -n)

