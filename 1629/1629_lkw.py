import sys
sys.stdin = open("1629/input.txt","r")

A, B, C = map(int, input().split())

# 모듈러 연산의 분배법칙 활용
# 모듈러 연산의 분배법칙의 특징은 분배 후에도 모듈러 연산이 살아남는다는 점이다.
# 일반적인 곱셈의 분배법칙  -> (A*B) * C = AC * BC
# 모듈러 연산의 분배법칙    -> (A*B) % C = ((A%C) * (A%B)) % B
# 따라서 다음과 같은 식이 성립한다.
# A^n % B = (A*A*..(n번)..*A) % B
#         = ((A%B) * (A%B)*..(n번)..*(A%B)) % B
#         = ((A%B)^n) % B
#         즉, n제곱 안으로 모듈러 연산을 바로 분배할 수 있다.
#
# 그래서 n이 짝수일 때(n%2 == 0) A^n % B 는
# (A^(n//2))^2 % B = (A^(n//2) % B)^2 % B 로 표현될 수 있다. 그리고 A^(n//2) % B 를 다시 재귀적으로 계산하면 되는 것.
# n이 홀수일 때는 [(A^(n//2))^2 * A] % B = [{(A^(n//2))^2 % B} * (A % B)] % B = [{(A^(n//2) % B)^2 % B} * (A % B)] % B처럼 표현 가능하다.

def fast_mod(A, n, B):
    if n <= 6:
        return A**n%B

    if n % 2 == 0:
        return fast_mod(A, n//2, B)**2 % B
    else: # n % 2 == 1
        return ((fast_mod(A, n//2, B)**2 % B) * (A % B)) % B

print(fast_mod(A,B,C))



