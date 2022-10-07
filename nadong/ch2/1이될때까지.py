
import sys
sys.stdin=open("input.txt", "r")
N, K = map(int, input().split())
cnt = 0


while True:
  if N < K:
    cnt += N-1 
    break
  else: 
    target = (N//K) * K 
    cnt += N - target  
    N = target // K 
    cnt += 1     


print(cnt)
    
