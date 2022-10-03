import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

lt = 0
rt = n - 1
cnt = 0
while lt <= rt:

  if lt == rt:
    cnt += 1
    break 
  elif weight[lt] + weight[rt] <= m:
    cnt += 1
    lt += 1
    rt -= 1
  else:
    cnt += 1
    rt -= 1
print(cnt)
    
  
  