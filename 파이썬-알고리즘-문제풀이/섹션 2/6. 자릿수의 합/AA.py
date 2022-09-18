import sys
#sys.stdin=open("input.txt", "r")
N, M = map(int, input().split())

ch = [0] * (N + M + 1)

for n in range(1, N+1):
  for m in range(1, M+1):
    ch[n+m] += 1
maxx = max(ch)
for i in range(2, N+M+1):
  if ch[i] == maxx:
    print(i, end = ' ')
