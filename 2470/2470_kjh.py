import sys

n = int(sys.stdin.readline().rstrip())
sol = sorted(list(map(int, sys.stdin.readline().split())))

def solution(sol):
    s = 0
    e = n-1
    min_sum = 9999999999999
    min_sol = [None, None]
    while s < e:
        if abs(sol[s]+sol[e]) < min_sum:
            min_sum = abs(sol[s]+sol[e])
            min_sol[0] = sol[s]
            min_sol[1] = sol[e]
        if abs(sol[s]) > abs(sol[e]):
            s += 1
        else:
            e -= 1
    return min_sol

answer = solution(sol)
sys.stdout.write(f'{answer[0]} {answer[1]}')
