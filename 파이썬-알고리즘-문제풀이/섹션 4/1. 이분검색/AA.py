import sys
#sys.stdin=open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
lt = 0
rt = N - 1
while lt <= rt :
  mid = (lt + rt) // 2
  if M == arr[mid]:
    print(mid+1)
    break
  elif M > arr[mid]:
    lt = mid + 1
  else:
    rt = mid - 1 
