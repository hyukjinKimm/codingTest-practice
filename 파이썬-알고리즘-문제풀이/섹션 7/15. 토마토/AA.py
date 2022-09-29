import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def D(P):
  a, b = P
  ch[a][b] = 1
  if a == 0:
    print(b)
    sys.exit()
  else:
    for i in range(3):
      x = a + dx[i]
      y = b + dy[i]
      if 0 <= x < 10 and 0 <= y < 10 and ch[x][y] == 0 and board[x][y] == 1:
        D((x, y))


Q = deque()
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
dis = [[0] * M for _ in range(N)]
for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      Q.append((i, j))
while Q:
  a, b = Q.popleft()
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < N and 0 <= y < M and box[x][y] == 0 :
      box[x][y] = 1
      Q.append((x, y))
      dis[x][y] = dis[a][b] + 1 

maxx = -1
for i in range(N):
  for j in range(M):
    if box[i][j] == 0:
      print(-1)
      sys.exit()
    if dis[i][j] > maxx:
      maxx = dis[i][j]
print(maxx)
  