import sys

#sys.stdin=open("input.txt", "r")


def dfs(L):
  global cnt
  if L == M:
    for x in res:
      print(x, end = ' ')
    print()
    cnt += 1
  else:
    for i in range(1, N+1):
      if ch[i] == 0:
        ch[i] = 1
        res[L] = i
        dfs(L+1)
        ch[i] = 0
    


N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
ch = [0] * (N+1)
res = [0]*M
cnt = 0
dfs(0)
print(cnt)

