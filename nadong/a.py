import queue
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(x, y):
  board[x][y] = 0
  queue = deque([(x, y)])
  while queue:
    a, b = queue.popleft()
    for i in range(8):
      xx = a + dx[i]
      yy = b + dy[i]
      if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 1:
        queue.append((xx, yy))
        board[xx][yy] = 0

def dfs(x, y):
  board[x][y] = 0
  for i in range(8):
    xx = x + dx[i]
    yy = y + dy[i]
    if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 1:
      dfs(xx, yy)
    
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

def main():
  cnt  = 0
  for i in range(m):
    for j in range(n):
      if board[i][j] == 1:
        cnt += 1
        dfs(i, j)
  print(cnt)


if __name__ == "__main__":
    main()