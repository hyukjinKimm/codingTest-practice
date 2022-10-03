import sys
#sys.stdin=open("input.txt", "r")
N = int(input())
score = list(map(int, input().split()))
ave = int(sum(score) / N + 0.5 ) 
diff = float('inf')

res = 0
res_score = 0
for i, s in enumerate(score):
  tmpDiff = abs(s - ave)
  if tmpDiff  < diff:
    diff = tmpDiff
    res = i + 1 
    res_score = s
  elif tmpDiff == diff:
    if s > res_score: # 지금 보는 점수가 이전의 점수보다 크면
      res = i+1
      res_score = s 
print(ave, res)

    