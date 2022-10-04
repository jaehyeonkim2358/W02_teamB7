# 2504: 괄호의 값

import sys

sys.stdin = open('input.txt', 'r')
bracket = sys.stdin.readline().rstrip()

def check(target):
    stack = []
    depth = 0
    depth_sum = [0] * (len(target))
    for i in target:
        if i == '(' or i == '[':
            stack.append(i)
            depth += 1
        else:
            # 올바르지 않은 '닫는 괄호'일 경우 결과값에 0 저장 후 반복문 종료
            # 왜냐! 올바른 괄호이면 일치할 때 pop()을 해서 없애기 때문이다.
            # 예를 들어, i가 ']'일 때, stack[-1]이 '['가 아닐 경우
            if len(stack) == 0 or {']':'[', ')':'('}[i] != stack[-1]:
                depth_sum[0] = 0
                break
            else:
                if i == ')' or i == ']':
                    stack.pop()
                depth_sum[depth] = 1 if depth_sum[depth] == 0 else depth_sum[depth]
                if i == ']':
                    depth_sum[depth] *= 3
                else:
                    depth_sum[depth] *= 2
                depth_sum[depth-1] += depth_sum[depth]
                depth_sum[depth] = 0
                depth -= 1
                
    return depth_sum[0]

print(f'{check(bracket)}')
