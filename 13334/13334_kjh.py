import heapq
import sys

n = int(sys.stdin.readline().rstrip())
# 입력 값이 전혀 정렬되어있지 않은채로 들어옴
roads = sorted([sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(n)], key=lambda x: (x[1], x[0]))
d = int(sys.stdin.readline().rstrip())

heap = []
answer = 0
for road in roads:
    if road[1] - road[0] > d:
        continue
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

sys.stdout.write(f'{answer}')
