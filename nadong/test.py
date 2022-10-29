
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, visited):
  sum = 0
  tmp = []
  queue = deque([(x, y)])
  while queue:
    a, b = queue.popleft()
    tmp.append((a, b))
    sum += board[a][b]
    for k in range(4):
      xx = a + dx[k]
      yy = b + dy[k]
      if 0 <= xx < n and 0 <= yy < n:
        if visited[xx][yy] == False:
          if r <= abs(board[a][b] - board[xx][yy]) <= l:
            queue.append((xx, yy))
            visited[xx][yy] = True
  for x, y in tmp:
    board[x][y] = sum // len(tmp)
    

def check():
    for x in range(n):
      for y in range(n):
        for k in range(4):
          xx = x + dx[k]
          yy = y + dy[k]
          if 0 <= xx < n and 0 <= yy < n:
            if r <= abs(board[x][y] - board[xx][yy]) <= l:
              return False 
    return True
n, r, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def main():
  cnt = 0
  if check():
    print(0)
    return 

  while True:
    cnt += 1
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
      for y in range(n):
        if visited[x][y] == False:
          visited[x][y] = True
          bfs(x, y, visited)

    if check():
      print(cnt)
      return
      


        

  
    
    
    

  
 

    
  

  
if __name__ == "__main__":
  main()
