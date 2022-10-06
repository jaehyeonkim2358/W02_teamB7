import heapq
import sys

# 입력
n = int(sys.stdin.readline().rstrip())
roads = []
for _ in range(n):
    # (70, 40)과 같이 집과 사무실에 대한 좌표가 정렬되어 있지 않기 때문에 정렬 시켜서 입력 받음
    road = sorted(tuple(map(int, sys.stdin.readline().split())))
    roads.append(road)
# roads를 정렬하는데,
# 1. 끝값을 오름차순으로 정렬
# 2. 끝값이 같으면, 시작값을 오름차순으로 정렬
roads = sorted(roads, key=lambda x: x[1])
d = int(sys.stdin.readline().rstrip())

heap = []   # 최소 힙으로 사용할 리스트 heap
answer = 0  # 최대 수를 갱신할 변수 answer

for road in roads:
    # 시작~끝 거리가 철로 길이(d) 보다 크면 철로 선분에 포함될 수 없으므로 패스
    if road[1] - road[0] > d:
        continue
    # heap의 루트(0)의 시작이 (road의 끝 - 철로 길이) 보다 멀리 있을때 까지 pop() 반복
    while heap and heap[0][0] < road[1] - d:
        heapq.heappop(heap)
    # 다음 순회를 위해 현재 road를 heap에 저장
    heapq.heappush(heap, road)
    # 현재 heap에 저장된 값의 개수 = (road의 끝지점 - 철로 길이) 안에 집과 사무실이 있는 사람 수
    answer = max(answer, len(heap))

sys.stdout.write(f'{answer}')
