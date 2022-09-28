import sys

sys.stdin=open("input.txt", "r")
N, M = map(int, input().split())
arr = [i+1 for i in range(N)]
while len(arr) != 1:
  for _ in range(M-1):
    arr.append(arr.pop(0))
  arr.pop(0)
print(arr[0])