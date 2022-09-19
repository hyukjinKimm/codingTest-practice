import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

N, K = map(int, input().split())

arr = deque([i+1 for i in range(N)])

while len(arr) > 1:
  for i in range(K-1):
    arr.append(arr.popleft())
  arr.popleft()

print(arr[0])