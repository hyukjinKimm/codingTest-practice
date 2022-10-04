import sys
from collections import deque
from itertools import permutations
import heapq as hq
sys.stdin=open("input.txt", "r")

def d(P):
  ch[P] = True
 
  global cnt
  if P == n-1:
    cnt += 1
  
  else:
    for i in range(n):
      if graph[P][i] == 1 and ch[i] == False: 
        ch[i] = True
        d(i)
        ch[i] = False
      
     
  

    
      
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for i in range(m):
 a, b = map(int, input().split())
 graph[a-1][b-1] = 1
ch = [False] * n 
cnt = 0
d(0)
print(cnt)