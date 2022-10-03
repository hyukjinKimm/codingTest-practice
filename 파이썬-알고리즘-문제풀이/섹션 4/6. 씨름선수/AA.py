import sys
#sys.stdin=open("input.txt", "r")
import bisect
n = int(input())
spec = []
for _ in range(n):
  spec.append(list(map(int, input().split())))
spec.sort(reverse=True)
largest = spec[0][1]
cnt = 1
for i in range(1, n):
  if spec[i][1] > largest:
    cnt += 1
    largest = spec[i][1]
print(cnt)