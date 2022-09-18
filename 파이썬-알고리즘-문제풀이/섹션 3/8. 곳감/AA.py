import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
order = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
  a, b, c = order[i]

  if b == 0:
    for _ in range(c):
      arr[a-1].append(arr[a-1].pop(0))
  else:
    for _ in range(c):
      arr[a-1].insert(0, arr[a-1].pop())

s = 0 
e = N - 1 
summ = 0
for i in range(N):
  summ += sum(arr[i][s:e+1])
  if i < N//2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1
print(summ)

