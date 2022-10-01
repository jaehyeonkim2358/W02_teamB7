import sys
# heapq 는 기본적으로 Min Heap 임
import heapq

n = int(sys.stdin.readline().rstrip())

max_heap = []
min_heap = []
cnt = 0

while n > 0:
    k = int(sys.stdin.readline().rstrip())


    # [ 값 저장 ]

    # 1. 길이가 0 이거나(첫 입력), 
    # 2. max_heap의 root보다 k가 작을 경우에만
    # max_heap에 push
    if len(max_heap) == 0 or -max_heap[0] > k:
        # max_heap으로 사용하기 위해서 부호를 반대로 바꿔줌
        heapq.heappush(max_heap, -k)
    # 그 외의 경우는, min_heap에 push
    else:
        heapq.heappush(min_heap, k)


    # [ 중간값 유지를 위한 힙 간 값 전달 ]

    # 양 heap의 길이가 2 이상 차이나면 
    # 긴 쪽에서 pop()한 값을 짧은 쪽에서 push() 받음
    if len(max_heap) > len(min_heap)+1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap)+1:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))


    # [ 현재 중간값이 있는 힙을 판별 ]

    # 두 힙의 길이가 같다면
    if len(min_heap) == len(max_heap):
        # 중간값은 두 힙의 root값 중 작은 값
        mid = min_heap[0] if min_heap[0] < -max_heap[0] else -max_heap[0]
        sys.stdout.write(f'{mid}\n')
    # 두 힙의 길이가 다르다면
    else:
        # 중간값은 두 힙 중 길이가 긴 힙의 root값
        mid = min_heap[0] if len(min_heap) > len(max_heap) else -max_heap[0]
        sys.stdout.write(f'{mid}\n')

    n -= 1
