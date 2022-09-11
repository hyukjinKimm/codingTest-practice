import sys
#sys.stdin=open("input.txt", "r")

N = int(input())
time = []
for i in range(N):
  s, e =map( int, input().split())
  time.append([s, e])
time.sort(key=lambda x:x[1])


endtime = - 1
cnt = 0 
for t in time:
  if t[0] >= endtime:
    endtime = t[1]
    cnt += 1
print(cnt)