import sys
from itertools import permutations

def D(x):

  if x >= n:
    tot = 0
    for i in range(n):
      tot += b[i] * res[i]
    if tot == k:
      for x in res:
        print(x, end = ' ')
      sys.exit()

  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1 
        res[x] = i
        D(x+1)
        ch[i] = 0

n, k = map(int, input().split())
res = [0] * k 

def main():
  D(0, 0)

  


if __name__ == '__main__':
  main()

