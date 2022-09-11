import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
gotgams = [list(map(int, input().split())) for _ in range(N)]
M  = int(input())
orders = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
  a, b, c = orders[i]
  if b == 0:
    for j in range(c):
      gotgams[a-1].append(gotgams[a-1].pop(0))
  else:
    for j in range(c):
      gotgams[a-1].insert(0, gotgams[a-1].pop(N-1))
s = 0
e = N - 1
summ = 0
for i in range(N):
  summ += sum(gotgams[i][s:e+1])
  if i < N // 2:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1
print(summ)