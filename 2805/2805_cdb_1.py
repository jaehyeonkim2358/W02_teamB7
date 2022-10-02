# 2805: 나무 자르기

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def solution(target, key):
    # end 값을 max(target)으로 잡는다고 생각을 못 했다.
    start, end = 0, max(target)
    while start < end:
        mid = (start + end) // 2 + 1
        # 원래 이분탐색은  => if target[mid] > key:
        # 하지만, 절단기 높이 H를 계속 탐색해야하기 때문에 
        # 중간인 mid부터 탐색하여 get_height 함수의 return 값, 
        # 1. 즉 sum 값이 key보다 작으면 end 값을 줄이고, 
        # 2. sum 값이 key보다 크면 start 값을 높인다.
        if get_height(target, mid) < key:
            end = mid - 1
        else:
            start = mid
    return start

def get_height(target, H):
    sum = 0
    for t in target:
        sum += (t-H if t>H else 0)
    return sum

sys.stdout.write(f'{solution(trees, M)}')