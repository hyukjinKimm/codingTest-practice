import sys
#sys.stdin=open("input.txt", "r")
from collections import deque
n = int(input())
arr = list(map(int, input().split()))
ch = [0] * n 
for i in range(n):

  for j in range(n):
    if ch[j] == 0 and arr[i] == 0:
      ch[j] = i+1
      break
    elif ch[j] == 0:
      arr[i] -= 1
      
for x in ch:
  print(x, end= ' ')