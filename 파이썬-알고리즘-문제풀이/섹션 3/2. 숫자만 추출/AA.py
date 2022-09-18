import sys
#sys.stdin=open("input.txt", "r")

N = input()
res = 0
for n in N:
  if n.isdecimal():
    res = res*10 + int(n)
  
cnt = 0 
for i in range(1, res+1):
  if res % i == 0:
    cnt += 1
print(res)
print(cnt)
