import sys
#sys.stdin=open("input.txt", "r")



def Count(dist): # dist 이상으로 말을 배치했을때 배치가능한 말의 수 
  cnt = 1 
  p = point[0]
  for i in range(1, N):
    if point[i] - p >= dist:
      cnt += 1
      p = point[i]
  return cnt

N, C = map(int, input().split())
point = []
for i in range(N):
  point.append(int(input()))
point.sort()

lt = 1 
rt = point[N-1] -  point[0]
while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= C:
    res = mid 
    lt = mid + 1 
  else:
    rt = mid - 1

print(res)