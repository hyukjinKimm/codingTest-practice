import sys
sys.stdin=open("input.txt", "r")

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
  for j in range(7):
    for k in range(2):
      if board[j][i+k] != board[j][4-k+i]:
        break 
    else:
      cnt += 1
  for j in range(7):
    for k in range(2):
      if board[i+k][j] != board[4-k+i][j]:
        break 
    else:
      cnt += 1
print(cnt)