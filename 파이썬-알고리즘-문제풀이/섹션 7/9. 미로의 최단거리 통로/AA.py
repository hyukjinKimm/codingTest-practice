import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(P):
  global minn
  a, b = P
  if a == 6 and b ==  6:
    if dis[6][6] < minn:
      minn = dis[6][6]
    return
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < 7 and 0 <= y < 7 and mapp[x][y] == 0:
      dis[x][y] = dis[a][b] + 1
      mapp[x][y] = 1
      DFS((x, y))
      mapp[x][y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]


mapp = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
Q = deque()
mapp[0][0] =1
Q.append((0, 0))
while Q:
  a, b = Q.popleft()
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < 7 and 0 <= y < 7 and mapp[x][y] == 0:
      mapp[x][y] = 1
      dis[x][y] = dis[a][b] + 1
      Q.append((x, y))
if dis[6][6] == 0:
  print(-1)
else:
  print(dis[6][6])
