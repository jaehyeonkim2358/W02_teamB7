import sys

n, c = map(int, sys.stdin.readline().split())
house = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

def solution(target, key):
    s = 1
    e = target[len(target)-1] - target[0]
    while s < e:
        m = (s+e) // 2 + 1
        # m을 최소 거리로 할 때, 
        # '설치 가능한 공유기의 최대 갯수' < '설치 하려는 공유기의 갯수' 이면
        # 최소 거리를 더 늘려도 됨 
        # (최소 거리가 증가하면 전체 간격이 늘어나서 설치 가능한 공유기 갯수가 감소하므로)
        if count(target, m) < key:
            e = m - 1
        # 그렇지 않다면, 반대로 최소 거리를 줄여야 함
        else:
            s = m + 1
    return e

# (정렬된 집 좌표, 최소거리)를 파라미터로 전달받아 
# 설치 가능한 공유기 최대 갯수를 return
def count(target, min_dist):
    pre = 0     # 직전에 설치한 집의 index. 0번째 집에 설치하고 시작
    count = 1   # 설치 횟수를 계산. 0번째 집에 설치했기 때문에 횟수는 1부터 시작
    for i in range(1, len(target)):
        # 두 집 사이의 거리가 최소 거리보다 작으면 설치 불가
        if target[i]-target[pre] < min_dist:
            continue
        # 그렇지 않으면 설치
        else:
            pre = i     # i에 설치했으므로, 다음 탐색부터는 '직전에 설치한 집의 index'가 i가 됨
            count += 1  # 설치 횟수 1 증가
    return count

sys.stdout.write(f'{solution(house, c)}')
