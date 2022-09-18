import sys
sys.stdin=open("input.txt", "r")
T = int(input())
for i in range(T):
  N, s, e, K = list(map(int, input().split()))
  arr = list(map(int, input().split()))
  b = arr[s-1: e]
  b.sort()
  print("#%d %d" %(i+1, b[K-1]))
