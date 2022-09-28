import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L):
  global cnt
  ch[L] = 1
  global cnt
  if L == N:
    cnt += 1
  else:
    for i in range(1, N+1):
      if ch[i] == 0:
        if mapp[L][i] == 1:
          D(i)
          ch[i] = 0

    
N, M = map(int, input().split())
mapp = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  mapp[a][b] = 1
ch = [0] * (N+1)
cnt = 0
D(1)
print(cnt)