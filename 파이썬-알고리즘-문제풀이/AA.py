import sys

sys.stdin=open("input.txt", "r")


def dfs(x):
  if x > N:
    for i in range(1, N+1):
      if ch[i] == 1:
        print(i, end = ' ')
    print()
  else:
    ch[x] = 1
    dfs(x+1)
    ch[x] = 0 
    dfs(x+1)


N = int(input())
ch = [0] * (N+1)
dfs(1)



