import sys
import heapq as  hq
#sys.stdin=open("input.txt", "r")

def D(n):
  if n == 0:
    return 
  else:
    D(n//2)
    print(n%2, end = '')

n = int(input())
D(n)