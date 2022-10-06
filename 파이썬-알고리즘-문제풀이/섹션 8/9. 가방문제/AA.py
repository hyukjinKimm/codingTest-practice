import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
v = []
w = []
dy = [0]  *(m+1)
for _ in range(n):
  a, b = map(int, input().split())
  w.append(a)
  v.append(b)

for i in range(n):
  for j in range(w[i], m+1):
    dy[j] = max(dy[j-w[i]] + v[i], dy[j])

print(dy[m])