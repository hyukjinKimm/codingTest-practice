import sys
#sys.stdin=open("input.txt", "r")

def Count(capacity): # capacity 만큼으로 용량을 잡았을때 몇개면 모든 노래를 담을 수 있나?? 
  summ = 0
  cnt = 1
  for m in music:
    summ += m 
    if summ > capacity:
      cnt += 1
      summ = m
  return cnt


N, M = map(int, input().split())
music = list(map(int, input().split()))
lt = 1
rt = sum(music)
minn = min(music)
while lt <= rt:
  mid = (lt + rt) // 2
  if (mid >= minn and Count(mid) <= M):
    rt = mid - 1
    res = mid 
  else:
    lt = mid + 1
print(res)