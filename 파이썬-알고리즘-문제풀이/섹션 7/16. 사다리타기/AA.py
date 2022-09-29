import sys
#sys.stdin=open("input.txt", "r")

dx = [0, 0, -1]
dy = [-1, 1, 0]
def D(P):
  a, b = P
  ch[a][b] = 1
  if a == 0:
    print(b)
    sys.exit()
  else:
    for i in range(3):
      x = a + dx[i]
      y = b + dy[i]
      if 0 <= x < 10 and 0 <= y < 10 and ch[x][y] == 0 and board[x][y] == 1:
        D((x, y))




board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for i in range(10):
  if board[9][i] == 2:
    D((9, i))