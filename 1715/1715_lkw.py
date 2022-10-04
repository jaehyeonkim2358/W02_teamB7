from heapq import *
import sys
sys.stdin = open("1715/input.txt","r")

n = int(input())
l = list(map(int, sys.stdin.read().strip().split('\n')))

# 작은 순서대로 섞는 것이 최소값이 아니라, 매번 카드 뭉치 모음에서 가장 적은 두개를 골라서 섞어야 함.
# 두개의 카드뭉치가 하나의 카드뭉치가 된 후, 그 하나의 카드뭉치가 원래의 카드뭉치 모음에서 다시 하나의 카드 뭉치로 취급된다.

heapify(l)
result = 0

while len(l) > 1 :
    x = heappop(l)
    y = heappop(l)
    new_deque = x+y
    heappush(l, new_deque)
    result += new_deque
        
print(result)

