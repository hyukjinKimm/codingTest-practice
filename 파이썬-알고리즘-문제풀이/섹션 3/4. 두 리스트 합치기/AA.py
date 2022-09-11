import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
nrr = list(map(int, input().split()))
M = int(input())
mrr = list(map(int , input().split()))

n = 0
m = 0
result = []
while n < N and m < M:
  if nrr[n] >mrr[m]:
    result.append(mrr[m])
    m += 1
  else:
    result.append(nrr[n])
    n += 1
if n < N:
  result = result + nrr[n: ]
else:
  result = result + mrr[m:]
for i in result:
  print(i, end = ' ')
