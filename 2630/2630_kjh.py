n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

count = [0, 0]

def solution(target, size, r, c):
    global count
    if size == 1:
        count[target[r][c]] += 1
        return
    color = check(target, size, r, c)
    if color != -1:
        count[color] += 1
        return
    solution(target, size//2, r, c)
    solution(target, size//2, r, c+size//2)
    solution(target, size//2, r+size//2, c)
    solution(target, size//2, r+size//2, c+size//2)
    

def check(target, size, r, c):
    color = target[r+size-1][c+size-1]
    for i in range(r, r + size):
        for j in range(c, c + size):
            if target[i][j] != color:
                return -1
    return color
            
solution(paper, n, 0, 0)
print(f'{count[0]}\n{count[1]}')
