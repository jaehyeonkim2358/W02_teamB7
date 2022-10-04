from heapq import heappop, heappush
import sys
sys.stdin = open("13334/input.txt","r")

n, *ll, d = sys.stdin.read().strip().split('\n')
n, d = int(n), int(d)
# 이 문제에서 힙(우선순위 큐)을 쓰는 이유.
#
# 힙은 가장 작은/큰 값 몇개를 알고자 할 때 유용하다.
# for문이 돌아가면서 road가 바뀔 때 가능 범위가 변하므로, 힙에서 가능 범위를 벗어날 가능성이 가장 큰 road들 부터 차례대로 없애는 것이다.
# 이때, 벗어날 가능성이 큰 road들을 얻을 때 유용한 것이 heap인 것인데 이유는,
# 새로운 road를 '넣어 둘때' log n으로 정렬이 되기 때문이다.
# (뺄 때도 log n이라는 단점(힙이 아닌 배열에 정렬된 값들은 그냥 끝 값을 빼면 되기때문에 O(1))이 있긴 하나 넣을 때 log n 인건 큰 장점.)
# 따라서 heap은 값을 넣거나 빼면서 정렬을 유지해야하고, 작은/큰 값들 몇개를 얻어야 할 때 유용하다.

heap = []
roads = []
for line in ll:
    start, end = map(int, line.split())
    # road = (start, end)
    # 항상 road의 start의 원소가 더 작게.
    if start > end:
        roads.append((end,start))
    else:
        roads.append((start,end))

roads.sort(key=lambda x: -x[0]) # road들을 start의 내림차순으로 정렬한다.
                                # 이 경우 end의 값을 저장하는 heap은 최대힙으로 구성해야 함.
                                # 반대로 road들을 end의 오름차순으로 정렬할 경우,
                                # start의 값을 저장하는 heap은 최소힙으로 구성해야 함.
                                # 각 정렬에서의 각 기준 즉, start의 값 또는 end의 값이 같은 road들이 있을 경우 그 값들사이의 정렬은 상관없다.
                                # 어차피 아래에서 heap으로 정리가 된다.

count = 0
for road in roads:
    if road[1] - road[0] > d:
        continue                # 선분 길이보다 도로가 긴 경우 pass
    
    heappush(heap, -road[1])    # end를 기준으로하는 최대힙 즉, end의 내림차순.     # 각 노드는 end값만 가지고 있어도 충분하므로 end의 값만 push했다.
                                # heap에 들어있는 road들은 범위 안에 들어온 road를 의미.
                                # 지금 기준으로 선택된 road는 당연히 범위 안에 존재하므로 일단 push.
    
    limit = road[0] + d         # 지금 road의 start에 d를 더해서 limit값을 얻는다.
    while limit < -heap[0]:     # heap의 루트노드 = end 가 가장 오른쪽에 있는(=큰) road.
                                # end가 가능범위 안에 있는 road가 나올 때 까지 pop.
                                # 지금 기준이 되는 road는 무조건 limit 안이기 때문에 heap이 비어있는지 확인할 필요 없다. 지금 road에 다다르면 while문 깨짐.
        heappop(heap)

    count = max(count, len(heap))   # 가능 범위 내 최대 road 개수 update.
                                    # heap안에 살아남아 있는 road가 가능 범위 안에 있는 road 이다.

print(count)
        

# 시간초과
# heap = []
# for line in ll:
#     h, o = map(int, line.split())
#     if abs(h-o) <= d:
#         heappush(heap, (h,o) if h<o else (o,h))

# _max = 0
# while heap:
#     t = heappop(heap)
#     cnt = 1
#     tmp = []
#     while heap and t[0] == heap[0][0]:   # 시작점이 같은 것들.
#         t = heappop(heap)
#         cnt += 1
    
#     while heap and heap[0][0] < t[0]+d:
#         next = heappop(heap)
#         if next[1] <= t[0]+d:
#             cnt += 1
#         tmp.append(next)

#     for node in tmp:
#         heappush(heap, node)
    
#     if _max < cnt :
#         _max = cnt

# print(_max)
