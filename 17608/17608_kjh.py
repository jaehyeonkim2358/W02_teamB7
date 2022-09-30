import sys

n = int(sys.stdin.readline().rstrip())

stack = []

while n > 0:
    m = int(sys.stdin.readline().rstrip())
    if len(stack) == 0:
        stack.append(m)
    else:
        while stack[-1] <= m:
            stack.pop()
            if len(stack) == 0:
                break
        stack.append(m)
    n -= 1
sys.stdout.write(f'{len(stack)}')
