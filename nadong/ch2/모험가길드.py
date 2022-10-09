import sys
sys.stdin=open("input.txt", "r")
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
cnt = 0
result = 0 
i = 0 
while i < n :
  cnt += 1
  if cnt >= arr[i]:
    result += 1
    cnt = 0 
  i += 1
print(result)

