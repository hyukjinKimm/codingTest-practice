import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(a, b):
  global cnt

  ch[a][b] = True
  if a == 0:
    print(b)
    sys.exit()
     
  else:
    for i in range(3):
      x = a + dx[i]
      y = b + dy[i]
      if 0 <= x < 10 and 0 <= y < 10 and board[x][y] == 1 and ch[x][y] == False:
       
        d(x, y)

 


board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]  *10 for _ in range(10)]
dx = [0, 0, -1]
dy = [-1, 1, 0]
for k in range(10):
  if board[9][k] == 2:
    d(9, k)