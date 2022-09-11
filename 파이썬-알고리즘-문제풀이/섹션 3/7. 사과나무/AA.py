import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = e = N // 2
summ = 0
 

for i in range(N):
  summ += sum(arr[i][s:e+1])
  if i < N//2 :
    s -= 1
    e += 1
  else:
    s += 1
    e -= 1
print(summ)

