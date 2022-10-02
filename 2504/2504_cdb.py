# 2504: 괄호의 값

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline().strip())

while N > 0:
    bracket = sys.stdin.readline().strip()
    vps = []
    for i in bracket:
        if i == '(':
            vps.append(i)
        else:
            if len(vps) == 0:
                vps.append(i)
            else: 
                if vps[-1] == "(":
                    vps.pop()
                else:
                    vps.append(i)
    if len(vps) == 0:
        print("YES")
    else:
        print("NO")
    N -= 1