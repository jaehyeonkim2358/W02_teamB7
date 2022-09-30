import sys
# N의 영상의 크기가 주어지고, N**2만큼 크기의 범위에 0과 1로 이어져있다. 
# 0과 1이 섞여있다면, 4분면으로 나눠 압축하여 출력한다.
# quad_tree가 실행되면, x, y 범위 값을 검사해 범위 안에 서로 다른 값이 있을 경우 4등분으로 나눠주고 괄호를 쳐준다.
# 만약 재귀함수로 안 들어가고 for문이 끝난다면 범위 안에 값이 전부 같은 값이기 때문에 result에 append 해준다.
N = int(sys.stdin.readline())

board = [list(map(int, (input()))) for i in range(N)]
print(board)
def quad_tree(x, y, n):
    check = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != board[i][j]:
                check = -1
                break
    if check == -1:
        # 모두 같은 색이 아니기 때문에 4사분면으로 쪼개진다. 쪼개지기 전, 후로 괄호를 넣는다.
        print("(", end="")
        n = n // 2 
        quad_tree(x, y, n)
        quad_tree(x, y+n, n)
        quad_tree(x+n, y, n)
        quad_tree(x+n, y+n, n)
        print(")", end="")
    elif check == 1:
        print(1, end="")
    else:
        print(0, end="")

quad_tree(0, 0, N)
