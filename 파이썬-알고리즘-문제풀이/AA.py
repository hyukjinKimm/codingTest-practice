import sys
sys.stdin=open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
bongs = [list(map(int, input().split())) for _ in range(N)]
bongs.insert(0, [0]*N)
bongs.append([0]*N)

for i in range(N+2):
  bongs[i].insert(0, 0)
  bongs[i].append(0)
cnt = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    if all(bongs[i][j] > bongs[i+dx[k]][j+dy[k]] for k in range(4)):
      cnt += 1
print(cnt)