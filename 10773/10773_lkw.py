from collections import deque
import sys
sys.stdin = open("10773/input.txt","r")

n, *l = map(int, sys.stdin.read().split())
stk = deque()

for x in l:
    if x == 0:
        stk.pop()
    else:
        stk.append(x)

print(sum(stk))