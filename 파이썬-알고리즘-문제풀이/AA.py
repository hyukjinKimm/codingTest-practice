import sys
import heapq as  hq
sys.stdin=open("input.txt", "r")

def D(L, sum):
  global cnt
  if L > cnt:
    return
  if sum > money:
    return
  if sum == money:
    if L < cnt:
      cnt = L
  else:
    for i in range(N):
      D(L+1, sum + coin[i])
    
N = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)
money = int(input())
cnt = float('inf')
D(0, 0)
print(cnt)