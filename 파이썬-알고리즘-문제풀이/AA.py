from optparse import BadOptionError
import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
graph = [[0]*n for _ in range(n)]
degree = [0] * n
for _ in range(n):
  a, b = map(int, input().split())
  graph[a-1][b-1] = 1
  degree[b-1] += 1
q = deque()
for i in range(n):
  if degree[i] == 0 :
    q.append(i)

while q:
  now = q.popleft()
  print(now+1, end=' ')
  for i in range(n):
    if graph[now][i] == 1:
      degree[i] -= 1
      if degree[i] == 0:
        q.append(i)
