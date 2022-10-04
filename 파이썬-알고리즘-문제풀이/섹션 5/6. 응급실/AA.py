import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = deque([(arr[i], i) for i in range(n)])
cnt = 0 
while True:
  x = arr.popleft()
  if all(arr[i][0] <= x[0] for i in range(len(arr))):
    cnt += 1
    if k == x[1]:
      print(cnt)
      break 
  else: 
    arr.append(x)
