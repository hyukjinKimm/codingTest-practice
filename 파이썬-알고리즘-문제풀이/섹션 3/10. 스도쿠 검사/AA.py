import sys
#sys.stdin=open("input.txt", "r")

board = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
  ch1 = [0] * 10
  ch2 = [0] * 10
  for j in range(9):
    ch1[board[i][j]] = 1
    ch2[board[j][i]] = 1
  if sum(ch1) != 9 or sum(ch2) != 9:
    print('NO')
    break 
else:
  for i in range(0, 9, 3):
    ch1 = [0] * 10
    for j in range(0, 9, 3):
      for k in range(3):
        for m in range(3):
          ch1[board[i+k][j+m]] = 1
      if sum(ch1) != 9:
        print('NO')
        sys.exit()
  else:
    print('YES')

