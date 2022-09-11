import sys
#sys.stdin=open("input.txt", "r")
def reverse(x):
  res = 0
  while x > 0:
    res = res*10 + x % 10
    x = x // 10
  return res

def isPrime(x):
  if x == 1:
    return False
    
  for i in range(2, x):
    if x % i == 0:
      return False
  else:
    return True
N = int(input())
nums = list(map(int ,input().split()))

for n in nums:
  tmp = reverse(n)
  if isPrime(tmp):
    print(tmp, end = ' ')