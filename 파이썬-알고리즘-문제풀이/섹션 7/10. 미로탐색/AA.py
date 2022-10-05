import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(a, b):
  global cnt
  ch[a][b] = True
  if a == 6 and b == 6:
    cnt += 1 

  else:
    for i in range(4):
      x = a + dx[i]
      y = b  + dy[i]
      if 0 <=x < 7 and 0 <=y<7 and ch[x][y] == False and arr[x][y] == 0:
        d(x, y)
        ch[x][y] = False
  
 

   

arr = [list(map(int, input().split())) for _ in range(7)]
ch = [[False] * 7 for  _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]
cnt=0
d(0, 0)
print(cnt)