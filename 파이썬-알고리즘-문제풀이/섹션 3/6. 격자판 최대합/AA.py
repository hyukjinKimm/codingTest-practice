import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]



maxx = -1
for i in range(N):
  sum1 = sum2 = 0
  sum1 = sum(arr[i])
  for j in range(N):
    sum2 += arr[j][i]
  if sum1 > maxx:
    maxx = sum1 
  if sum2 > maxx:
    maxx = sum2 
sum1 = sum2 = 0
for i in range(N):
  sum1 +=arr[i][i]
  sum2 += +arr[i][N-i-1]

if sum1 > maxx:
  maxx = sum1 
if sum2 > maxx:
  maxx = sum2 
print(maxx)
