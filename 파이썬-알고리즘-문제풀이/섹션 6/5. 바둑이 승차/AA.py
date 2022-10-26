
import sys


def D(x, s, t):
  global res
  if s > c:
    return 
  if s + sum(dog) - t <= res:
    return
  if x >= len(dog):
    res = max(s, res)
    return
  else:
    D(x+1, s+dog[x], t + dog[x])
    D(x+1, s, t + dog[x])
  

c, n = map(int, input().split())
dog = []
res = 0
for _ in range(n):
  dog.append(int(input()))
def main():
  D(0, 0, 0)
  print(res)
if __name__ == '__main__':
  main()

