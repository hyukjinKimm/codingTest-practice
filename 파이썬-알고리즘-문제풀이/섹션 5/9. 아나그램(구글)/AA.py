import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N1 = input()
N2 = input()
ch1 = [0] * 52


for i in range(len(N1)):
  if N1[i].isupper():
    ch1[ord(N1[i])-65] += 1
  else:
    ch1[ord(N1[i])-71] += 1
  if N2[i].isupper():
    ch1[ord(N2[i])-65] -= 1 
  else:
    ch1[ord(N2[i])-71] -= 1


if ch1.count(0) != 52:
  print('NO')
else:
  print('YES')
  

