import sys
#sys.stdin=open("input.txt", "r")

L = int(input())
boxes = list(map(int, input().split()))

M = int(input())
boxes.sort()
for i in range(M):
  boxes[0] += 1
  boxes[L-1] -= 1
  boxes.sort()

print(boxes[L-1] - boxes[0])

