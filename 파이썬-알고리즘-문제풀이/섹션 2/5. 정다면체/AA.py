import sys
#sys.stdin=open("input.txt", "r")


N, M = map(int ,input().split())
arr1 = [i + 1 for i  in range(N)]
arr2 = [i + 1 for i  in range(M)]

ch = [0] * (N+M+1)  # ~ch[N+M]
for a in arr1:
  for b in arr2:
    idx = a + b 
    ch[idx] += 1
maxx = (max(ch))

for i in range(N+M+1):
  if ch[i] == maxx:
    print(i, end=' ')