# 10830: 행렬 제곱
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 
# 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

import sys
sys.stdin = open('input.txt', 'r')
# 크기가 N*N인 행렬 A, B제곱
N, B = map(int, sys.stdin.readline().split())

# N개의 줄에 행렬의 각 원소 주어짐
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    

# 받을 때부터 행렬의 각 원소가 나머지로 들어감.??
for i in range(N):
    for j in range(N):
        A[i][j] %= 1000
    
# 행렬 간의 곱셈하는 함수
def calc(ma, mb):
    n = len(ma)
    new_arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
               new_arr[i][j] += ma[i][k] * mb[k][j]
            new_arr[i][j] %= 1000
    return new_arr

# 분할정복을 통합 거듭제곱
def solution(a, b):
    if b == 1:
        return a
    sub_a = solution(a, b//2)
    if b % 2 == 1:  # 제곱하는 숫자가 홀수인 경우
        return calc(calc(sub_a, sub_a), a)
    else:   # 제곱하는 숫자가 짝수인 경우
        return calc(sub_a, sub_a)

answer = solution(A, B)

for a in answer:
    for i in a:
        sys.stdout.write(f'{i} ')
    sys.stdout.write('\n')


