import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

c1 = [0] * 52
c2 = [0] * 52
N1 = input()
N2 = input()

for i in range(len(N1)):
  if N1[i].isupper():
    c1[ord(N1[i]) - 65] += 1
  else: 
    c1[ord(N1[i]) - 71] += 1

  if N2[i].isupper():
    c2[ord(N2[i]) - 65] += 1
  else: 
    c2[ord(N2[i]) - 71] += 1
for i in range(52):
  if c1[i] != c2[i]:
    print('NO')
    break   
else:
  print('YES')