import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(P):
  global cnt
  a, b = P
  if a == 6 and b ==  6:
    cnt += 1
    return
  for i in range(4):
    x = a + dx[i]
    y = b + dy[i]
    if 0 <= x < 7 and 0 <= y < 7 and mapp[x][y] == 0:
      mapp[x][y] = 1
      DFS((x, y))
      mapp[x][y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]



mapp = [list(map(int, input().split())) for _ in range(7)]
ch = [[0] * 7 for _ in range(7)]
cnt = 0
mapp[0][0] = 1
DFS((0, 0))
print(cnt)