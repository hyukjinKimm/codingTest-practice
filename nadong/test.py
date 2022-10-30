import queue
import sys
from collections import deque
from itertools import product
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def main():
 n = 4
 print(list(product(['+', '+','-', '*', '/'], repeat = n-1)))

  
      
if __name__ == "__main__":
  main()


