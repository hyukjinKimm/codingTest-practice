import sys
#sys.stdin=open("input.txt", "r")

arr = [i for i in range(21)]
for i in range(10):
  a, b = map(int, input().split())
  for j in range((b-a) // 2 + 1 ):
    arr[a+j], arr[b-j] = arr[b-j], arr[a+j]
for i in arr:
  print(i, end  = ' ')