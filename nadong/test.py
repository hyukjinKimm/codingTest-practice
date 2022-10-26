import sys
from collections import deque
sys.stdin=open("input.txt", "r")

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1

ch = [0] * (n+1)

def DFS(x):
  print(x, end = ' ')
  for i in range(n+1):
    if graph[x][i] == 1 and ch[i] == 0:
      ch[i] = 1 
      DFS(i)


def main():
  ch[v] = 1
  DFS(v)
  

  arr = deque()


      
if __name__ == "__main__":
  main()
