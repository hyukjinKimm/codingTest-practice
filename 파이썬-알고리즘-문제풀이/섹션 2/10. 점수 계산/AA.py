import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
scores = list(map(int, input().split()))
acc = 0
tot = 0

for i in range(N):
  if scores[i] == 1:
    acc += 1
    tot += acc 
  else: 
    acc = 0
print(tot)