import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(a, b):
  global cnt

  for i in range(4):
    x = a + dx[i]
    y = b  + dy[i]
    if 0 <=x < n and 0 <=y<n and arr[x][y] == 1:
      arr[x][y] = 0
      cnt += 1
      d(x, y)
     

 

   
n, m = list(map(int, input().split()))

aarr = [list(map(int, input().split())) for _ in range(m)]
q = deque()
for i in range(m):
  for j in range(n):
    if aarr[i][j] == 1:
      q.append((i, j, 0))


dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]

lastd = -1
while q:
  a, b, d = q.popleft()
  lastd = d
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < m and 0 <= y < n and aarr[x][y] == 0:
      aarr[x][y] = 1
      q.append((x, y, d+1))
   
for i in range(m):
  for j in range(n):
    if aarr[i][j] == 0:
      print(-1)
      sys.exit()
else:
  print(lastd)      