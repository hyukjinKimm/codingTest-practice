import sys
#sys.stdin=open("input.txt", "r")
def digit_sum(x):
  res = 0
  while x > 0:
    res += x % 10
    x = x // 10
  return res
N = int(input())
arr = list(map(int, input().split()))
minn = -1
res = 0
for a in arr:
  ss = digit_sum(a)
  if ss > minn:
    minn = ss 
    res = a 
print(res)
