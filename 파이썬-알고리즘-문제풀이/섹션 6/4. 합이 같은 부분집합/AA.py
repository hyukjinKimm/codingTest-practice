import sys

#sys.stdin=open("input.txt", "r")


def dfs(x, summ):
  if x >= N:
    if (tot - summ) == summ:
      print('YES')
      sys.exit()
  else:
    dfs(x+1, summ + arr[x])
    dfs(x+1, summ)
    


N = int(input())
arr = list(map(int, input().split()))
tot = sum(arr)
ch = [0] * (N+1)
dfs(0, 0)
print('NO')



