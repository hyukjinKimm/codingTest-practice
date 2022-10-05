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

   
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for  _ in range(n)]
ch[n//2][n//2] = 1 
q = deque()
q.append((n//2, n//2))
cnt = arr[n//2][n//2]
dx = [-1, 0, 1, 0]
dy = [0 ,1, 0, -1]
L = 0

while True:
  if L == n//2:
    break
  size = len(q)
  for i in range(size):
    a, b = q.popleft()
    for j in range(4):
       x = a + dx[j]
       y = b + dy[j]
       if ch[x][y] == 0:
        q.append((x, y))
        cnt += arr[x][y]
        ch[x][y] = 1
  L += 1
print(cnt)