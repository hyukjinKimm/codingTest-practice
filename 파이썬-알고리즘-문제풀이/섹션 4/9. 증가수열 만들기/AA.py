import sys
#sys.stdin=open("input.txt", "r")
N = int(input())
arr = list(map(int ,input().split()))

result = []
last = -1
while True:
  tmp = []
  if arr[0] > last:
    tmp.append((arr[0], 'L'))
  if arr[-1] > last:
    tmp.append((arr[-1], 'R'))
  if len(tmp) == 0:
    break
  tmp.sort()
  if tmp[0][1] == 'L':
    result.append('L')
    arr.pop(0)
  else:
    result.append('R')
    arr.pop()
  last = tmp[0][0]

print(len(result))
for i in result:
  print(i, end= '')
