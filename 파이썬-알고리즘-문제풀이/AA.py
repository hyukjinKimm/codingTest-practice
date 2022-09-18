import sys
sys.stdin=open("input.txt", "r")

N =int(input())
time = []
for i in range(N):
  time.append(list(map(int, input().split())))

time.sort(key=lambda x: x[1])
endtime = - 1
cnt = 0
for i in range(N):
  if time[i][0] >= endtime:
    cnt += 1
    endtime = time[i][1]
print(cnt)