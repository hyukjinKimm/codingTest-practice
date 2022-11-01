import queue
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x):
  global d
  visited[x] = 1 
  ch[x] = d
  d += 1
  for v in grap[x]:
    if visited[v] == 0:
        dfs(v)
    
d = 1
n, m, x = map(int, input().split())
grap = [[] for _ in range(n+1)]
edge = []
visited = [0]*(n+1)
ch = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    edge.append([a, b])
edge.sort(key=lambda x: (x[0], x[1]))
for i in range(m):
  a, b = edge[i]
  grap[a].append(b)
  grap[b].append(a)

    
cnt = 0 
def main():
  dfs(x)
  for c in ch[1:]:
    print(c)
         


if __name__ == "__main__":
    main()