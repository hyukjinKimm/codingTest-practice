import sys
from collections import deque

#sys.stdin=open("input.txt", "r")
Need = list(input())
N = int(input())
for i in range(N):
  need = deque(Need.copy())
  time = input()
  for j in range(len(time)):
    if time[j] in need:
      first = need.popleft()
      if first != time[j]:
        print("#%d NO" %(i+1))
        break 
  else:
    if len(need) != 0:
      print("#%d NO" %(i+1))
    else:
      print("#%d YES" %(i+1))  
