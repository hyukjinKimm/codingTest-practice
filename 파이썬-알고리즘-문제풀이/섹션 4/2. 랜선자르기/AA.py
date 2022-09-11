import sys
#sys.stdin=open("input.txt", "r")

def Count(x): # x만큼 으로 잘랐을때 몇개의 라인이 나오나? 
  cnt = 0
  for l in line:
    cnt += l // x 
  return cnt
K, N = map(int, input().split())
line = []
for i in range(K):
  line.append(int(input()))


lt = 1
rt = max(line)
res = -1
while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= N:
    res = mid 
    lt = mid + 1
  else:
    rt = mid - 1
print(res)