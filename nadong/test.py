import sys
sys.stdin=open("input.txt", "r")
def count(x): # x로 이루어진 덩어리 갯수를 찾느다 .
  p = -1 
  cnt = 0
  for i in range(len(s)):
    if s[i] == x:
        p = i  
    else:
      if p != -1:
        cnt += 1
        p = - 1
  else:
      if p != -1:
        cnt += 1

  return cnt
s = list(map(int, input()))
res1 = count(0)
res2 = count(1)
if res1 >= res2:
    print(res2)
else:
    print(res1)
