# BOJ 6549 히스토그램에서 가장 큰 직사각형
# 분할 정복
import sys


def solution(histogram, s, e):
    # s == e 일 때는 높이가 히스토그램의 넓이임
    if s == e:
        return histogram[s]

    # 중간 index를 이용해서 좌, 우 최대 넓이를 계산
    m = (s+e)//2

    # 왼쪽 넓이와 오른쪽 넓이를 구한 뒤
    # 둘 중 큰쪽의 넓이를 저장
    left_width = solution(histogram, s, m)
    right_width = solution(histogram, m+1, e)
    max_area = max(left_width, right_width)

    # 가운데 넓이를 구하기
    # 가운데 넓이는 m부터 시작해서, 왼쪽 또는 오른쪽으로 넓혀가며 계산함
    # 이때, 왼쪽 막대의 높이와 오른쪽 막대의 높이를 비교해서 큰쪽으로 넓혀감
    l_idx = m
    r_idx = m
    height = histogram[m]
    mid_width = height
    while s < l_idx and r_idx < e:
        if histogram[l_idx-1] < histogram[r_idx+1]:
            r_idx += 1
            height = min(height, histogram[r_idx])
        else:
            l_idx -= 1
            height = min(height, histogram[l_idx])
            
        mid_width = max(mid_width, height * (r_idx-l_idx+1))

    # 아직 비교하지 못한 오른쪽 범위가 존재하면, 끝지점에 닿을 때 까지 반복하며 최대 넓이 갱신
    while r_idx < e:
        r_idx += 1
        height = min(height, histogram[r_idx])
        mid_width = max(mid_width, height * (r_idx-s+1))

    # 아직 비교하지 못한 왼쪽 범위가 존재하면, 시작지점에 닿을 때 까지 반복하며 최대 넓이 갱신
    while s < l_idx:
        l_idx -= 1
        height = min(height, histogram[l_idx])
        mid_width = max(mid_width, height * (e-l_idx+1))
        
    # 아까 계산해주었던 왼쪽-오른쪽 넓이 중 큰값과, 지금 구한 가운데 넓이 중 큰 값을 return
    max_area = max(max_area, mid_width)
    return max_area


tc = list(map(int, sys.stdin.readline().split()))
while tc[0] != 0:
    ans = solution(tc[1:], 0, tc[0]-1)
    sys.stdout.write(f'{ans}\n')
    tc = list(map(int, sys.stdin.readline().split()))