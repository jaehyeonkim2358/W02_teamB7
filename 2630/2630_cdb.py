# 2630: 색종이 만들기
# 쿼드트리를 만드는 문제

# 하얀색: 0
# 파란색: 1
import sys
N = int(sys.stdin.readline())

confetti = []
for i in range(N):
    input = list(map(int, sys.stdin.readline().split()))
    confetti.append(input)

white_count = 0
blue_count = 0

def quad_tree(x, y, n):
    global white_count
    global blue_count
    
    check = confetti[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != confetti[i][j]:
                check = -1
                break
    if check == -1:
        n = n // 2 
        quad_tree(x, y, n)
        quad_tree(x, y+n, n)
        quad_tree(x+n, y, n)
        quad_tree(x+n, y+n, n)

    elif check == 1:
        blue_count += 1
    else:
        white_count += 1

quad_tree(0, 0, N)
# 하얀색: 0
print(white_count)
# 파란색: 1
print(blue_count)
