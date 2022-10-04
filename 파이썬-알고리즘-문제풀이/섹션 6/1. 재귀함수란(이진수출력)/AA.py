import sys
from collections import deque
import heapq as hq
#sys.stdin=open("input.txt", "r")

def b(x):
  if x == 0:
    return
  else:
    b(x//2)
    print(x%2,end='')

n = int(input())
b(n)