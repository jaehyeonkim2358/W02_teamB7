# 이진 검색 알고리즘
# 이진 탐색 트리: 정렬된 구조를 저장하고 탐색하는 '자료구조'
# 이진 검색: 정렬된 배열에서 값을 찾아내는 '알고리즘'자체
from typing import Any, Sequence

def bin_search(a: Sequence, key: Any):
    # 시퀀스 a에서 key와 일치하는 원소를 이진 검색
    pl = 0          # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1 # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            # pc가 중앙 원소의 인덱스인데 결국에는 1이라고 더 커야하기에 + 1
            pl = pc + 1     # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pl = pc - 1     # 검색 범위를 앞쪽 절반으로 좁힘

        if pl > pr: 
            break
        return -1   # 검색 실패

if __name__ == "__main__":
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열 x를 생성

    print('배열 데이터를 오름차순으로 입력하세요.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i-1]:
                break

    key = int(input('검색할 값을 입력하세요.')) # 검색할 키값 key를 입력

    idx = bin_search(x, key)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
