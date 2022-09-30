import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline())

stack = []

# 함수에서 print 출력 안 하고, return 값 받아서 출력하기

def push(n):
    stack.append(n)

def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) == 0: return 1
    else: return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]

# N이 명령의 수이기 때문에 0보다 클 때까지 ~

while N > 0:
    command = sys.stdin.readline().strip()
    # type(command) => str이기 때문에 push 2를 split()을 활용해서 쪼개준다.
    if 'push' in command:
        num = int(command.split()[1])
        push(num)
    elif 'pop' in command:
        sys.stdout.write(f'{pop()}\n')
    elif 'size' in command:
        sys.stdout.write(f'{size()}\n')
    elif 'empty' in command:
        sys.stdout.write(f'{empty()}\n')
    else:
        sys.stdout.write(f'{top()}\n')
    N -= 1

