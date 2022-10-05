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

   
n, e= list(map(int, input().split()))
q = deque()
q.append((n, 0))
ch = [0] * 10001
ch[n] = 1
while True:
  now, d = q.popleft()
  for x in [now+1, now-1, now+5]:
    if 0 < x < 10001:

      if ch[x] == 0:
        ch[x] = 1
        q.append((x, d+1))
        if x == e:
          print(d+1)
          sys.exit()
