import sys
#sys.stdin=open("input.txt", "r")

T =int(input())
for i in range(T):
  N, s, e, k = map(int, input().split())
  arr = list(map(int, input().split()))
  tmp = arr[s-1:e]        
  tmp.sort()
  print("#%d %d" %(i+1, tmp[k-1]))


