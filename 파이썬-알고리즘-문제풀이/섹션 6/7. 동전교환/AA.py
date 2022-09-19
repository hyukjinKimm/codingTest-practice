import sys

#sys.stdin=open("input.txt", "r")


def dfs(summ, cnt):
  global res
  if cnt > res:
    return
  if summ > M:
    return
  if summ == M:
    if cnt < res:
      res = cnt 
  else:
    for i in range(N):
      dfs(summ + coins[i], cnt+1)


    

N = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
M = int(input())
res = float('inf')
dfs(0, 0)
print(res)



