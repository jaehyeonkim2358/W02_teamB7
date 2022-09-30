from collections import deque

a = deque([i for i in range(1, int(input())+1)])

flag = 1
while len(a) > 1:
    if flag == 1:
        a.popleft()
    else:
        a.append(a.popleft())
    flag = (flag + 1) % 2

print(a.pop())