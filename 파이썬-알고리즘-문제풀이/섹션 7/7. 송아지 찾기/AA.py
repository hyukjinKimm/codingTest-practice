import sys
from collections import deque
#sys.stdin=open("input.txt", "r")


N, M = map(int, input().split())
dis = [0]  *10001
ch = [0] * 10001
ch[N] = 1
Q = deque()
Q.append(N)
while True:
  x = Q.popleft()
  for i in [x-1, x+1, x + 5]:
    if 0 < i < 10001 and ch[i] == 0:
      dis[i] = dis[x] + 1
      ch[i] = 1
      Q.append(i)
      if i == M:
        print(dis[M])
        sys.exit()
