import sys
#sys.stdin=open("input.txt", "r")


N = int(input())
scores = list(map(int, input().split()))
ave = int(sum(scores) / N + 0.5)

minn = float('inf')
res_score = - 1
res = -1
for i in range(N):
  if abs(scores[i] - ave) < minn: # 평균에 더 가까우면 
    minn = abs(scores[i] - ave)
    res_score = scores[i]
    res = i + 1 
  elif abs(scores[i] - ave) == minn:
    if scores[i] > res_score:
      res_score = scores[i]
      res = i + 1 

print(ave, res)