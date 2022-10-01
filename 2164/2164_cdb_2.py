from collections import deque
N = int(input())  # 주어질 수의 개수 N
deque = deque(range(1, N+1))

while len(deque) > 1:   # 같은 동작을 카드가 한 장 남을 때까지~
    deque.popleft()             # 제일 왼쪽값 추출 및 삭제
    deque.append(deque.popleft()) # 맨 끝에 값 추가

print(deque.pop())