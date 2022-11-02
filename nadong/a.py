from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def get_nextPos(pos, visited, new_board, n):
    next_pos = []
    pos1, pos2 = pos 
    x1, y1, x2, y2 = pos1[0], pos1[1], pos2[0], pos2[1]
    for i in range(4):
        xx1 = x1 + dx[i]
        yy1 = y1 + dy[i]

        xx2 = x2 + dx[i]
        yy2 = y2 + dy[i]

        if 1<=xx1<=n and 1<=yy1<=n and 1<=xx2<=n and 1<=yy2<=n:
            if new_board[xx1][yy1] == 0 and new_board[xx2][yy2] == 0: 
              if {(xx1, yy1), (xx2, yy2)} not in visited:
                next_pos.append({(xx1, yy1), (xx2, yy2)})

    if x1 == x2:
      for ddx in [-1, 1]:
        xx1 = x1 + ddx
        if new_board[xx1][y1] == 0 and new_board[xx1][y2] == 0:
            if {(x1, y1), (xx1, y1)} not in visited:
              next_pos.append({(x1, y1), (xx1, y1)})
            if {(x2, y2), (xx1, y2)} not in visited:
              next_pos.append({(x2, y2), (xx1, y2)})
           
    if y1 == y2:
      for ddy in [-1, 1]:
        yy1 = y1 + ddy
        if new_board[x1][yy1] == 0 and new_board[x2][yy1] == 0:
            if {(x1, y1), (x1, yy1)} not in visited:
              next_pos.append({(x1, y1), (x1, yy1)})
            if {(x2, y2), (x2, yy1)} not in visited:
              next_pos.append({(x2, y2), (x2, yy1)})

    return next_pos
            

def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i-1][j-1] != 1:
                new_board[i][j] = board[i-1][j-1]

    visited = []
    pos = {(1, 1), (1, 2)}
    visited.append(pos)
    queue = deque([])
    queue.append((pos, 0))

    while queue:
        pos, second = queue.popleft()
        for next_pos in get_nextPos(pos, visited, new_board, n): # 현재 pos 에서 움직일 수 있는 list(pos)
          if (n, n) in next_pos:
            return second + 1 
          visited.append(next_pos)
          queue.append((next_pos, second+1))

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))