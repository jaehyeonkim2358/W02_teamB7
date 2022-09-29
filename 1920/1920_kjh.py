n = int(input())
# 이분 탐색을 위해, 탐색할 리스트는 정렬되어있어야 한다.
A = sorted(list(map(int, input().split())))

m = int(input())
B = list(map(int, input().split()))

def binary_search(key, start, end, target):
    s = start
    e = end
    while s < e:
        # mid = (s + e) // 2
        mid = (s + e) // 2 + 1
        # if target[mid] >= key:
        if target[mid] > key:
            # e = mid
            e = mid - 1
        else:
            # s = mid + 1
            s = mid
    print(int(target[e]==key))


for b in B:
    binary_search(b, 0, n-1, A)