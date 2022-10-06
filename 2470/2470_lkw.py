import sys
sys.stdin = open("W02/2470/input.txt","r")

n = int(input())
l = map(int, input().split())

def resovle(arr):
    left = 0
    right = len(arr)-1

    best_pair = (arr[left],arr[right])
    while left < right:
        a = arr[left]; b = arr[right]

        if a + b == 0:
            return (a,b)

        best_pair = (a,b) if abs(a+b) < abs(sum(best_pair)) else best_pair

        # 양쪽의 절대값이 같은 경우는 없다.
        # 서로 부호가 다른 경우엔 절대값이 같다면 위의 조건에서 return될 것이고,
        # 부호가 같은경우엔 특성값은 중복되지 않는다는 조건에 의해 절대값이 같을 수 없다.
        if abs(a) > abs(b):
            left += 1
        else:
            right -= 1

    return best_pair

print(*resovle(sorted(l)))