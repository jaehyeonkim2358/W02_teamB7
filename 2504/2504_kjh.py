import sys

ps = sys.stdin.readline().rstrip()

def check(target):
    stack = []                          # 괄호 문자를 입력대로 하나씩 push 또는 pop
    flag = 1                            # 올바른 괄호 문자열인지 여부
    depth = 0                           # 괄호의 깊이
    depth_sum = [0] * (len(target)+1)   # 괄호의 각 깊이에 대한 계산값을 저장, 갱신할 리스트

    for p in target:
        if p == '[' or p == '(':
            depth += 1
            stack.append(p)
        elif len(stack) == 0 or {']':'[', ')':'('}[p] != stack[-1]:
            flag = 0
            break
        else:
            depth_sum[depth] = 1 if depth_sum[depth]==0 else depth_sum[depth]
            if p == ']':
                depth_sum[depth] *= 3
            else:
                depth_sum[depth] *= 2
            
            depth -= 1
            depth_sum[depth] += depth_sum[depth+1]
            depth_sum[depth+1] = 0
            stack.pop()
    return flag if flag == 0 else depth_sum[0]

ans = check(ps)
print(f'{ans}')