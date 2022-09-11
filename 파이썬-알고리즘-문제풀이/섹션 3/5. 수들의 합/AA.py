import sys
#sys.stdin=open("input.txt", "r")

N, M = list(map(int, input().split()))
numbers = list(map(int, input().split()))
lt = 0
rt = 1
summ = 0
cnt = 0

while True:
  summ = sum(numbers[lt:rt])
  if M  <= summ :
    cnt += 1
    summ -= numbers[lt]
    lt += 1
  elif summ < M:
    rt += 1
  if rt >= N:
    if summ < M:
      break 
print(cnt)