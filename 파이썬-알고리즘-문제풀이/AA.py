import sys
sys.stdin=open("input.txt", "r")



board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
  for j in range(3):
    tmp = board[i][j:j+5]
    if tmp == tmp[::-1]:
      cnt += 1

  for j in range(3):
    for k in range(2):
      if board[j+k][i] != board[4+j-k][i]:
        break 
    else:
      cnt += 1 
print(cnt)