import sys
from collections import deque
from itertools import permutations
import heapq as hq
sys.stdin=open("input.txt", "r")

def d(L, P):
  global result
  
  if n[L] == -1 :
    result += 1
    for i in range(P):
      print(chr(res[i] + 64), end = '')
    print()
  else:
    for i in range(1, 27): # 1 ~ 26 
      if i < 10:
        if n[L] == i :
          res[P] = i 
          d(L+1, P+1)
      else:
        if n[L+1] != -1 and n[L] == i // 10 and n[L+1] == i % 10 :
          res[P] = i 
          d(L+2, P+1)

   
n = list(map(int, input()))
n.append(-1)
res = [0] * 50
result = 0
d(0, 0)
print(result)