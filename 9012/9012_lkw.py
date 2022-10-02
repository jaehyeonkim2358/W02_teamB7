from collections import deque
import sys
sys.stdin = open("9012/input.txt","r")

n, *l = sys.stdin.read().strip().split('\n')

stk = deque()
for line in l:
    flag = False
    for p in line:
        if p == '(':
            stk.append(p)
        else :
            try:
                stk.pop()
            except IndexError:
                print('NO')         # '(' 가 모두 pop 되었는데 ')'가 나타난 경우.
                flag = True
                break
    if not flag:
        if not stk : print('YES')   # 스택이 비어있을 때
        else: print('NO')           # 스택에 괄호 남아있을 때
        
    stk.clear()

