import sys
sys.stdin=open("input.txt", "r")
n, k = map(int, input().split()) # n >= k >= 2 

cnt = 0 
while n >= k:
  target = n // k * k 
  cnt += n - target 
  n = target // k 
  cnt += 1

cnt +=  n-1
print(cnt) 
  
