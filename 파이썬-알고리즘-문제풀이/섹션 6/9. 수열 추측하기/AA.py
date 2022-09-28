import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L):
  global cnt
  if L == N:
    sum = 0
    for i in range(N):
      sum += b[i] * res[i]
    if sum == F:
      for x in res:
        print(x, end = ' ')
      sys.exit()
  else:
    for i in range(1, N+1):
      if ch[i] == 0:
        ch[i] = 1
        res[L] = i 
        D(L+1)
        ch[i] = 0

    
N, F = map(int, input().split())
arr = [i+1 for i in range(N)]
b = [1] * N
for i in range(1, N):
  b[i] = b[i-1] * (N-i) // i
ch = [0] * (N+1)
res = [0] * N 
D(0)
