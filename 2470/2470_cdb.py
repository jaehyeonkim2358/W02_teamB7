import sys
sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().split())))

def solution():
    start = 0
    end = n-1
    count = 0
    temp = [2000000000,0,0] # 가능한 결과의 최댓값과 그때의 인덱스 두 개 
    while start < end:
        value = arr[start] + arr[end] 
        if abs(value) < temp[0]:
            temp[0] = abs(value)
            temp[1] = start
            temp[2] = end
        if value == 0:
            break
        elif value < 0:
            start += 1
        else:
            end -= 1
    print(arr[temp[1]], arr[temp[2]])

solution()