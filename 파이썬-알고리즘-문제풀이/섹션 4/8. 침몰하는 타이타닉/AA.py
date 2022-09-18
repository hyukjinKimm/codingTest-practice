import sys
#sys.stdin=open("input.txt", "r")
from collections import deque

N, M = map(int, input().split())
passenger = list(map(int, input().split()))
passenger.sort()
cnt = 0
arr = deque(passenger)
while len(arr) > 0:
  if len(arr) == 1:
    cnt += 1
    break 
  p1 = arr.popleft()
  p2 = arr.pop()
  if p1 + p2 <= M:
    cnt += 1
  else:
    arr.appendleft(p1)
    cnt += 1
print(cnt)