import sys
from itertools import permutations
sys.stdin=open("input.txt", "r")

def D(x):
  ch[x] = 1
  global cnt
  if x == n:
    print(path)   
  else:
    for i in range(1, n+1):
      if graph[x][i] == 1 and ch[i] == 0:

        ch[i] = 1
        path.append(i)
        D(i)
        path.pop()
        ch[i] = 0

    
     

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
ch = [0] * (n+1)
for i in range(m):
  a, b= map(int, input().split())
  graph[a][b] = 1
for x in graph:
  print(x)
path = []
cnt = 0
def main():
  path.append(1)
  D(1)
if __name__ == '__main__':
  main()


