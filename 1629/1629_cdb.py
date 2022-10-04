# 1629: 곱셈
# 자연수 A를 B번 곱한 수를 알고 싶다.
# 단, 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구한다.

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')
num = list(map(int, sys.stdin.readline().split()))

a, b, c = num[0], num[1], num[2]

def power(a, n, z):
    if n == 0:
    	# a^0 = 1 이므로 1 리턴
        return 1 
    
    x = power(a, n//2, z)
    
    if n % 2 == 0: # n이 짝수일 때
        return x * x % z   # x를 두 번 곱해줘서 power 함수의 호출을 반으로 줄일 수 있다.
    
    else: # n이 홀수일 때
        return x * x * a % z

print(power(a, b, c))