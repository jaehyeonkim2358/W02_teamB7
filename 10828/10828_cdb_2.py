import sys
N = int(sys.stdin.readline())

stack = []

def push(n):
    stack.append(n)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        # print(stack.pop)를 하면 print만 되는게 아니라 pop()도 같이 됨
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

# N이 명령의 수이기 때문에 0보다 클 때까지 ~
while N > 0:
    command = sys.stdin.readline().strip()
    # type(command) => str이기 때문에 push 2를 split()을 활용해서 쪼개준다.
    if 'push' in command:
        num = int(command.split()[1])
        push(num)
    elif 'pop' in command:
        pop()
    elif 'size' in command:
        size()
    elif 'empty' in command:
        empty()
    else:
        top()
    N -= 1

