import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)
#sys.stdin=open("input.txt", "r")

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [float('inf')] * (m+1) # 돈이 i 일때 최소 동전 갯수 
dy[0] = 0
for i in range(n):
  for j in range(coin[i], m+1):
    dy[j] = min(dy[j-coin[i]] + 1 , dy[j])
print(dy[m])

