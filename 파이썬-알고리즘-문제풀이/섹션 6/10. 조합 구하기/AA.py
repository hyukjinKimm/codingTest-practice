import sys
from itertools import permutations


def D(x, s):
  global cnt
  if x >= k:
    for i in res:
      print(i, end = ' ')
    print()
    cnt += 1
  else:
    for i in range(s, n):
      res[x] = i+1
      D(x+1, i+1)
     

n, k = map(int, input().split())
res = [0] * k 
cnt=0
def main():
  D(0, 0)
  print(cnt)
if __name__ == '__main__':
  main()

