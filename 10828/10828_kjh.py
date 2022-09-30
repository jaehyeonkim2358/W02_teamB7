import sys

n = int(sys.stdin.readline().rstrip())
stack = [0] * n
last_idx = -1

def push(num):
    global stack
    global last_idx
    last_idx += 1
    stack[last_idx] = num

def pop():
    global stack
    global last_idx
    if last_idx < 0:
        return -1
    else:
        v = stack[last_idx]
        last_idx -= 1
        return v

def size():
    global stack
    global last_idx
    return last_idx+1

def empty():
    global stack
    global last_idx
    return 1 if last_idx < 0 else 0

def top():
    global stack
    global last_idx
    return -1 if last_idx < 0 else stack[last_idx]


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
        else:
            sys.stdout.write(f'{top()}\n')
    n -= 1
sys.stdout.flush()