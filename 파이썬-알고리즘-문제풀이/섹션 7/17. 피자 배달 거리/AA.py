import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L, s):
  global result

  if L == M:
    sum = 0 
    for i in range(len(hs)):
      tmp = []
      x1, y1 = hs[i]
      for j in range(len(pz)):
        if ch[j] == 1:
          x2, y2 = pz[j]
          dist = abs(x1-x2) + abs(y1-y2)
          tmp.append(dist)
      sum += min(tmp)
    if sum < result:
      result = sum
    
  else:
    for i in range(s, len(pz)):
      if ch[i] == 0:
        ch[i] = 1
        D(L+1, i+1)
        ch[i] = 0

N, M = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(N)]

pz = []
hs = []
for i in range(N):
  for j in range(N):
    if mapp[i][j] == 2:
      pz.append((i, j))
    elif mapp[i][j] == 1:
      hs.append((i, j))
result = float('inf')


ch = [0] * (len(pz))
D(0, 0)
print(result)
