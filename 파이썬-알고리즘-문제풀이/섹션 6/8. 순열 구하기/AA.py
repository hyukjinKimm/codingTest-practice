import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L):
  global cnt
  if L == m: 
    cnt += 1
    for x in res:
      print(x, end=  ' ')
    print()

  else:
    for i in range(n):
      if ch[i] == 0:
        ch[i] = 1
        res[L] = i+1
        d(L+1)
        ch[i] = 0
  

    
      
n, m = map(int, input().split())
b = [1] * n 
for i in range(1, n):
  b[i] = b[i-1] * (n-i) // i 

arr = [i+1 for i in range(n)]
for x in permutations(arr):
  sum = 0
  for i in range(n):
    sum += b[i] * x[i]
  if sum == m:
    for j in x:
      print(j, end = ' ')
    sys.exit()
