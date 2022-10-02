# 1920: 수 찾기
import sys
# 이분 탐색를 위해서는 탐색할 리스트가 정렬되어있어야 한다. 

N = int(sys.stdin.readline())
A = sorted(list(map(int, input().split())))

N = int(sys.stdin.readline())
B = list(map(int, input().split()))

def binary_search(key, start, end, target):
    s = start
    e = end
    while s < e:
        # + 1 을 해줘야 한다. 해주지 않으면 무한 루프에 빠짐.
        # mid = (s + e) // 2
        mid = (s + e) // 2 + 1
        # if target[mid] >= key:
        if target[mid] > key:
            # e = mid
            e = mid - 1
        else:
            # s = mid + 1
            s = mid
    print(int(target[e] == key))

for b in B:
    binary_search(b, 0, N-1, A)
