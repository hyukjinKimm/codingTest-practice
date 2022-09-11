import sys
#sys.stdin=open("input.txt", "r")
N = int(input())
arr = list(map(int ,input().split()))
result = [0] * (N+1)

for i in range(N):
  z = 0
  for j  in range(1, N + 1):
    if arr[i] == 0 and result[j] == 0:
      result[j] = i+1
      break
    if result[j] == 0:
      z += 1
      arr[i] -= 1
for i in range(1, N+1):
  print(result[i], end = ' ')

  
    