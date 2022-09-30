from collections import deque
import sys
sys.stdin = open("18258/input.txt","r")

n = int(input())
queue = deque()
for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
        
    elif cmd[0] == 'pop':
        try:
            print(queue.popleft())
        except IndexError:
            print(-1)

    elif cmd[0] == 'front':
        try:
            print(queue[0])
        except IndexError:
            print(-1)
    elif cmd[0] == 'back':
        try:
            print(queue[-1])
        except IndexError:
            print(-1)

    elif cmd[0] == 'size':
        print(len(queue))

    elif cmd[0] == 'empty':
        print(int(not queue))
