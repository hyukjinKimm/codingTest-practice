import sys
from bisect import bisect_left, bisect_right
from itertools import combinations, product
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

def check(n, jw, x): # 질투심 x 로 n명에게 보석을 전부 나눠줄수 있는가? 
  if len(jw) > n:
    return False 







def main():
  n, m = map(int, input().split())
  jw = []
  for _ in range(m):
    jw.append(int(input()))
  jw.sort()
  res = 0
  lt = 1
  rt = sum(jw)
  while lt<=rt:
    mid = (lt+rt) // 2
    if check(n, jw, mid):
      res = mid 
      rt = mid - 1
    else:
      lt = mid + 1
  print(res)

if __name__ == "__main__":
    main()