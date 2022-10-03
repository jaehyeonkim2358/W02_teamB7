import sys

n, b = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] %= 1000
    
def solution(a, b):
    if b == 1:
        return a
    sub_a = solution(a, b//2)
    if b % 2 == 1:
        return calc(calc(sub_a, sub_a), a)
    else:
        return calc(sub_a, sub_a)

    
def calc(ma, mb):
    result = [[0]*len(ma) for _ in range(len(ma))]
    for i in range(len(ma)):
        for j in range(len(ma)):
            for k in range(len(ma)):
                result[i][j] += ma[i][k] * mb[k][j]
            result[i][j] = result[i][j]%1000
    return result

answer = solution(a, b)

for a in answer:
    for i in a:
        sys.stdout.write(f'{i} ')
    sys.stdout.write('\n')
