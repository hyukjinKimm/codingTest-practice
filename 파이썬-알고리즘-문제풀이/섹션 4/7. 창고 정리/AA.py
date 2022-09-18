import sys
#sys.stdin=open("input.txt", "r")

N =int(input())
boxes = list(map(int, input().split()))
M = int(input())
for i in range(M):
  boxes.sort()
  boxes[0] += 1
  boxes[N-1] -= 1

boxes.sort()
print(boxes[N-1] - boxes[0])