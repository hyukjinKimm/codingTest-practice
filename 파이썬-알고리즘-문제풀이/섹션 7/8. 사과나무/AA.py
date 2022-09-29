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


N = int(input())
mapp = [list(map(int, input().split())) for _ in range(N)]

Q = deque()
Q.append((N//2, N//2))
cnt = mapp[N//2][N//2]
ch = [[0] * N for _ in range(N)]
ch[N//2][N//2] = 1
L = 0
while True:
  if L == N//2:
    break
  size = len(Q)
  for j in range(size):
    a, b = Q.popleft()
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]
      if 0 <= x < N and 0 <= y < N and ch[x][y] == 0:
        ch[x][y] = 1
        cnt += mapp[x][y]
        Q.append((x, y))
  L += 1

print(cnt)