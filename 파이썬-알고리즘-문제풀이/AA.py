import sys
sys.stdin=open("input.txt", "r")
N, M = map(int,  input().split())
d = dict()
for i in range(1, N+1):
  for j in range(1, M+1):
    d[i+j] = d.get(i+j, 0) + 1 
maxx = max(d.values())
for k, v in d.items():
  if v == maxx:
    print(k, end = ' ')