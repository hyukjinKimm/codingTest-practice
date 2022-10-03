import sys
#sys.stdin=open("input.txt", "r")
import bisect
N, K = map(int, input().split())
line = []
for _ in range(N):
  line.append(int(input()))
lt = 1
rt = max(line)
ans = -1

def Count(x):
  cnt = 0 
  for l in line:
    cnt += l // x
  return cnt
while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= K:
     ans = mid 
     lt = mid + 1 
  else:
    rt = mid - 1
print(ans)