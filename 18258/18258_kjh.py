import sys

n = int(sys.stdin.readline().rstrip())
queue = [0] * n

front = 0
rear = -1


def push(num):
    global rear
    rear += 1
    queue[rear] = num

def pop():
    global rear
    global front
    if empty():
        return -1
    else:
        v = queue[front]
        front += 1
        return v
    
def size():
    global rear
    global front
    return rear-front+1

def empty():
    global front
    global rear
    return 1 if rear-front < 0 else 0

def _front():
    global front
    if empty():
        return -1
    else:
        return queue[front]

def back():
    global rear
    if empty():
        return -1
    else:
        return queue[rear]


while n > 0:
    cmd = sys.stdin.readline().rstrip()
    if 'push' in cmd:
        num = int(cmd.split()[1])
        push(num)
    else:
        if cmd == 'pop':
            sys.stdout.write(f'{pop()}\n')
        elif cmd == 'size':
            sys.stdout.write(f'{size()}\n')
        elif cmd == 'empty':
            sys.stdout.write(f'{empty()}\n')
        elif cmd == 'front':
            sys.stdout.write(f'{_front()}\n')
        else:
            sys.stdout.write(f'{back()}\n')
    n -= 1

