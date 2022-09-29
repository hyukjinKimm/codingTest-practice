import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(L, P):
  global cnt
  if L == len(N)-1:
    cnt += 1
    for c in res[:P]:
      print(chr(c+64), end= '')
    print()

  else:
    for i in range(1, 26):
      if i < 10 and N[L] == i:
        res[P] = i 
        DFS(L+1, P+1)
      elif  10 <= i  and N[L+1] != -1 and N[L] == i // 10 and N[L+1] == i % 10:
        res[P] = 10 * N[L]  + N[L+1]
        DFS(L+2, P+1)
N = list(map(int, input()))
N.append(-1)
res = [0] * len(N)
cnt = 0
DFS(0, 0)
print(cnt)