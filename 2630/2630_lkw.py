import sys
sys.stdin = open("2630/input.txt","r")

n = int(sys.stdin.readline())
ll = sys.stdin.read().strip().split('\n')
l = [[int(x) for x in line.split()] for line in ll]
result = [0,0]

def is_complete(l, row, col, w):
    key = l[row][col]
    for i in range(row, row+w):
        for j in range(col, col+w):
            if key != l[i][j] : return False
    return True

def update_result(key):
    if key : result[1] += 1
    else : result[0] += 1

def func(l, result, row, col, n):
    # (white, blue)

    if is_complete(l, row, col, n):
        update_result(l[row][col])
        return
    
    if n == 1:
        update_result(l[row][col])
        return

    n //= 2
    func(l, result, row, col, n)
    func(l, result, row, col+n, n)
    func(l, result, row+n, col, n)
    func(l, result, row+n, col+n, n)

func(l, result, 0, 0, n)

print(*result, sep='\n', end='')