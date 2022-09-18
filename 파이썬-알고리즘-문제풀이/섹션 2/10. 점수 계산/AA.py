import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
score = list(map(int, input().split()))

before = 0 
res = 0

for i in range(N):
  if score[i] == 1:
   
    before += 1
    res += before
  else:
    before = 0 
print(res)