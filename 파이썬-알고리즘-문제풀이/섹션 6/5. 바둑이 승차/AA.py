import sys

#sys.stdin=open("input.txt", "r")


def dfs(x, summ, tsum):
  global result
  if tot - tsum + summ < result:
    return
  if C < summ:
    return
  if x >= N:
    if summ > result:
      result = summ
  else:
    dfs(x+1, summ + dogs[x], tsum + dogs[x])
    dfs(x+1, summ, tsum  + dogs[x])

    


C, N = list(map(int, input().split()))
dogs = []
result = -1
for i in range(N):
  dogs.append(int(input()))
dogs.sort(reverse=True)
tot = sum(dogs)
dfs(0 ,0, 0)
print(result)



