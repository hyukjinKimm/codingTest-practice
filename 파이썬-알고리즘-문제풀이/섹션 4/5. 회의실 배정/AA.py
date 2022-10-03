import sys
#sys.stdin=open("input.txt", "r")
import bisect
n = int(input())
se = []

for _ in range(n):
  a, b = map(int, input().split())
  se.append((a, b))
se.sort(key=lambda x : x[1])

endtime  = se[0][1]
cnt = 1
for value in se[1:]:
  if value[0] >= endtime:
    cnt += 1
    endtime = value[1]
print(cnt)