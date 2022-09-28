import sys
import heapq as  hq
sys.stdin=open("input.txt", "r")

def D(L, sum, tsum):
  global result
  if sum > C:
    return 
  if tot - tsum + sum < result:
    return 

  if L == N:
    if sum > result:
      result = sum
  else:
    D(L+1, sum + dogs[L], tsum + dogs[L])
    D(L+1, sum, tsum + dogs[L])
    
C, N = map(int, input().split())
dogs = []
for i in range(N):
  dogs.append(int(input()))
tot = sum(dogs)
result = -1
D(0, 0, 0)
print(result)
