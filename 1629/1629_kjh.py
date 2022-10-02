a, b, c = map(int, input().split())

def solution(a, b):
    global c
    if b <= 1:
        return 1 if b == 0 else a%c
    if b % 2 == 0:
        return solution((a%c)*(a%c), b//2) % c
    else:
        return ((solution((a%c)*(a%c), b//2) % c) * (a%c))%c

print(solution(a, b))
