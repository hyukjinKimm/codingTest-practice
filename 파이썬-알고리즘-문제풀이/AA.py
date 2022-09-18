import sys
sys.stdin=open("input.txt", "r")

N = int(input())
nums = list(map(int, input().split()))

ch = [0] * (N)

for i in range(N):

  for j in range(N):
    if nums[i] == 0 and ch[j] == 0:
      ch[j] = i+1
      break
    elif ch[j] == 0:
      nums[i] -= 1
      continue 
for i in ch:
  print(i, end=' ')
