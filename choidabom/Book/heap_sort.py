# 힙(heap): '부모의 값이 자식의 값보다 항상 크다'는 조건을 만족하는 완전 이진 트리이다.
# 힙 정렬 알고리즘 구현하기

# 1. 힙에서 최댓값인 루트를 꺼낸다.
# 2. 루트 이외의 부분을 힙으로 만든다.

from typing import MutableSequence

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')


def heap_sort(a: MutableSequence):
    def down_heap(a: MutableSequence, left: int, right: int):
        # a[left] ~ a[right]를 힙으로 만들기
        temp = a[left]   # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl # 큰 값을 선택
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    
    n = len(a)

    for i in range((n-1) // 2, -1, -1): # a[i] ~ a[n-1]을 힙으로 만들기
        down_heap(a, i, n-1)

    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0] # 최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a, 0, i-1)    # a[0] ~ a[i-1]을 힙으로 만들기


if __name__ == "__main__":
    print('힙 정렬을 수행합니다.')

    num = int(sys.stdin.readline())
    x = []

    for i in range(num):
        input = int(sys.stdin.readline().strip())
        x.append(input)
    print(x)


    heap_sort(x)    # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}]: = {x[i]}')