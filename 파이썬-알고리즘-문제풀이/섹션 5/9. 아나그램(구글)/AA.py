import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N1 = input()
N2 = input()
p = dict()

for i in range(len(N1)):
  p[N1[i]] = p.get(N1[i], 0) + 1 
  p[N2[i]] = p.get(N2[i], 0) - 1 
  

for key, val in p.items():
  if val != 0:
    print('NO')
    break
else:
  print('YES')