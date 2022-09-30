from collections import deque
import sys
sys.stdin = open("18258/input.txt","r")

n = int(input())
stk = deque([],maxlen=10000)
for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        stk.append(int(cmd[1]))
        
    elif cmd[0] == 'pop':
        try:
            print(stk.pop())
        except IndexError:
            print(-1)

    elif cmd[0] == 'size':
        print(len(stk))

    elif cmd[0] == 'empty':
        print(int(not stk))

    elif cmd[0] == 'top':
        try:
            print(stk[-1])
        except IndexError:
            print(-1)
