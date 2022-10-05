import sys
from collections import deque
from itertools import permutations
import heapq as hq
sys.stdin=open("input.txt", "r")

def d(a, b):
  global cnt
  ch[a][b] = True
  if a == maxp[0] and b == maxp[1]:
    cnt += 1 

  else:
    for i in range(4):
      x = a + dx[i]
      y = b  + dy[i]
      if 0 <=x < n and 0 <=y<n and ch[x][y] == False and arr[x][y] > arr[a][b]:
        d(x, y)
        ch[x][y] = False
  
 

   
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minn = float('inf')
maxx = -1
for i in range(n):
  for j in range(n):
    if arr[i][j]  < minn:
      minn = arr[i][j]
      minp = (i, j)
    if arr[i][j]  > maxx:
      maxx = arr[i][j]
      maxp = (i, j)

ch = [[False] * 7 for  _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]
cnt=0
d(minp[0], minp[1])
print(cnt)