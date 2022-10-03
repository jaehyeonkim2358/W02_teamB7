import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().rstrip()

stack = []
for i in range(len(num)):
    while stack and n-k < len(num)-i + len(stack) and int(stack[-1]) < int(num[i]):
        stack.pop()
    stack.append(num[i])

print(''.join(stack[:n-k]))