# 2164: 카드 2
from collections import deque 

# append(x): 오른쪽(마지막)에 원소 추가(삽입)
# popleft(): 왼쪽(앞쪽)부터 차례대로 제거와 반환
# pop(): 오른쪽에서 원소 하나를 제거하여 반환

d = deque() 
import sys
N = int(sys.stdin.readline())

for i in range(1, N+1):
    d.append(i)

while True:
    if len(d) == 1:
        print(d.pop())
        break
    else:
        d.popleft()
        d.append(d.popleft())


