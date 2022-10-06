import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)
#sys.stdin=open("input.txt", "r")
def d(a, b):
  
  if dy[a][b] != 0:
    return dy[a][b]
  else:
    if a == 0:
      dy[0][b] = d(0, b-1) + board[0][b]
      return dy[0][b]
    elif b == 0:
      dy[a][0] = d(a-1, 0) + board[a][0]
      return dy[a][0]
    else:
      dy[a][b] = min( d(a-1, b) , d(a,b-1)) + board[a][b]
      return dy[a][b]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)] 
dy[0][0] = board[0][0]

print(d(n-1, n-1))