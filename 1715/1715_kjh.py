import heapq
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

cards = []
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

sum = 0
while len(cards) > 1:
    r1 = heapq.heappop(cards)
    r2 = heapq.heappop(cards)
    sum += r1 + r2
    heapq.heappush(cards, r1+r2)

print(sum)