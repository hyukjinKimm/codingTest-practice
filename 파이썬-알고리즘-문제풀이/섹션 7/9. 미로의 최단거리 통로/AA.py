import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, P):
  global result
  
  if n[L] == -1 :
    result += 1
    for i in range(P):
      print(chr(res[i] + 64), end = '')
    print()
  else:
    for i in range(1, 27): # 1 ~ 26 
      if i < 10:
        if n[L] == i :
          res[P] = i 
          d(L+1, P+1)
      else:
        if n[L+1] != -1 and n[L] == i // 10 and n[L+1] == i % 10 :
          res[P] = i 
          d(L+2, P+1)

   

arr = [list(map(int, input().split())) for _ in range(7)]
ch = [[0] * 7 for  _ in range(7)]
ch[0][0] = 1 
q = deque()
q.append((0, 0, 0))
dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]
while q:
  a, b, d = q.popleft()
  for j in range(4):
      x = a + dx[j]
      y = b + dy[j]
      if 0 <= x < 7 and 0 <= y  <7 and ch[x][y] == 0 and arr[x][y] == 0:
        q.append((x, y, d+1))
        ch[x][y] = 1
        if x == 6 and y == 6:
          print(d+1)
          sys.exit()
print(-1)
