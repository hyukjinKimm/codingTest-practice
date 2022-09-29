import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(L, sum):
  global cnt
  if sum > T:
    return 

  if L == K:
    if sum == T:
      cnt += 1
    return
  else:
    for i in range(n[L] + 1):
      DFS(L+1, sum + i * p[L])


T = int(input())
K = int(input())
p = []
n = []

for i in range(K):
  a, b = map(int, input().split())
  p.append(a)
  n.append(b)
cnt = 0
DFS(0, 0)
print(cnt)