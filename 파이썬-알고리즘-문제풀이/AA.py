import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]
arr = deque(arr)
while len(arr) > 1:
  for _ in range(k-1):
    arr.append(arr.popleft())
  arr.popleft()
print(arr[0])