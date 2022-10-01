# 괄호의 값 https://www.acmicpc.net/problem/2504
from collections import deque
import sys
sys.stdin = open("2504/input.txt","r")

def check(line):
    op_stk = deque()
    postfix_exp = '0'
    open_pair = {")" : "(" , "]" : "["}

    closed = True
    for p in line:
        if p in '([' :
            if closed : op_stk.append('+')
            else : op_stk.append('*')
            op_stk.append(p);

            if p == '(' : postfix_exp += '2'
            else : postfix_exp += '3'

            closed = False
        else:
            if not op_stk : return 0

            top = op_stk.pop() 
            while top in '+*':
                if not op_stk : return 0

                postfix_exp += top
                top = op_stk.pop()

            if top != open_pair[p]:
                 return 0

            closed = True
    # end for

    while op_stk:
        lefted = op_stk.pop()
        if lefted in '([' :
            return 0
        postfix_exp += lefted

    cal_stk = deque()
    for a in postfix_exp:
        if a in '+*':
            cal_stk.append(eval(f'{cal_stk.pop()}{a}{cal_stk.pop()}'))
        else:
            cal_stk.append(a)
    
    return cal_stk[0]

print(check(input()))

# 백준 정답
# def f(p):
#     if len(p) == 0 :return 1

#     dic = {'(':')', '[':']'}
#     ans, sub, stk = 0, '', []

#     for i in p:
#         sub += i

#         if len(stk) > 0 and dic.get(stk[-1], '') == i:
#             stk.pop()
#         else :
#             stk.append(i)

#         if len(stk) == 0:
#             ans = ans + f(sub[1:-1]) * (2 if sub[0] == '(' else 3)
#             sub= ''

#     if len(stk) > 0 :
#         return 0

#     return ans

# print(f(input()))