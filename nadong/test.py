import sys

sys.stdin=open("input.txt", "r")


def solve(n):
  k  = -1
  ki = 0
  for i in range(len(n)-1, 0, -1):
    for j in range(i-1, -1, -1):
      if int(n[j]) < int(n[i]):
        if j > k :
          ki = i
          k=j 
        elif j == k:
          if n[i] < n[ki] :
            ki = i
  else:
    if k == -1:
      print('BIGGEST')
    else:
      n[k], n[ki] = n[ki], n[k]
      res = n[:k+1]
      res += sorted(n[k+1:])
      print("".join(res))
    



def main():
  t = int(input())
  for i in range(t):
    n = list(input())
    if len(n) == 1 or len(n) == 2:
      print('BIGGEST')
      return
    solve(n)

dd

   
if __name__ == "__main__":
  main()
