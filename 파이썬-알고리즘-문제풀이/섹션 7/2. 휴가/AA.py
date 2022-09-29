import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L, sum):
  global result 
  if L == N + 1:
    if sum > result:
      result = sum 
  else:
    if L+T[L] <= N + 1: 
      D(L+T[L], sum + P[L])
    D(L+1, sum)

    
N = int(input())
T = []
P = []
for i in range(N):
  a, b = map(int, input().split())
  T.append(a)
  P.append(b)
T.insert(0, 0)
P.insert(0, 0)
result = 0 
D(1, 0)
print(result)