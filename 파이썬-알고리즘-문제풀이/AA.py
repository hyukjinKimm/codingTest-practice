import sys
sys.stdin=open("input.txt", "r")
from collections import deque
n = int(input())
arr = deque(list(map(int, input().split())))


ans = ''
last = -1
while True:
  tmp = []

  if arr and last < arr[0]:
    tmp.append((arr[0], 'L'))
  if arr and last < arr[-1]:
    tmp.append((arr[-1], 'R'))
  if len(tmp) == 0:
    break 

  tmp.sort()
  if tmp[0][1] == 'L':
    ans += 'L'
    arr.popleft()
  else:
    ans += 'R'
    arr.pop()
  last = tmp[0][0]
print(ans)