import sys
sys.stdin=open("input.txt", "r")
s = input()

# 연산하는 두 수중 0 또는 1 이 있다면 더하는게 최선 ! 
result = int(s[0])
for i in range(1, len(s)):
  data = int(s[i])
  if data <= 1 or result <= 1:
    result += data 
  else:
    result *= data 
