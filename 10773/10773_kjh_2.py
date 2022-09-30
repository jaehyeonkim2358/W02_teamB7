import sys

k = int(sys.stdin.readline().rstrip())

stack = []

while k > 0:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
    k -= 1

sys.stdout.write(f'{sum(stack)}')