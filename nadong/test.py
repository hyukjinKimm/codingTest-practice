
import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)


def main():
  n = int(input())
  arr = []
  for _ in range(n):
    arr.append(int(input()))
  res = 0
  k = 1
  while arr:
    for i in range(len(arr)):
      if arr[i] == k:
        res += k 
        k += 1
        arr.pop(i)
        break
  print(res)
      
        


   
if __name__ == "__main__":
  main()
