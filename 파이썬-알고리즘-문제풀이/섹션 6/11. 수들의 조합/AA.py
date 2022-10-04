import sys
from collections import deque
from itertools import permutations
import heapq as hq
#sys.stdin=open("input.txt", "r")

def d(L, s):
  global cnt
  if L == k:
   if sum(res) % m == 0:
    cnt+= 1
  
  else:
    for i in range(s, n):
      res[L] = arr[i] 
      d(L+1, i+1)
     
  

    
      
n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
res = [0] * k
cnt = 0
d(0, 0)
print(cnt)