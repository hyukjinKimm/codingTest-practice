import sys
sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
number = list(map(int, input().split()))

lt = 0 
rt = 1
res = number[0]
cnt = 0 

while True:
  if res == M:
    cnt += 1 
    res -= number[lt]
    lt += 1
  elif res < M:
    if rt >= N:
      break
    else:
      res += number[rt]
      rt += 1
  elif res > M:
    res -= number[lt]
    lt += 1

print(cnt)