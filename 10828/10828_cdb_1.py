import sys
N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    command = list(sys.stdin.readline().split())
    # push X: 정수 X를 스택에 넣는 연산
    if command[0] == 'push':
        stack.append(command[1])

    # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수 출력
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    # size: 스택에 들어있는 정수의 개수 출력
    elif command[0] == 'size':
        print(len(stack))

    # empty: 스택이 비어있으면 1, 아니면 0
    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    # top: 스택의 가장 위에 있는 정수 출력
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
