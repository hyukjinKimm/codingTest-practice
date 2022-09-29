import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(P):
  global cnt
  a, b = P
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < N and 0 <= y < N and mapp[x][y] == 1:
      mapp[x][y] = 0
      cnt += 1
      DFS((x, y))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]



N = int(input())
mapp = [list(map(int, input())) for _ in range(N)]
Q = deque()
res = []
for i in range(N):
  for j in range(N):
    if mapp[i][j] == 1:
      cnt = 1
      mapp[i][j] = 0 
      DFS((i, j))
      res.append(cnt)
      
res.sort()
print(len(res))
for x in res:
  print(x)