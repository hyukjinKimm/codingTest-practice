import sys
#sys.stdin=open("input.txt", "r")
N = int(input())
scores = list(map(int, input().split()))
ave = int(sum(scores) / N + 0.5)

res = -1
res_score = -1
diff = float('inf')
for i in range(N):
  if abs(scores[i] - ave) < diff:
    diff = abs(scores[i] - ave)
    res = i 
    res_score = scores[i]
  else:
    if abs(scores[i] - ave) == diff:
      if scores[i] > res_score:
        res = i 
        res_score = scores[i]
    
print(ave, res+1)