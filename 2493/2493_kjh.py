import sys

n = int(sys.stdin.readline().rstrip())

tower = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []
idx = 0
while n > 0:
    if not stack:
        stack.append([tower[idx], idx+1])
        answer.append(0)
    else:
        while stack and stack[len(stack)-1][0] < tower[idx]:
            stack.pop()
        if stack:
            answer.append(stack[len(stack)-1][1])
        else:
            answer.append(0)
        stack.append([tower[idx], idx+1])
    idx += 1
    n -= 1

print(*answer)