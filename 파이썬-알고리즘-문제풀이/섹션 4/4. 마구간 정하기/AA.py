import sys
#sys.stdin=open("input.txt", "r")
import bisect
n, m = map(int, input().split())
p = []
for _ in range(n):
  p.append(int(input()))
p.sort()
lt = 1
rt = p[n-1]

def Count(dist): # dist이상 길이로 배치하면 말 몇마리 배치 가능?
  cnt = 1  
  mark = p[0]
  for x in p[1:]:
    if x - mark >= dist:
      mark = x 
      cnt += 1
  return cnt
    

while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= m: 
    lt = mid + 1
    ans = mid
  else: 
    rt = mid - 1
print(ans)