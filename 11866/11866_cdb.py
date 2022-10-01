# 11866: 요세푸스 문제 0
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(<=N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거하낟.
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
deque = deque(range(1, N+1))
result = []

# [1, 2, 3, 4, 5, 6, 7]
# -> [3, 4, 5, 6, 7, 1, 2]  3 out
# -> [4, 5, 6, 7, 1, 2]
# -> [6, 7, 1, 2, 4, 5]     6 out
# -> [7, 1, 2, 4, 5]        
# -> [2, 4, 5, 7, 1]        2 out
# -> [4, 5, 7, 1]           
# -> [7, 1, 4, 5]           7 out       
# -> [1, 4, 5]
# -> [5, 4, 1]              5 out
# -> [1, 4]                 1 out
# -> [4]                    4 out   

while N > 0:   
    # K가 3이면, 앞에 두 개가 뒤로 가면 된다. 
    for i in range(K-1):
        deque.append(deque.popleft())
    result.append(deque.popleft())
    N -= 1
    
print("<", end="")
# *의 의미는?
print(*result, sep=', ', end="")
print(">", end="")

