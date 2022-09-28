import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(L, s):
  global cnt
  if L == M:
    for x in res:
      print(x, end = ' ')
    print()
    cnt += 1
    return
  else:
    for i in range(s, N):
      res[L] = i+1
      D(L+1, i+1)

    
N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
res = [0] * M
cnt = 0
D(0, 0)
print(cnt)