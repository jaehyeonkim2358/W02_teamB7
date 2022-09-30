# 18258: 큐2
import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline())
que = [0] * N

# 초기값 설정만 잘 해주면 됨.
front = 0
rear = -1

def push(num):
    global rear
    rear += 1
    que[rear] = num

def pop():
    global front
    global rear
    if empty():
        return -1
    else:
        x = que[front]
        front += 1
        return x
    
def size():
    global front
    global rear
    return rear - front + 1

def empty():
    global front
    global rear
    return 1 if rear-front < 0 else 0

def _front():
    global front
    if empty():
        return -1
    else:
        return que[front]

def back():
    global rear
    if empty():
        return -1
    else:
        return que[rear]

while N > 0:
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        num = int(command.split()[1])
        push(num)
    else:
        if command == 'pop':
            sys.stdout.write(f'{pop()}\n')
        elif command == 'size':
            sys.stdout.write(f'{size()}\n')
        elif command == 'empty':
            sys.stdout.write(f'{empty()}\n')
        elif command == 'front':
            sys.stdout.write(f'{_front()}\n')
        else:
            sys.stdout.write(f'{back()}\n')
    N -= 1

