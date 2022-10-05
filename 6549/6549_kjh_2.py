# BOJ 6549 히스토그램에서 가장 큰 직사각형
# 스택
import sys


def solution(histogram):
    stack = []      # histogram의 Index를 가지는 스택
    max_area = 0    # histogram에서 가장 큰 직사각형의 넓이를 저장할 변수

    # 전체 사각형을 한번씩 순회
    for i in range(len(histogram)):
        # stack의 값을 pop()해주면서 max_area를 갱신해주는데,
        # 1. stack이 비거나, 
        # 2. 현재 순회중인 사각형의 높이가 stack의 top에 있는 Index의 높이보다 클때까지 반복
        while stack and histogram[i] <= histogram[stack[-1]]:
            # 높이를 구할 때 pop()을 해준다.
            height = histogram[stack.pop()]
            # 넓이는 다음과 같이 계산
            # 1. stack이 비기 전까지는 현재 순회중인 Index(=i)에서 
            # stack의 top에 저장된 Index(방금 pop한 값 이전에 stack에 저장되어있던 index) 직전까지의 길이를 가로길이로 계산한다.
            # 직전까지의 길이를 넓이로 하는 이유는 현재 top의 index의 높이는 heigth과 다르기 때문
            # 2. stack이 비었다면, 현재 순회중인 Index까지의 길이(=i)를 가로 길이로 계산한다.
            # (stack이 비었다는 것은, 현재 순회중인 Index(=i)의 높이가 이전까지 저장한 index의 각각의 높이보다 작았다는 뜻 이므로)
            width = i-stack[-1]-1 if stack else i
            # 최대 넓이 갱신
            max_area = max(max_area, height * width)
        stack.append(i)

    # 전체 사각형을 순회 한 뒤에도 stack에 값이 남아있을 수 있다.
    # (마지막 순회의 값보다 작은 사각형 또는 점점 큰 사각형만 들어와서 pop이 일어나지 않을 경우 등)
    # 따라서 stack에 남은 값을 하나씩 꺼내서 마찬가지로 넓이를 구해주고 max_area를 갱신한다.
    while stack:
        height = histogram[stack.pop()]
        width = len(histogram)-stack[-1]-1 if stack else len(histogram)
        max_area = max(max_area, height * width)

    return max_area


tc = list(map(int, sys.stdin.readline().split()))
while tc[0] != 0:
    ans = solution(tc[1:])
    sys.stdout.write(f'{ans}\n')
    tc = list(map(int, sys.stdin.readline().split()))