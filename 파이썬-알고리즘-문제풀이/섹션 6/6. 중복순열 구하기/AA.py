import sys

#sys.stdin=open("input.txt", "r")


def dfs(index):
  global cnt
  if index == M:
    for x in res:
      print(x, end = ' ')
    cnt += 1
    print()
    return
  else:
    for i in range(1, N+1):
      res[index] = i
      dfs(index + 1)

    


N, M = list(map(int, input().split()))
res = [0]*(M)
cnt = 0
dfs(0)
print(cnt)



