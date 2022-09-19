import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque([[arr[i], i] for i in range(N)])
cnt = 0

maxx = -1
while True:
  maxx = max(arr)
  p = arr.popleft()
  if maxx[0] <= p[0]:
    cnt += 1
    if p[1] == M:
      print(cnt)
      break
  else:
    arr.append(p)

