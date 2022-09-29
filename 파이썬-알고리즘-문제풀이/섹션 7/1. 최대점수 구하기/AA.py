import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L, time, profit):
  global result 
  if time > M:
    return 

  if L == N:
    if profit > result:
      result = profit
  else:
    D(L+1, time + t[L], profit + p[L])
    D(L+1, time , profit)

    
N, M = map(int, input().split())
t = []
p = []
for i in range(N):
  a, b = map(int, input().split())
  t.append(b)
  p.append(a)
result = 0 

D(0, 0, 0)
print(result)