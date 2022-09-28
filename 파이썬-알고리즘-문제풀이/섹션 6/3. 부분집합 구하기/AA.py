import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L):
  if L == n+1:
    for i in range(1, n+1):
      if res[i] == 1:
        print(i, end=' ')
    print()
  else:
    res[L] = 1
    D(L+1)
    res[L] = 0
    D(L+1)

n = int(input())
res = [0] * (n+1)
D(1)