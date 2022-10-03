import sys
#sys.stdin=open("input.txt", "r")
N, M = map(int,  input().split())
res = [0] * (N+M+1)

for i in range(1, N+1):
  for j in range(1, M+1):
    res[i+j] += 1
maxx = max(res)
for i in range(2, N+M+1):
  if res[i] == maxx:
    print(i, end = ' ')