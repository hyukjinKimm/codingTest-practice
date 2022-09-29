import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

def DFS(L):
  global minn
  if L == N:
    diff = max(ABC) - min(ABC)
    if diff >= minn:
        return
    else:
      tmp = set()
      for i in range(3):
        tmp.add(ABC[i])
      if len(tmp) == 3:
        diff = max(tmp) - min(tmp)
        if diff < minn:
          minn = diff
  
      
  else:
    for i in range(3):
      ABC[i] += coin[L]
      DFS(L+1)
      ABC[i] -= coin[L]
N = int(input())
coin = []
minn = float('inf')
for i in range(N):
  coin.append(int(input()))
ABC = [0] * 3
DFS(0)
print(minn)