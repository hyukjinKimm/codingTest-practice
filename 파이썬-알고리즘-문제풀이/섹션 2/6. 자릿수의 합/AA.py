import sys
#sys.stdin=open("input.txt", "r")

def digit_sum(x):
  res = 0
  while x > 0:
    res += x % 10
    x /= 10
  return res

N = int(input())
number = list(map(int ,input().split()))
maxx = -1
res = -1
for i in range(N):
  if digit_sum(number[i]) > maxx:
    res = i 
print(number[res])
