import sys

sys.stdin=open("input.txt", "r")

def get_bin(x):
  cnt = 0
  sum = 1
  while True:
    sum = 2 ** cnt 
    if sum >= x:
      return sum
    cnt += 1 

  


def main():
  n = int(input())
  b = list(bin(n))
  chk = 0
  for i, c in enumerate(b[2:]):
    if c == '1':
      chk = i+1 
  if chk == 1:
    print(n, 0)
  else:
    print(get_bin(n), chk)

  
  

if __name__ == "__main__":
  main()
