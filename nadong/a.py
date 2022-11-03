import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs(x, d):
  global sum
  queue = deque([(x, d)])
  while queue:
    node, d = queue.popleft()
    for v in grap[node]:
      if visited[v] == 0:
        queue.append((v, d+1))
        visited[v] = 1
        dist[v] = d+1
def dfs(x):
  global sum
  for v in grap[x]:
    if visited[v] == 0:
      visited[v] = 1
      dist[v] = dist[x] + 1
      dfs(v)
 
        


n = int(input())
grap = [[] for _ in range(n+1)]
visited = [0] * (n+1)
dist = [0] * (n+1)

for i in range(n-1):
  a, b = map(int, input().split())
  grap[a].append(b)
  grap[b].append(a)
 

def main():
  sum = 0
  visited[1] = 1
  dfs(1)

  for i in range(2, n+1):
    if len(grap[i]) == 1:
      sum += dist[i]

  if sum % 2 == 0:
    print('No')
  else:
    print('Yes')
  




if __name__ == "__main__":
    main()