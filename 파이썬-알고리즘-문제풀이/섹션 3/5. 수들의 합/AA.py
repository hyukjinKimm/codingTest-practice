import sys
#sys.stdin=open("input.txt", "r")
n, k = map(int, input().split())
arr = list(map(int, input().split()))

lt = 0
rt = lt + 1 
sum = arr[lt]
cnt = 0
while True:
  if sum == k:
    cnt += 1
    sum -= arr[lt]
    lt += 1
  elif sum > k:
    sum -= arr[lt]
    lt += 1
  else:
    if rt == n:
      break 
    else:
      sum += arr[rt]
      rt += 1
print(cnt)