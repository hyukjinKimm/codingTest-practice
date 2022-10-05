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
     

 

   
n = int(input())
aarr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]
q = deque()
maxx = -1
for r in range(101):
  arr = aarr.copy()
  for i in range(n):
    arr[i] = aarr[i].copy()  
  cnt = 0
  for i in range(n):
    for j in range(n):
      if arr[i][j] > r:
        arr[i][j] = 0
        q.append((i, j))
        cnt += 1 
        while q:
          a, b = q.popleft()
          for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and arr[x][y] > r:
              arr[x][y] = 0
              q.append((x, y))
        if cnt > maxx:
          maxx = cnt
print(maxx)