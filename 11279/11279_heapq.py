# 11279: 최대 힙
import sys
import heapq
heap = []
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    i = int(sys.stdin.readline().rstrip())
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-i, i))