import sys
#sys.stdin=open("input.txt", "r")
n = int(input())
arr = list(map(int, input().split()))
res = 0
before = 0
for c in arr:

  if c == 1:
    res += (before + 1) 
    before += 1
  else:
    before = 0
print(res)