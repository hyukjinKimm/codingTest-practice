import sys
import heapq as  hq
sys.stdin=open("input.txt", "r")

def D(L, s, sum):
  global cnt
  if L == K:
    if sum % M == 0 :
      cnt += 1
  else:
    for i in range(s, N):
      D(L+1, i+1, sum+arr[i])

    
N, K = map(int, input().split())
arr = list(map(int, input().split()))
M = int(input())
cnt = 0
D(0, 0, 0)
print(cnt)
