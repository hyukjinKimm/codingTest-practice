from optparse import BadOptionError
import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)

def D(x):
  if x >= n+1:
    for i in range(1, n+1):
      if res[i] == 1:
        print(i, end=' ')
    print()
  else:
    res[x] = 1
    D(x+1)
    res[x] = 0
    D(x+1)
  

n = int(input())
res = [0] * (n+1)

def main():
  D(1)

if __name__ == '__main__':
  main()

