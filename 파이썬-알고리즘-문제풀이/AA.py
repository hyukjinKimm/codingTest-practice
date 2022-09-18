import sys
sys.stdin=open("input.txt", "r")

N =int(input())
spec = []
for i in range(N):
  spec.append(list(map(int, input().split())))

spec.sort(reverse=True)
largest = - 1
cnt = 0
for i in range(N):
  if spec[i][1] > largest:
    cnt += 1
    largest = spec[i][1]
print(cnt)