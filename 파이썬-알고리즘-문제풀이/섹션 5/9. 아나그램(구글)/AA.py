import sys
from collections import deque

#sys.stdin=open("input.txt", "r")

N1 = input()
N2 = input()
a1 = [0] * 52 
a2 = [0] * 52 


for i in range(len(N1)):
  if N1[i].isupper():
    a1[ord(N1[i])-65] += 1
  else:
    a1[ord(N1[i])-71] += 1

  if N2[i].isupper():
    a2[ord(N2[i])-65] += 1
  else:
    a2[ord(N2[i])-71] += 1

for i in range(52):
  if a1[i] != a2[i]:
    print('NO')
    break 
else:
  print('YES')