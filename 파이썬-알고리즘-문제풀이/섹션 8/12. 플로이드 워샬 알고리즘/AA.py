from optparse import BadOptionError
import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)
#sys.stdin=open("input.txt", "r")

n = int(input())
board = [[float('inf')] * n for _ in range(n)]
for i in range(n):
  board[i][i] = 0
while True:

  a, b = map(int, input().split())
  if a == -1 and b == -1:
    break 
  
  board[a-1][b-1] = 1
  board[b-1][a-1] = 1 
for k in range(n):
  for i in range(n):
    for j in range(n):
      board[i][j] = min(board[i][k] + board[k][j], board[i][j])

minn = float('inf')
for i in range(n):
  board[i] = max(board[i])
  minn = min(board[i], minn)
res = []
for i in range(n):
  if board[i] == minn:
    res.append(i+1)
print(minn, len(res))
for x in res:
  print(x, end = ' ')
