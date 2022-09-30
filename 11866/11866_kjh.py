from collections import deque

n, k = map(int, input().split())
a = deque([i for i in range(1, n+1)])
result = list()
while n > 0:
    for _ in range(k-1):
        a.append(a.popleft())
    result.append(a.popleft())
    n -= 1

print('<', end="")
print(*result,sep=', ', end="")
print('>', end="")
