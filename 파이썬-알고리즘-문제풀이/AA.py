import sys
import heapq as  hq
sys.stdin=open("input.txt", "r")

def D(L, sum):
  if L == n:
    if tot - sum == sum:
      print('YES')
      sys.exit()
  else:
    D(L+1, sum + number[L])
    D(L+1, sum)
    

n = int(input())
number = list(map(int, input().split()))
tot = sum(number)
D(0, 0)
print('NO')