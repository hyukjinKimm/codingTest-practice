from optparse import BadOptionError
import sys
from collections import deque
from itertools import combinations
import heapq as hq
sys.setrecursionlimit(10**6)


def bin(x):
  if x == 1: print(1,end='')
  else:
    bin(x//2)
    print(x%2, end='')

n = int(input())

bin(n)