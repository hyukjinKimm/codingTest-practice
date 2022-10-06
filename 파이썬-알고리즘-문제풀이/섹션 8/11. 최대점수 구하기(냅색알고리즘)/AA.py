import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
s = []
t = []
for _ in range(n):
  a, b = map(int, input().split())
  s.append(a)
  t.append(b)
dy = [0] * (m+1)
for i in range(n):
  for j in range(m, t[i]-1, -1):
    dy[j] = max(dy[j-t[i]] + s[i], dy[j])
print(dy[m])
