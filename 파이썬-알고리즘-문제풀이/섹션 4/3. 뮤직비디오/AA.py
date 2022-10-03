import sys
#sys.stdin=open("input.txt", "r")
import bisect
n, m = map(int, input().split())
music = list(map(int, input().split()))
lt = max(music)
rt = sum(music)

def Count(x): # x만큼 용량이면 DVD 몇장 나오는지? 
  tmp = 0
  cnt = 1  
  for m in music:
    tmp += m 
    if tmp > x:
      cnt += 1
      tmp = m 

  return cnt
    

while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) > m: 
    lt = mid + 1 
  else: 
    ans = mid 
    rt = mid - 1 
print(ans)