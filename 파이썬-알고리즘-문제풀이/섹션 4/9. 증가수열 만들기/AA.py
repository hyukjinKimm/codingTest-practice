import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
nums = list(map(int, input().split()))


result = []
last = -1
lt= 0 
rt = N-1
while lt <= rt:
  n1 = nums[lt]
  n2 = nums[rt]
  tmp =[]
  if n1 > last:
    tmp.append([n1, 'L'])
  if n2 > last:
    tmp.append([n2, 'R'])
  tmp.sort()
  if len(tmp) == 0:
    break
  else:
    result.append(tmp[0][1])
    last = tmp[0][0]
    if tmp[0][1] == 'L':
      lt += 1
    else:
      rt -= 1
 

print(len(result))
for x in result:
  print(x, end = '')

