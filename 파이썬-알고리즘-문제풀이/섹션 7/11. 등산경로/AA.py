import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(P):
  global cnt
  a, b = P
  if a == e[0] and b ==  e[1]:
    cnt += 1
    return
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < N and 0 <= y < N and mapp[x][y] > mapp[a][b] and ch[x][y] == 0:
      ch[x][y] = 1
      DFS((x, y))
      ch[x][y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]



N = int(input())
mapp = [list(map(int, input().split())) for _ in range(N)]
ch = [[0] * N for _ in range(N)]
cnt = 0
minn = float('inf')
maxx = -1
for i in range(N):
  for j in range(N):
    if mapp[i][j] < minn:
      minn = mapp[i][j]
      s = (i, j)
    if mapp[i][j] > maxx:
      maxx = mapp[i][j]
      e = (i, j)
ch[s[0]][s[1]] = 1
DFS(s)
print(cnt)