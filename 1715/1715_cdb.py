import sys
# heapq는 리스트를 힙처럼 사용할 수 있게 해주는 모듈이다.
import heapq
sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())   # 최소 비교 횟수

# 각 묶음의 카드의 수 A, B => 두 묶음을 합쳐서 하나로 만드는데 A+B번 비교
# N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 구함 !
result = 0
cards = []

for i in range(N):
    heapq.heappush(cards, int(sys.stdin.readline().strip()))

# cards의 갯수가 1이면 비교가 필요없기 때문에 0을 출력
if len(cards) == 1:
    print(0)
else:
    while len(cards) > 1:
        # 오름차순으로하고, 작은 수부터 2개씩 묶어서 더해줘야 가장 효율적인 방법 => 그리디
        # plus에 최소 힙에서 뽑은 가장 작은 원소 하나, 또 하나를 더해준다.
        plus = heapq.heappop(cards) + heapq.heappop(cards)
        # 누적이기 때문에 plus를 result에 넣어준다.
        result += plus
        # plus가 다시 cards에 들어가야하기에 push해서 넣어준다.
        heapq.heappush(cards, plus)

    print(result)