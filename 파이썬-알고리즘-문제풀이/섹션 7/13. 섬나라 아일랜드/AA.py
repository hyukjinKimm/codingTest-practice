import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(P, h):
  a, b = P
  ch[a][b] = 1
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < N and 0 <= y < N and mapp[x][y] > h and ch[x][y] == 0:
      DFS((x, y), h)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]



N = int(input())
mapp = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
cnt = 0
for i in range(N):
  for j in range(N):
    if mapp[i][j] == 1:
      cnt += 1
      mapp[i][j] = 0 
      Q.append((i, j))
      while Q:
        a, b = Q.popleft()
        for k in range(8):
          x = a + dx[k]
          y = b + dy[k]
          if 0 <= x < N and 0 <= y < N and mapp[x][y] == 1:
            mapp[x][y] = 0
            Q.append((x, y))
      
print(cnt)