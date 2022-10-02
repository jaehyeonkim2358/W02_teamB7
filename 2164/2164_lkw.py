import sys
from collections import deque
sys.stdin = open("2164/input.txt","r")

q = deque()
n = int(input())

for x in range(1, n+1):
    q.append(x)

while True:
    if len(q) == 1:
        print(q.pop())
        break

    q.popleft()
    q.append(q.popleft())


    