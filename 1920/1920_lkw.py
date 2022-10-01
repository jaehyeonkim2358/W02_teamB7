import sys
sys.stdin = open("1920/input.txt","r")

n = int(input())
arr = sorted(map(int, input().split()))
m, *keys = map(int, sys.stdin.read().split())

def bi_search(arr, key):
    left = 0
    right = n-1

    while left <= right :
        mid = (left + right) // 2

        # 원소 두개가 남은 상황에서는 mid는 왼쪽 원소
        # 경우의 수.
        # ##################################################
        #       1.key              3.key           5.key
        #         | left=mid(=2.key) | right(=4.key) |
        # ##################################################
        # 2는 바로 찾게 되고,
        # 4 는 left와 right가 같아져 결국 찾게되고,
        # 1,3,5 는 left와 rigth가 교차된다.

        if arr[mid] == key:
            return 1

        if arr[mid] < key:  # key가 중간값 보다 클 때 -> 중간값 보다 오른쪽에 있을 때
            left = mid + 1
        else : # key < arr[mid]  # key가 중간값 보다 작을 때 -> 중간값 보다 왼쪽에 있을 때
            right = mid - 1

    return 0

for key in keys:
    print(bi_search(arr, key))
        