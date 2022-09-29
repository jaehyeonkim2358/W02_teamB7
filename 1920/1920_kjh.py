n = int(input())
A = sorted(list(map(int, input().split())))

m = int(input())
B = list(map(int, input().split()))

def binary_search(key, start, end, target):
    s = start
    e = end
    while s < e:
        mid = (s + e) // 2
        if target[mid] >= key:
            e = mid
        else:
            s = mid+1
    print(int(target[e]==key))


for b in B:
    binary_search(b, 0, n-1, A)