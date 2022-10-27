<<<<<<< HEAD

import sys
from collections import deque
sys.stdin=open("C:\github\codingTest-practice\\nadong\input.txt", "r")

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def D(x):
  global cnt, visited
  visited[x] = 1
  cnt += 1
  for v in graph[x]:
    if visited[v] == 0:
      D(v)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
res = -1
cnt = 0
visited = [0] * (n+1)
for i in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

def main():
  global cnt, res, visited
  ch = [0] * (n+1)
  for i in range(1, n+1):
    cnt = 0
    visited = [0] * (n+1)
    D(i)
    print(visited)
    ch[i] = cnt
    res = max(cnt, res)

  for i in range(1, n+1):
    if ch[i] == res:
      print(i, end = ' ')
=======
import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

ch = [0] * (n+1)

def DFS(x):
  print(x, end = ' ')
  for i in range(n+1):
    if graph[x][i] == 1 and ch[i] == 0:
      ch[i] = 1 
      DFS(i)


def main():
  ch[v] = 1
  DFS(v)
  

  arr = deque()


      
>>>>>>> 7e7474cdab5c2dca98d6b1b67555e7bb69c8982d
if __name__ == "__main__":
  main()
