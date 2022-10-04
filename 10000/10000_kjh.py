import sys

n = int(sys.stdin.readline().rstrip())

# 원의 좌표를 정렬
# 정렬 기준
# 1. 원의 왼쪽 시작좌표 오름차순(좌표값이 작은 것 부터)
# 2. 원의 길이 내림차순(길이가 긴 것 부터)
circles = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[0]-x[1], -x[1]))

def solution():
    stack = []
    count = 1

    for c in circles:
        # 우선 들어온 원에의해 영역수 1 증가함
        count += 1

        # 원의 왼쪽 좌표, 오른쪽 좌표
        l = c[0]-c[1]
        r = c[0]+c[1]
        # stack이 비어있는 경우 저장
        if not stack:
            # 순서대로, 원의 왼쪽 좌표, 오른쪽 좌표, 길이(지름)
            stack.append([l, r, r-l])
        # stack이 비어있지 않은 경우
        else:
            # 나를 포함하고 있지 않은 원을 모두 제거
            sub_len = 0     # 나를 포함하고 있지 않은 원 중 마지막 원의 길이를 저장할 변수
            while stack and stack[-1][1] <= l:
                sub_len = stack.pop()[2]

            # 나를 포함하고 있지 않던 마지막 원과 내가
            # 나를 포함하는 원을 양분하는지 확인
            if stack and sub_len+r-l == stack[-1][1]-stack[-1][0]:
                # 양분한다면 영역이 2개로 나눠지므로, 영역수를 1 증가
                count += 1
            # 현재 원 저장
            # 이때 지름에 sub_len을 더해주는 이유는
            # 이전에 있던 '나를 포함하지 않는 원 중 마지막 원'의 지름을 더한 값으로 
            # '나를 포함하는 원'을 양분하는지 확인하기 위함임
            stack.append([l, r, sub_len+r-l])
    
    return count

sys.stdout.write(f'{solution()}')