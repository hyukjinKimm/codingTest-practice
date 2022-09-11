import sys
#sys.stdin=open("input.txt", "r")
def digit_sum(x):
  res = 0
  while x > 0:
    res += x % 10
    x = x // 10
  return res



N = int(input())
numbers = list(map(int, input().split()))
maxx = -1
for n in numbers:
    if digit_sum(n) > maxx:
      maxx = digit_sum(n)
      res = n
print(res)