import sys
from itertools import permutations

def D(x, s):
  global cnt
  if x >= k:
    if sum(res) % m == 0:
      cnt += 1
  else:
    for i in range(s, n):
      res[x] = arr[i]
      D(x+1, i+1)
     

n, k = map(int, input().split())
res = [0] * k 
arr = list(map(int, input().split()))
m = int(input())
cnt = 0
def main():
  D(0, 0)
if __name__ == '__main__':
  main()
  print(cnt)

