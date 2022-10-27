import sys
def D(x, s):
  if x >= len(arr):
    if s == sum(arr) - s:
      print('YES')
      sys.exit()
  else:
    D(x+1, s+arr[x])
    D(x+1, s)
  

n = int(input())
arr = list(map(int, input().split()))

def main():
  D(0, 0)
  print('NO')

if __name__ == '__main__':
  main()

