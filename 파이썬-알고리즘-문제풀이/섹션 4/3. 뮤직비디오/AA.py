import sys
#sys.stdin=open("input.txt", "r")

def Count(capacity): # capacity 만큼일때 필요한 DVD 갯수 
  cnt = 1 
  p = music[0]
  for i in range(1, N):
    p += music[i]
    if p > capacity:
      cnt += 1
      p = music[i]
  return cnt


N, M = map(int, input().split())
music = list(map(int, input().split()))

res = -1
while lt <= rt:
  mid = (lt + rt) // 2

  if Count(mid) <= M:
    res = mid 
    rt = mid -1 
  else:
    lt = mid + 1

print(res)