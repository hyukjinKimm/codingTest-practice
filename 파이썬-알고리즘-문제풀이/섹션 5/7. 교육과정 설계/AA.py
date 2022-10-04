import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N = input()
k = int(input())
for o in range(k):
  need = deque(N) 
  time = deque(input())
  for i in range(len(time)):
    t = time[i]
    if t in need:
      n = need.popleft()
      if t != n:
        print(f'#{o+1} NO')
        break 
  else:
    if need:
        print(f'#{o+1} NO')
    else:
        print(f'#{o+1} YES')
  