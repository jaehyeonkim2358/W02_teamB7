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


# 재현이형 코드.
def binary_search(key, start, end, target):
    s = start
    e = end

    # 1.
    # ##################################################
    #         |-->          2.key             4.key
    #         | start(=1.key) | end=mid(=3.key) |
    # ##################################################
    # '같거나'의 조건이 붙은 쪽은 사이값이 없게 된다.
    # 두개 남았을 때를 위해 '같거나' 조건이 없는 쪽으로 mid를 줘야함.
    # 이 문제는 찾고자 하는 값이 있는지 여부만을 리턴하면 되기 때문에,
    # s와 e가 같아지는 상황까지 체크하지 않아도 된다. 같아 진 후에 s=e=index의 value가 찾고자 하는 값인지만 확인하면 되기 때문이다.   

    while s < e:
        mid = (s + e) // 2 + 1
        if key < target[mid]:
            e = mid - 1
        else: # target[mid] <= key
            s = mid 

      # 2.
      # ##################################################
      #       1.key               3.key            <--|
      #         | start=mid(=2.key) |   end(=4.key)   |
      # ##################################################
      # '같거나'의 조건이 붙은 쪽은 사이값이 없게 된다.
      # 두개 남았을 때를 위해 '같거나' 조건이 없는 쪽으로 mid를 줘야함.

      # mid = (s + e) // 2
      # if key <= target[mid]:
      #     e = mid
      # else: # target[mid] < key
      #     s = mid + 1


    print(int(target[e]==key))

        