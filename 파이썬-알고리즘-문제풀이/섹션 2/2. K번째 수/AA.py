import sys
#sys.stdin=open("input.txt", "r")
T = int(input())
for i in range(T):
  n, s, e, k = map(int, input().split())
  arr = list(map(int, input().split()))
  ans = sorted(arr[s-1:e])
  print(f'#{i+1} {ans[k-1]}')
