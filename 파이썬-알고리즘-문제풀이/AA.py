import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.stdin=open("input.txt", "r")
n = int(input())
arr = list(map(int, input().split()))
dy = [0] * n 
dy[0] = 1 
for i in range(2, n):
  for j in range(i):
    if arr[j] < arr[i]:
      dy[i] = max(dy[j], dy[i])
  dy[i] += 1
print(arr)
print(dy)
maxx = -1

for i in range(n):
  maxx = max(dy[i], maxx)
print(maxx)
