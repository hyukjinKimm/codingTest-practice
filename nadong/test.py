
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
if __name__ == "__main__":
  main()
