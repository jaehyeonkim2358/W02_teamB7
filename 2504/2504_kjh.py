# boj 2504 괄호의 값

import sys

ps = sys.stdin.readline().rstrip()

def check(target):
    stack = []                          # 괄호 문자를 입력대로 하나씩 push 또는 pop
    depth = 0                           # 괄호의 깊이
    depth_sum = [0] * (len(target)+1)   # 괄호의 각 깊이에 대한 계산값을 저장, 갱신할 리스트

    for p in target:
        # '여는 괄호'가 시작되면 push(), 괄호 깊이 1 증가
        if p == '[' or p == '(':
            stack.append(p)
            depth += 1
        else:
            # 올바르지 않은 '닫는 괄호'일 경우 결과값에 0 저장 후 반복문 종료
            if len(stack) == 0 or {']':'[', ')':'('}[p] != stack[-1]:
                depth_sum[0] = 0
                break
            # 올바른 '닫는 괄호'일 경우 pop(), 계산
            else:
                stack.pop()
                # 곱 연산을 위해, 현재 계산된 값이 없다면 초기값 1로 저장
                depth_sum[depth] = 1 if depth_sum[depth] == 0 else depth_sum[depth]
                # 각 괄호에 대한 연산
                if p == ']':
                    depth_sum[depth] *= 3
                else:
                    depth_sum[depth] *= 2
                # 이전 깊이의 괄호에 대한 계산값을 더해줌
                depth_sum[depth-1] += depth_sum[depth]
                # 현재 값은 더해줬으므로 0으로 초기화
                depth_sum[depth] = 0
                # 괄호가 닫혔으므로 깊이 1 감소
                depth -= 1

    return depth_sum[0]

print(f'{check(ps)}')