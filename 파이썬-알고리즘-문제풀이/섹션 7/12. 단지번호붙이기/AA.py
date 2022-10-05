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
arr = [list(map(int, input())) for _ in range(n)]

ch = [[False] * n for  _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]
res=[]
q = deque()
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      arr[i][j] = 0
      cnt = 1
      d(i, j)
      res.append(cnt)
print(len(res))
print(sorted(res))
