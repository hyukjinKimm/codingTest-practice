import sys
sys.stdin=open("input.txt", "r")

def Count(x): # x만큼 잘랐을때 나오는 라인의 갯수 
  cnt = 0 
  for l in line:
    cnt += l // x 
  return cnt


K, N = map(int, input().split())
line = []
for i in range(K):
  line.append(int(input()))
line.sort()
lt = 1 
rt = line[K-1]

res = -1
while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= N :
    res = mid
    lt = mid +1 
  else:
    rt = mid - 1
print(res)
