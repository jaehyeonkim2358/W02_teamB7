# 9012: 괄호
# 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 
# 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline())


while N > 0:
    bracket = sys.stdin.readline().strip()
    cnt = 0
    okay = True
    for i in bracket:
        if i == '(':
            cnt += 1
        else:
            cnt -=1
        if cnt < 0 :
            okay = False
            break
    if okay and cnt == 0:
        print("YES")
    else:
        print("NO")

    N -= 1

