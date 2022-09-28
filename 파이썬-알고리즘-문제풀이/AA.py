import sys
import heapq as  hq
sys.stdin=open("input.txt", "r")

def D(L):
  global cnt
  if L == M:
   for x in res:
    print(x, end = ' ')
   print()
   cnt += 1
  else:
    for i in range(N):
      if ch[i] == 0:
        ch[i] = 1
        res[L] = i+1
        D(L+1)
        ch[i] = 0

    
N, M = map(int, input().split())
res = [0] * M 
ch = [0] * N
cnt = 0
D(0)
print(cnt)