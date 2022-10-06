# 2493: 탑

import sys
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())   # 탑의 수
# 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호/수신하는 탑 존재 X => 0
# [6, 9, 5, 7, 4]
# [0, 0, 2, 2, 4]

stack = []
answer = []
highest = 0
for idx, tower in enumerate(map(int, input().split())):
    if tower > highest:
        highest = tower
        stack.append((idx+1, tower))
        answer.append(0)
        continue
    
    while True:
        if stack[-1][1] > tower:
            answer.append(stack[-1][0])
            stack.append((idx+1, tower))
            break
        elif len(stack) == 0:
            answer.append(0)
            break
        # tower보다 큰 애가 stack의 젤 위에 올 때까지...
        else:
            stack.pop()

print(*answer, sep=" ")