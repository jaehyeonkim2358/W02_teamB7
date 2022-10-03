import sys
import heapq
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline().rstrip())
max_heap, min_heap = [], []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    # 방법1: 왼쪽 최대 힙의 크기와 오른쪽 최대 힙의 크기가 똑같은 경우 왼쪽 최대 힙에 push 해줌.
    # if len(max_heap) == len(min_heap):
    #     heapq.heappush(max_heap, -num)

    # 방법2: i가 짝수일 때 왼쪽에 위치한 최대 힙에 push 해줌.
    if i % 2 == 0:
        heapq.heappush(max_heap, num * -1)
    else:
        heapq.heappush(min_heap, num)

    if max_heap and min_heap and max_heap[0] * -1 > min_heap[0]:
        temp = heapq.heappop(max_heap)* -1
        heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
        heapq.heappush(min_heap, temp)

    print(max_heap[0] * -1)