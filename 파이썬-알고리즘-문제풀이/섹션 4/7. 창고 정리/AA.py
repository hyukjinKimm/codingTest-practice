import sys
#sys.stdin=open("input.txt", "r")
import bisect
n = int(input())
box = list(map(int, input().split()))
k = int(input())

for _ in range(k):
  box.sort()
  box[0] += 1
  box[n-1] -= 1
box.sort()
print(box[n-1] - box[0])