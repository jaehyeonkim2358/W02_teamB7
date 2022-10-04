import sys
from heapq import * # heapq 의 heap은 최소힙.
# heappushpop() : push first, then pop 의 결과에 맞게 pop을 해줌. 
#                 heappush() then heappop() 보다 효율적으로 동작.
# heapreplace() : pop first, then push 의 순서에 맞게 원래 힙에서 pop을 하고 push를 해줌
#                 heappop() then heappush() 보다 효율적으로 동작.
# 아마 다운힙을 활용해 효율적으로 구현하지 않았을까.

sys.stdin = open("1655/input.txt","r")

n = int(input())
l_heap = []
r_heap = []

to_left = False

for i in range(1, n + 1):
    num = int(sys.stdin.readline())
    if i % 2 == 1:  # 전체가 홀수개 일 때... (짝수개인 상태에서 하나 추가.)
        heappush(l_heap, (-num,num))

        if r_heap and l_heap[0][1] > r_heap[0][1]:
            node = heappop(l_heap)
            heappush(r_heap, (-node[0],node[1]))
            print(r_heap[0][1])
            to_left = True
        else:
            print(l_heap[0][1])

    else: # 전체가 짝수개 일 때... (홀수개인 상태에서 하나 추가.)
        heappush(l_heap if to_left else r_heap, (-num,num) if to_left else (num,num)) # 개수 하나 모자란 곳에 push.

        if l_heap[0][1] > r_heap[0][1]:   # 왼쪽 최대값이 오른쪽 최소값보다 클 때.
            l_max_node = l_heap[0]
            r_min_node = heapreplace(r_heap, (-l_max_node[0],l_max_node[1]))
            heapreplace(l_heap, (-r_min_node[0],r_min_node[1]))
        print(l_heap[0][1])    # 짝수 일때는 왼쪽값 (중간의 둘 중에 작은 값).
        to_left = False
            

