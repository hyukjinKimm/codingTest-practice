import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
maxx = -1
for i in range(n):
  a, b, c = sorted(list(map(int, input().split())))
  if a == b and b == c:
    money = 10000 + a*1000
  elif a == b:
    money = 1000 + a*100
  elif b == c:
    money = 1000 + b*100
  else:
    money = c * 100
  
  if money > maxx:
    maxx = money
  
print(maxx)