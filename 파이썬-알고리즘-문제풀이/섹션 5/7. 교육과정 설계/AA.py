import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

need = input()
N = int(input())
for i in range(N):
  needd = deque(need)
  cur = input()
  for j in range(len(cur)):
    if cur[j] in needd:
      n = needd.popleft()
      if cur[j] != n:
        print('#%d NO' %(i+1))
        needd.appendleft(n)
        break
  else:
    if len(needd) != 0:
      print('#%d NO' %(i+1))
    else:
      print('#%d YES' %(i+1))
