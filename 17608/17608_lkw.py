from collections import deque
import sys
sys.stdin = open("17608/input.txt","r")

n, *l = map(int, sys.stdin.read().strip().split('\n'))

stk = deque()

for x in l:
    while stk and stk[-1] <= x:
        stk.pop()
    stk.append(x)

print(len(stk))
