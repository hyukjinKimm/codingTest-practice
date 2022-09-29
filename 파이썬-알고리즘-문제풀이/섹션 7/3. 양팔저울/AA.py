import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L, sum):
 
  if L == N:
    if sum > 0:
      res.add(sum)
  else:
    D(L+1, sum + weight[L])
    D(L+1, sum)
    D(L+1, sum - weight[L]) 
    

    
N = int(input())
weight = list(map(int, input().split()))
res = set()
D(0, 0)
print(sum(weight) - len(res))