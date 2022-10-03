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

    # 방법2: 입력값을 최대 힙과 최소 힙에 번갈아 가면서 저장하면, 항상 최대 힙의 peek 값이 중간값이 된다.
    # 단, 저장할 때마다 최대 힙의 peek값과 최소 힙의 peek 값을 비교하고, 최소 힙의 peek값이 더 크다면 그 둘을 바꿔줘야한다.
    # (항상 최대 힙의 peek값이 최소 힙의 peek 값보다 작도록 유지하며 진행)
    if i % 2 == 0:
        heapq.heappush(max_heap, num * -1)
    else:
        heapq.heappush(min_heap, num)

    if max_heap and min_heap and max_heap[0] * -1 > min_heap[0]:
        temp = heapq.heappop(max_heap)* -1
        heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)
        heapq.heappush(min_heap, temp)

    print(max_heap[0] * -1)
