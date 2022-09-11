import sys
#sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()
cnt = 0 
summ = 0 

while len(weight) > 0:
  if len(weight) == 1:
    cnt += 1
    weight.pop()
    break
  elif weight[0] + weight[-1] <= M:
    cnt += 1
    weight.pop()
    weight.pop(0)
  else:
    weight.pop()
    cnt  += 1

print(cnt)
