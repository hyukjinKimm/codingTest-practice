import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque([[arr[i], i] for i in range(N)])
cnt = 0

maxx = -1
while True:
  p = arr.popleft()
  if any(p[0] < arr[i][0] for i in range(len(arr))):
    arr.append(p)
  else:
    cnt += 1
    if p[1] == M:
      print(cnt)
      break


