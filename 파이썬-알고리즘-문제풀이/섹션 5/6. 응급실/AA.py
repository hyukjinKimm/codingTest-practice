import sys
from collections import deque

#sys.stdin=open("input.txt", "r")
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = [[arr[i], i] for i in range(N)]
arr = deque(arr)
cnt = 0
while True:
  p = arr.popleft()
  for i in range(len(arr)):
    if p[0] < arr[i][0]:
      arr.append(p)
      break 
  else:
    cnt += 1
    if p[1] == M:
      print(cnt)
      sys.exit()
